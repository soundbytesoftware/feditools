#!/usr/bin/env python

"""
This module provides an implementation of the NodeInfo
protocol, as described at https://github.com/jhass/nodeinfo/.
"""

from argparse import ArgumentParser
from json import JSONDecodeError, dumps

from urllib3 import PoolManager as HTTP, Timeout
from urllib3.exceptions import RequestError

from feditools.webmetadata import JRD


class NodeInfo:
    """
    """

    @classmethod
    def discover(cls, host, timeout=None):
        # returns a JRD document containing the links to the node info itself
        # https://github.com/jhass/nodeinfo/blob/main/PROTOCOL.md
        http = HTTP(timeout=Timeout(timeout))
        try:
            rs = http.request("GET", f"https://{host}/.well-known/nodeinfo")
        except RequestError as error:
            raise NodeInfoError("Failed to discover node info endpoints") from error
        else:
            try:
                data = rs.json()
            except JSONDecodeError as error:
                raise NodeInfoError("Host does not export a well-known node info API") from error
            else:
                return JRD(data)

    @classmethod
    def get(cls, host, timeout=None):
        discovered = cls.discover(host, timeout=timeout)
        links = {}
        for link in discovered.links:
            links[link.rel] = link.href
        if not links:
            raise ValueError("No links in node info")
        links = {rel: href for rel, href in links.items()
                 if rel.startswith("http://nodeinfo.diaspora.software/ns/schema/")}
        href = sorted(links, reverse=True)[0]  # get the first one when listed backwards
        http = HTTP(timeout=Timeout(timeout))
        try:
            rs = http.request("GET", links[href])
        except RequestError as error:
            raise NodeInfoError("Failed to get node info") from error
        else:
            try:
                info = rs.json()
            except JSONDecodeError as error:
                raise NodeInfoError("Broken link in node info: %r" % links[href]) from error
            else:
                return cls(info)

    def __init__(self, info):
        self.info = info

    def __repr__(self):
        return f"{self.__class__.__name__}({self.info!r})"

    def __iter__(self):
        return iter(self.info.items())

    @property
    def version(self):
        """ The schema version, must be 1.0, 1.1, 2.0 or 2.1.
        """
        return self.info.get("version")

    @property
    def software(self):
        """ Metadata about server software in use.
        """
        return self.info.get("software")

    @property
    def protocols(self):
        """ The protocols supported on this server.
        """
        return self.info.get("protocols")

    @property
    def services(self):
        """ The third party sites this server can connect to via their application API.
        """
        return self.info.get("services")

    @property
    def open_registrations(self):
        """ Whether this server allows open self-registration.
        """
        return self.info.get("openRegistrations")

    @property
    def usage(self):
        """ Usage statistics for this server.
        """
        return self.info.get("usage")

    @property
    def metadata(self):
        """ Free form key value pairs for software specific values.
            Clients should not rely on any specific key being present.
        """
        return self.info.get("metadata")

    @property
    def users_total(self):
        try:
            return self.usage["users"]["total"]
        except (KeyError, TypeError):
            return None

    @property
    def local_posts(self):
        try:
            return self.usage["localPosts"]
        except (KeyError, TypeError):
            return None


class NodeInfoError(Exception):
    # TODO: split into sub-errors, e.g. can't resolve, can't connect, timeout, etc

    pass


def main():
    parser = ArgumentParser()
    parser.add_argument("-p", "--pretty", action="store_true")
    parser.add_argument("host")
    args = parser.parse_args()
    try:
        info = NodeInfo.get(args.host)
        print(dumps(dict(iter(info)), indent=("  " if args.pretty else None)))
    except NodeInfoError as error:
        print(f"{error}\n{error.__cause__}")
        exit(1)


if __name__ == "__main__":
    main()
