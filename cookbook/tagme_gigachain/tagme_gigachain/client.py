"""HTTP clients responsible for communicating with the TagMe backend."""

import json
import logging
import os
from typing import Any, List, Optional
from urllib.parse import urlparse

import aiohttp
import pandas as pd
import requests
from aiohttp import hdrs
from aiohttp.typedefs import StrOrURL

from .entities import DialogData, FunctionDef, FunctionResponse, MissingFunctionsError

logger = logging.getLogger(__name__)


class TagmeIntegrationClient:
    """Base configuration shared by the synchronous and asynchronous clients."""

    def __init__(
        self,
        token: Optional[str] = None,
        trust_env: bool = False,
        ssl: bool = True,
        ignore_missing_functions: bool = True,
        base_url: Optional[str] = None,
    ) -> None:
        """Initialize TagMe client settings and validate credentials.

        Args:
            token (Optional[str]): Explicit API token if not loaded from the environment.
            trust_env (bool): Whether to inherit proxy and auth settings from the host environment.
            ssl (bool): Controls SSL certificate verification behaviour for outgoing requests.
            ignore_missing_functions (bool): Skip raising when TagMe lacks referenced function definitions.
            base_url (Optional[str]): Override for the TagMe service root URL.
        """

        self.token = token or os.environ.get("TAGME_TOKEN")
        self.validate_token()

        raw_url = base_url or os.environ.get(
            "TAGME_BASE_URL", "https://tagme.sberdevices.ru/dev/chatwm/plugin_statistics/trace"
        )
        parsed = urlparse(raw_url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError(f"Invalid TAGME_BASE_URL value: {raw_url}")
        self._base_url = f"{parsed.scheme}://{parsed.netloc}"
        self._base_path = parsed.path.rstrip("/")

        self.connector: Optional[aiohttp.TCPConnector] = None
        self._session: Any = None
        self.trust_env = trust_env
        self.ssl = ssl
        self.ignore_missing_functions = ignore_missing_functions

    def validate_token(self):
        """Ensure that a TagMe access token is provided."""

        if not self.token:
            raise ValueError("TagMe access token is required")

    def get_headers(self):
        """Return default headers for TagMe API calls."""

        return {"X-API-Token": self.token, "Content-Type": "application/json"}


class TagmeIntegrationClientAsync(TagmeIntegrationClient):
    """Asynchronous HTTP client built on top of ``aiohttp``."""

    def __init__(
        self,
        token: Optional[str] = None,
        trust_env: bool = False,
        ssl: bool = True,
        ignore_missing_functions: bool = True,
        base_url: Optional[str] = None,
    ) -> None:
        """Configure the async TagMe client using shared and aiohttp specific settings.

        Args:
            token (Optional[str]): Explicit API token if not loaded from the environment.
            trust_env (bool): Whether to inherit proxy and auth settings from the host environment.
            ssl (bool): Controls SSL certificate verification behaviour for outgoing requests.
            ignore_missing_functions (bool): Skip raising when TagMe lacks referenced function definitions.
            base_url (Optional[str]): Override for the TagMe service root URL.
        """

        super().__init__(token, trust_env, ssl, ignore_missing_functions, base_url)
        self._session: Optional[aiohttp.ClientSession] = None

    def get_session(self) -> aiohttp.ClientSession:
        """Return a shared ``aiohttp`` session configured for the API."""

        if self.connector is None:
            self.connector = aiohttp.TCPConnector(limit_per_host=1)
        if self._session is None:
            self._session = aiohttp.ClientSession(
                connector=self.connector,
                base_url=self._base_url,
                trust_env=self.trust_env,
            )
        return self._session

    async def request(
        self,
        method: str,
        url: StrOrURL,
        data: Any = None,
        headers: Optional[dict] = None,
        **kwargs,
    ):
        """Execute an API call and deserialize the JSON response."""

        session = self.get_session()
        req_headers = self.get_headers()
        if headers:
            req_headers.update(headers)
        if data:
            data = json.dumps(data, ensure_ascii=False)
        target_url = kwargs.pop("base_path", self._base_path) + (url if isinstance(url, str) else url.path)
        async with session.request(
            method,
            target_url,
            data=data,
            headers=req_headers,
            ssl=self.ssl,
            **kwargs,
        ) as resp:
            try:
                resp.raise_for_status()
                return await resp.json()
            except aiohttp.ClientError as err:
                resp_json = await resp.json()
                if resp_json.get("code") == "FUNCTIONS_NOT_FOUND":
                    raise MissingFunctionsError(resp_json.get("missing", [])) from err
                logger.error("Error during TagMe request: %s \nServer response: %s", err, resp_json)
                raise

    async def health_check(self):
        """Verify that the TagMe service responds to ``/health``."""

        return await self.request(hdrs.METH_GET, "/health")

    async def send_dialog(self, dialog: DialogData, ignore_missing_functions: Optional[bool] = None):
        """Submit a dialog transcript for annotation."""

        return await self.request(
            hdrs.METH_POST,
            "/api/dialog",
            data=dialog.asdict(),
            params={
                "ignore_missing_functions": str(
                    ignore_missing_functions if ignore_missing_functions is not None else self.ignore_missing_functions
                )
            },
        )

    async def send_functions(self, functions: List[FunctionDef]):
        """Send function descriptions that TagMe can use for tool calls."""

        return await self.request(
            hdrs.METH_POST,
            "/api/functions",
            [func.asdict() for func in functions],
        )

    async def get_functions(self) -> List[FunctionResponse]:
        """Fetch function metadata currently available on TagMe."""

        resp = await self.request(hdrs.METH_GET, "/api/functions")
        return [FunctionResponse.from_dict(func) for func in resp.get("functions", [])]

    async def get_markup_statistics(self):
        """Retrieve annotation statistics."""

        return await self.request(hdrs.METH_GET, "/api/markup_statistics")

    async def get_markup_quality(self):
        """Retrieve quality metrics for completed annotations."""

        return await self.request(hdrs.METH_GET, "/api/markup_quality")

    async def get_results(self):
        """Retrieve annotated dialog results."""

        return await self.request(hdrs.METH_GET, "/api/results")

    async def get_results_df(self) -> pd.DataFrame:
        """Return annotation results as a Pandas ``DataFrame`` for analysis."""

        results = await self.get_results()
        return pd.DataFrame(results)

    async def close(self):
        """Close the shared ``aiohttp`` session if it was created."""

        if self._session is not None:
            await self._session.close()


class TagmeIntegrationClientSync(TagmeIntegrationClient):
    """Synchronous TagMe client implemented with the ``requests`` library."""

    def __init__(
        self,
        token: Optional[str] = None,
        trust_env: bool = False,
        ssl: bool = True,
        ignore_missing_functions: bool = True,
        base_url: Optional[str] = None,
    ) -> None:
        """Configure the sync TagMe client using shared and requests specific settings.

        Args:
            token (Optional[str]): Explicit API token if not loaded from the environment.
            trust_env (bool): Whether to inherit proxy and auth settings from the host environment.
            ssl (bool): Controls SSL certificate verification behaviour for outgoing requests.
            ignore_missing_functions (bool): Skip raising when TagMe lacks referenced function definitions.
            base_url (Optional[str]): Override for the TagMe service root URL.
        """

        super().__init__(token, trust_env, ssl, ignore_missing_functions, base_url)
        self._session: Optional[requests.Session] = None

    def get_session(self) -> requests.Session:
        """Return a cached ``requests`` session configured with trust options."""

        if self._session is None:
            self._session = requests.Session()
            self._session.trust_env = self.trust_env
        assert isinstance(self._session, requests.Session)
        return self._session

    def make_url(self, url: StrOrURL, base_path: str = "") -> StrOrURL:
        """Resolve a relative endpoint path into an absolute URL."""

        if isinstance(url, str):
            return f"{self._base_url}{base_path}/{url.lstrip('/')}"
        return url

    def request(
        self,
        method: str,
        url: str,
        data: Any = None,
        headers: Optional[dict] = None,
        **kwargs,
    ):
        """Execute an HTTP request and parse the JSON body."""

        session = self.get_session()
        req_headers = self.get_headers()
        if headers:
            req_headers.update(headers)
        if data is not None:
            data = json.dumps(data, ensure_ascii=False)
        target_url = str(self.make_url(url, kwargs.pop("base_path", self._base_path)))

        resp: Optional[requests.Response] = None
        try:
            resp = session.request(method, url=target_url, data=data, headers=req_headers, verify=self.ssl, **kwargs)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as err:
            resp_json: Any = None
            if resp is not None:
                try:
                    resp_json = resp.json()
                except Exception:  # pylint: disable=broad-except
                    resp_json = getattr(resp, "text", None)
            if isinstance(resp_json, dict) and resp_json.get("code") == "FUNCTIONS_NOT_FOUND":
                raise MissingFunctionsError(resp_json.get("missing", [])) from err
            logger.error("Error during TagMe request: %s \nServer response: %s", err, resp_json)
            raise

    def send_dialog(self, dialog: DialogData, ignore_missing_functions: Optional[bool] = None):
        """Submit a dialog transcript for annotation."""

        return self.request(
            "POST",
            "/api/dialog",
            data=dialog.asdict(),
            params={
                "ignore_missing_functions": str(
                    ignore_missing_functions if ignore_missing_functions is not None else self.ignore_missing_functions
                )
            },
        )

    def send_functions(self, functions: List[FunctionDef]):
        """Upload function definitions that TagMe can reference."""

        self.request(
            "POST",
            "/api/functions",
            data=[func.asdict() for func in functions],
        )

    def get_functions(self) -> List[FunctionResponse]:
        """Fetch function metadata currently registered on TagMe."""

        resp = self.request("GET", "/api/functions")
        return [FunctionResponse.from_dict(func) for func in resp.get("functions", [])]

    def get_markup_statistics(self):
        """Retrieve annotation statistics."""

        return self.request("GET", "/api/markup_statistics")

    def get_markup_quality(self):
        """Retrieve quality metrics for completed annotations."""

        return self.request("GET", "/api/markup_quality")

    def get_results(self):
        """Retrieve annotated dialog results."""

        return self.request("GET", "/api/results")

    def get_results_df(self) -> pd.DataFrame:
        """Return annotation results as a Pandas ``DataFrame`` for analysis."""

        results = self.get_results()
        return pd.DataFrame(results)

    def close(self):
        """Close the cached ``requests`` session if it exists."""

        if self._session is not None:
            self._session.close()

    def health_check(self):
        """Verify that the TagMe service responds to ``/health``."""

        return self.request("GET", "/health")
