#!/usr/bin/env python


from argparse import ArgumentParser
from json import JSONDecodeError, dumps

from urllib3 import PoolManager as HTTP

from feditools.streams import Link


def get_node_info_links(host):
    # returns the links to the node info itself
    # https://github.com/jhass/nodeinfo/blob/main/PROTOCOL.md
    http = HTTP()
    rs = http.request("GET", f"https://{host}/.well-known/nodeinfo")
    try:
        data = rs.json()
    except JSONDecodeError:
        raise ValueError("Host does not export a well-known node info API")
    else:
        return [Link.from_data(link_data) for link_data in data["links"]]


def get_node_info(host):
    http = HTTP()
    for link in get_node_info_links(host):
        rs = http.request("GET", link.href)
        try:
            yield rs.json()
        except JSONDecodeError:
            raise ValueError("Broken link in node info: %r" % link)


def main():
    parser = ArgumentParser()
    parser.add_argument("host")
    args = parser.parse_args()
    try:
        for info in get_node_info(args.host):
            # TODO: check rel to know how to parse the response
            print(dumps(info))
    except ValueError as e:
        print(f"{e}")
        exit(1)


if __name__ == "__main__":
    main()
