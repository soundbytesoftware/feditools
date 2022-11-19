#!/usr/bin/env python


from argparse import ArgumentParser
from json import dumps

from urllib3 import PoolManager as HTTP


def get_actor(host):
    http = HTTP()
    rs = http.request("GET", f"https://{host}/actor")
    return rs.json()


def main():
    parser = ArgumentParser()
    parser.add_argument("host")
    args = parser.parse_args()
    print(dumps(get_actor(args.host)))


if __name__ == "__main__":
    main()
