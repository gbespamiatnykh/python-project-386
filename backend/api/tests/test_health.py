"""Smoke test for the health endpoint.

The test performs a real HTTP request against a live Django server
(pytest-django ``liveserver`` fixture) and asserts the response matches the
TypeSpec contract (``contract/main.tsp``): ``{"status": "ok"}``.
"""

import json
import urllib.request

from pytest_django.live_server_helper import LiveServer


def test_health_endpoint_matches_contract(liveserver: LiveServer) -> None:
    """GET /api/health/ answers 200 with the contract JSON."""
    url = f"{liveserver.url}/api/health/"
    with urllib.request.urlopen(url) as response:
        assert response.status == 200
        assert response.headers["Content-Type"].startswith("application/json")
        body = json.loads(response.read())

    assert body == {"status": "ok"}


def test_health_endpoint_without_trailing_slash(liveserver: LiveServer) -> None:
    """GET /api/health (as emitted by TypeSpec) also answers 200."""
    url = f"{liveserver.url}/api/health"
    with urllib.request.urlopen(url) as response:
        assert response.status == 200
        body = json.loads(response.read())

    assert body == {"status": "ok"}
