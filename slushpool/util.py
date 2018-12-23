import requests


def fetch_json(url):
    """ Common method to fetch JSON from Slushpool and check response code. """
    r = requests.get(url)

    if r.status_code == 401:
        raise RuntimeError("Invalid Slushpool token!")

    return r.json()
