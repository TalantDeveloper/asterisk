import requests
from requests.auth import HTTPBasicAuth


def get_applications():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = 'Qosim123!'
    ASTERISK_HOST = '192.168.30.56'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/applications/'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_asterisk_info():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = 'Qosim123!'
    ASTERISK_HOST = '192.168.30.56'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/asterisk/info/'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_asterisk_ping():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = 'Qosim123!'
    ASTERISK_HOST = '192.168.30.56'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/asterisk/ping/'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_asterisk_modules():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = 'Qosim123!'
    ASTERISK_HOST = '192.168.30.56'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/asterisk/modules/'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_asterisk_logging():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = 'Qosim123!'
    ASTERISK_HOST = '192.168.30.56'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/asterisk/logging'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_asterisk_variable():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/asterisk/variable'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_bridges():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/bridges'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_channels():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/channels'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_deviceStates():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/deviceStates'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_endpoints():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/endpoints'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_events():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/events'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_mailboxes():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/mailboxes/'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_playbacks(playback_id):
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/playbacks/{playback_id}'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_recordings_stored():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/recordings/stored'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response


def get_sounds():
    # Replace these variables with your actual ARI credentials and Asterisk server details
    ARI_USERNAME = 'asterisk'
    ARI_PASSWORD = '@Botirjon06'
    ASTERISK_HOST = '192.168.30.48'
    ARI_PORT = '8088'  # Default ARI port

    # The URL for fetching channel data
    ARI_URL = f'http://{ASTERISK_HOST}:{ARI_PORT}/ari/sounds/'

    # Make the GET request to the ARI
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(ARI_USERNAME, ARI_PASSWORD))

    # Check the response status
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        return channels_data
    else:
        return response
