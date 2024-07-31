import requests
from requests.auth import HTTPBasicAuth


def check_ping(ip, port, username, password):
    response = requests.get(f"http://{ip}:{port}/ari/asterisk/ping",
                            auth=HTTPBasicAuth(username, password)
                            )
    if response.status_code == 200:
        ping = response.json()['ping']
    else:
        ping = -1
    return ping


def get_server(costumers):
    data = []
    for costumer in costumers:
        if not costumer.server.status:
            continue
        server = costumer.server
        ip = server.ip
        port = server.port
        username = server.username
        password = server.password

        ping = check_ping(ip, port, username, password)

        response = requests.get(f"http://{ip}:{port}/ari/asterisk/info",
                                auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            startup_time = response.json()['status']['startup_time']
            last_reload_time = response.json()['status']['last_reload_time']

        else:
            startup_time = -1
            last_reload_time = -1

        response = requests.get(f"http://{ip}:{port}/ari/endpoints",
                                auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            endpoints = []
            for result in response.json():
                abonent = result['resource']
                status = result['state']
                technology = result['technology']
                endpoint = {
                    'abonent': abonent,
                    'status': status,
                    'technology': technology
                }
                endpoints.append(endpoint)
        else:
            endpoints = []

        obj = {
            'ip': ip,
            'port': port,
            'username': username,
            'password': password,
            'ping': ping,
            'startup_time': startup_time,
            'last_reload_time': last_reload_time,
            'endpoints': endpoints
        }
        data.append(obj)
    return data


def get_endpoint(costumers):
    data = []
    for costumer in costumers:
        if not costumer.server.status:
            continue
        server = costumer.server
        ip = server.ip
        port = server.port
        username = server.username
        password = server.password

        response = requests.get(f"http://{ip}:{port}/ari/endpoints",
                                auth=HTTPBasicAuth(username, password))

        if response.status_code == 200:
            endpoints = []
            for result in response.json():
                abonent = result['resource']
                status = result['state']
                technology = result['technology']
                endpoint = {
                    'abonent': abonent,
                    'status': status,
                    'technology': technology
                }
                endpoints.append(endpoint)
        else:
            endpoints = []
        obj = {
            'server': server,
            'endpoints': endpoints
        }
        data.append(obj)
    return data
