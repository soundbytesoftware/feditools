#!/usr/bin/env python

from argparse import ArgumentParser
from json import JSONDecodeError
from os import linesep
from textwrap import wrap

from urllib3 import PoolManager as HTTP

from feditools.activity.streams import Link


class NodeInfo:
    """
    See: https://github.com/jhass/nodeinfo/
    """

    @classmethod
    def _get_links(cls, host):
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

    @classmethod
    def get(cls, host):
        http = HTTP()
        for link in cls._get_links(host):
            # TODO: check link.rel to know how to parse the response
            rs = http.request("GET", link.href)
            try:
                info = rs.json()
            except JSONDecodeError:
                raise ValueError("Broken link in node info: %r" % link)
            else:
                yield cls(info["version"], info["software"], info["protocols"], info["services"],
                          info["openRegistrations"], info["usage"], info["metadata"])

    def __init__(self, version, software, protocols, services, open_registrations, usage, metadata):
        self.version = version
        """ The schema version, must be 1.0, 1.1, 2.0 or 2.1.
        """
        self.software = software
        """ Metadata about server software in use.
        """
        self.protocols = protocols
        """ The protocols supported on this server.
        """
        self.services = services
        """ The third party sites this server can connect to via their application API.
        """
        self.open_registrations = open_registrations
        """ Whether this server allows open self-registration.
        """
        self.usage = usage
        """ Usage statistics for this server.
        """
        self.metadata = metadata
        """ Free form key value pairs for software specific values. 
            Clients should not rely on any specific key being present.
        """

    def __repr__(self):
        return (f"{self.__class__.__name__}(version={self.version!r}, software={self.software!r}, "
                f"protocols={self.protocols!r}, services={self.services!r}, "
                f"open_registrations={self.open_registrations!r}, usage={self.usage!r}, metadata={self.metadata!r})")

    def __str__(self):
        lines = [
            f"# NodeInfo version {self.version}",
            f"software: {self.software['name']} {self.software['version']}",
        ]
        lines.extend(wrap("protocols: {}".format(", ".join(self.protocols)), subsequent_indent="  "))
        lines.append("services:")
        lines.extend(wrap("  inbound: {}".format(", ".join(self.services["inbound"])), subsequent_indent="    "))
        lines.extend(wrap("  outbound: {}".format(", ".join(self.services["outbound"])), subsequent_indent="    "))
        lines.append(f"open registrations: {self.open_registrations}")
        lines.extend(wrap(f"usage: {self.usage}", subsequent_indent="  "))
        lines.append("metadata:")
        lines.extend(wrap("  {}".format(", ".join(f"{key}={value}" for key, value in self.metadata.items())),
                          subsequent_indent="    ", break_on_hyphens=False))
        return linesep.join(lines)


def main():
    parser = ArgumentParser()
    parser.add_argument("host")
    args = parser.parse_args()
    try:
        for info in NodeInfo.get(args.host):
            print(info)
    except ValueError as e:
        print(f"{e}")
        exit(1)


if __name__ == "__main__":
    main()
