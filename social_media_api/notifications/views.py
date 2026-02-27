from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
def get_notifications(request):
    notifications = request.user.notifications.all().order_by('-timestamp')
    data = [{"actor": n.actor.username, "verb": n.verb} for n in notifications]
    return Response(data)
