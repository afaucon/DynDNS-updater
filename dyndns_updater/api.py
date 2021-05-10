import dyndns_updater.exceptions
import requests


def duckdns_update(domain, token):
    # https://www.duckdns.org/spec.jsp
    url = 'https://duckdns.org/update/{}/{}'.format(domain, token)
    url = 'https://duckdns.org/update?domains={}&token={}&verbose=true'.format(domain, token)
    r = requests.get(url)
    # print(type(r))
    # print(r)
    # print(r.__dict__)
    # print(r.status_code)
    # print(r.headers)
    # print(r.encoding)
    # print(r.text)
    _, ipv4, _, change = r.text.split('\n')

    return ipv4, change=='UPDATED'
