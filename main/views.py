from django.shortcuts import render
from .models import Server, Costumer
from django.contrib.auth.decorators import login_required
from .functions import get_server


@login_required(login_url='login')
def welcome_view(request):
    user = request.user
    costumers = Costumer.objects.filter(user=user)
    try:
        servers = get_server(costumers)
    except Exception as e:
        pass
    print(servers)
    context = {
        'costumers': costumers,
        'servers': servers
    }
    return render(request, 'main/welcome.html', context)


def index(request):
    print(request.user)
    return render(request, 'main/index.html')
