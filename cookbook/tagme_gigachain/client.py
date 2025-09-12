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

from .types import FunctionDef, FunctionResponse, MissingFunctionsError

logger = logging.getLogger(__name__)


class TagmeIntegrationClient:
    def __init__(
        self,
        token: Optional[str] = None,
        trust_env: bool = False,
        ssl: bool = True,
        ignore_missing_functions: bool = True,
    ) -> None:
        self.token = token or os.environ.get("TAGME_GIGACHAIN_TOKEN")
        self.validate_token()

        raw_url = os.environ.get("TAGME_GIGACHAIN_BASE_URL", "http://localhost:8000")
        parsed = urlparse(raw_url)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError(f"Некорректный TAGME_GIGACHAIN_BASE_URL: {raw_url}")
        self._base_url = f"{parsed.scheme}://{parsed.netloc}"
        self._base_path = parsed.path.rstrip("/")

        self.connector: Optional[aiohttp.TCPConnector] = None
        self._session: Any = None
        self.trust_env = trust_env
        self.ssl = ssl
        self.ignore_missing_functions = ignore_missing_functions

    def validate_token(self):
        if not self.token:
            raise ValueError("Не предоставлен токен доступа TagMe")

    def get_headers(self):
        return {"X-API-Token": self.token, "Content-Type": "application/json"}


class TagmeIntegrationClientAsync(TagmeIntegrationClient):
    def __init__(
        self,
        token: Optional[str] = None,
        trust_env: bool = False,
        ssl: bool = True,
        ignore_missing_functions: bool = True,
    ) -> None:
        super().__init__(token, trust_env, ssl, ignore_missing_functions)
        self._session: Optional[aiohttp.ClientSession] = None

    def get_session(self) -> aiohttp.ClientSession:
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
                logger.error("Ошибка при запросе к TagMe: %s \nОтвет сервера: %s. ", err, resp_json)
                raise

    async def health_check(self):
        return await self.request(hdrs.METH_GET, "/health", base_path="")

    async def send_dialog(self, dialog):
        return await self.request(
            hdrs.METH_POST,
            "/dialog",
            data=dialog,
            params={"ignore_missing_functions": str(self.ignore_missing_functions)},
        )

    async def send_functions(self, functions: List[FunctionDef]):
        await self.request(
            hdrs.METH_POST,
            "/functions",
            [func.asdict() for func in functions],
        )

    async def get_functions(self) -> List[FunctionResponse]:
        resp = await self.request(hdrs.METH_GET, "/functions")
        return [FunctionResponse.from_dict(func) for func in resp.get("functions", [])]

    async def get_markup_statistics(self):
        return await self.request(hdrs.METH_GET, "/markup_statistics")

    async def get_markup_quality(self):
        return await self.request(hdrs.METH_GET, "/markup_quality")

    async def get_results(self):
        return await self.request(hdrs.METH_GET, "/results")

    async def get_results_df(self) -> pd.DataFrame:
        results = await self.get_results()
        return pd.DataFrame(results)

    async def close(self):
        if self._session is not None:
            await self._session.close()


class TagmeIntegrationClientSync(TagmeIntegrationClient):
    def __init__(
        self,
        token: Optional[str] = None,
        trust_env: bool = False,
        ssl: bool = True,
        ignore_missing_functions: bool = True,
    ) -> None:
        super().__init__(token, trust_env, ssl, ignore_missing_functions)
        self._session: Optional[requests.Session] = None

    def get_session(self) -> requests.Session:
        if self._session is None:
            self._session = requests.Session()
            self._session.trust_env = self.trust_env
        assert isinstance(self._session, requests.Session)
        return self._session

    def make_url(self, url: StrOrURL, base_path: str = "") -> StrOrURL:
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
            logger.error("Ошибка при запросе к TagMe: %s \nОтвет сервера: %s. ", err, resp_json)
            raise

    def send_dialog(self, dialog):
        return self.request(
            "POST",
            "/dialog",
            data=dialog,
            params={"ignore_missing_functions": self.ignore_missing_functions},
        )

    def send_functions(self, functions: List[FunctionDef]):
        self.request(
            "POST",
            "/functions",
            data=[func.asdict() for func in functions],
        )

    def get_functions(self) -> List[FunctionResponse]:
        resp = self.request("GET", "/functions")
        return [FunctionResponse.from_dict(func) for func in resp.get("functions", [])]

    def get_markup_statistics(self):
        return self.request("GET", "/markup_statistics")

    def get_markup_quality(self):
        return self.request("GET", "/markup_quality")

    def get_results(self):
        return self.request("GET", "/results")

    def get_results_df(self) -> pd.DataFrame:
        results = self.get_results()
        return pd.DataFrame(results)

    def close(self):
        if self._session is not None:
            self._session.close()

    def health_check(self):
        return self.request("GET", "/health", base_path="")
