from rest_framework.decorators import api_view
from rest_framework.response import Response


def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return Response(routes, safe=False)
