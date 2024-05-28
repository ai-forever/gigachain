"""Integration test for Polygon API Wrapper."""
<<<<<<< HEAD

=======
>>>>>>> langchan/master
from langchain_community.utilities.polygon import PolygonAPIWrapper


def test_get_last_quote() -> None:
    """Test for getting the last quote of a ticker from the Polygon API."""
    polygon = PolygonAPIWrapper()
    output = polygon.run("get_last_quote", "AAPL")
    assert output is not None
