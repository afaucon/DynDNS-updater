import argparse

import dyndns_updater
from dyndns_updater.api import duckdns_update


def duckdns_cli():
    parser = argparse.ArgumentParser(prog=dyndns_updater.__info__.__package_name__, 
                                     description=dyndns_updater.__info__.__description__)

    parser.add_argument('command', choices=['update'])
    parser.add_argument('domain')
    parser.add_argument('token')

    args = parser.parse_args()

    if args.command == 'update':
        
        ipv4, hasChanged = duckdns_update(args.domain, args.token)
        print(ipv4)
        print('Updated' if hasChanged else 'No change')

if __name__ == "__main__":
    pass
