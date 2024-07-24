from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import function


@api_view()
def welcome(request):
    data = function.get_applications()
    return Response(data)


@api_view()
def asterisk_info(request):
    info = function.get_asterisk_info()
    ping = function.get_asterisk_ping()
    modules = function.get_asterisk_modules()
    logging = function.get_asterisk_logging()
    data = {
        'info': info,
        'ping': ping,
        'modules': modules,
        'logging': logging
    }
    return Response(data)


@api_view()
def asterisk_variable(request):
    data = function.get_asterisk_variable()
    return Response(data)


@api_view()
def bridges(request):
    data = function.get_bridges()
    return Response(data)


@api_view()
def channels(request):
    data = function.get_channels()
    return Response(data)


@api_view()
def device_states(request):
    data = function.get_deviceStates()
    return Response(data)


@api_view()
def endpoints(request):
    data = function.get_endpoints()
    return Response(data)


@api_view()
def events(request):
    data = function.get_events()
    return Response(data)


@api_view()
def mailboxes(request):
    data = function.get_mailboxes()
    return Response(data)


@api_view()
def recordings_stored(request):
    data = function.get_recordings_stored()
    return Response(data)


@api_view()
def sounds(request):
    data = function.get_sounds()
    return Response(data)

