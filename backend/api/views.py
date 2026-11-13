"""HTTP API views.

Scaffold only: the single endpoint is the liveness probe defined by the
TypeSpec contract in ``contract/main.tsp``.
"""

from django.http import HttpRequest, HttpResponse, JsonResponse


def health(request: HttpRequest) -> HttpResponse:
    """Return ``{"status": "ok"}`` as required by the TypeSpec contract."""
    return JsonResponse({"status": "ok"})
