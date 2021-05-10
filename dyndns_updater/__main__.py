import argparse

import dyndns_updater
from dyndns_updater.api import duckdns_update

import logging
from pushbullet import PushBullet


def main_cli():
    parser = argparse.ArgumentParser(prog=dyndns_updater.__info__.__package_name__,
                                     description=dyndns_updater.__info__.__description__)

    parser.add_argument('--platform', action='store', required=True)
    parser.add_argument('command', choices=['update'])
    parser.add_argument('domain')
    parser.add_argument('token')
    parser.add_argument('--pushbullettoken', action='store', help='Access token to have full access to a Pushbullet account.')

    args = parser.parse_args()
    if args.command == 'update':

        if args.platform == 'duckdns':
            ipv4, hasChanged = duckdns_update(args.domain, args.token)

            if hasChanged:
                info_message = 'Current configured IP has changed. Verify the DNS at http://{}.duckdns.org/ ({})'.format(args.domain, ipv4)
                logging.info(info_message)
                if args.pushbullettoken is not None:
                    PushBullet(args.pushbullettoken).push_note('DNS IP changed', info_message)
            else:
                info_message = 'Current configured IP hasn\'t changed. Verify the DNS at http://{}.duckdns.org/ ({})'.format(args.domain, ipv4)
                logging.info(info_message)

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    main_cli()
