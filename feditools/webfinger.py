#!/usr/bin/env python

"""
This is an implementation of RFC 7033, which defines
the WebFinger protocol. For the full specification,
see https://datatracker.ietf.org/doc/html/rfc7033.

The acct URI scheme:
https://datatracker.ietf.org/doc/html/rfc7565

RFC 6415: resource descriptors
"""

from argparse import ArgumentParser
from json import JSONDecodeError
from os import linesep

from urllib3 import PoolManager as HTTP

from feditools.weblinking import Link


class ResourceDescriptor:
    """ RFC 6415
    """

    @classmethod
    def from_json(cls, data):
        return cls(data["subject"], data.get("aliases"), data.get("properties"), data.get("links"))

    def __init__(self, subject, aliases, properties, links):
        self.subject = subject
        self.aliases = aliases
        self.properties = properties
        self.links = [Link(self.subject, **link) for link in links]

    def __str__(self):
        lines = [f"Subject: {self.subject}"]
        if self.aliases:
            for i, alias in enumerate(self.aliases):
                if i == 0:
                    lines.append(f"Aliases: {alias}")
                else:
                    lines.append(f"         {alias}")
        if self.properties:
            for i, (name, value) in enumerate(self.properties.items()):
                if i == 0:
                    lines.append(f"Properties: {name} = {value!r}")
                else:
                    lines.append(f"            {name} = {value!r}")
        if self.links:
            for i, link in enumerate(self.links):
                if i == 0:
                    lines.append(f"Links: {link.href or link['template'] or ''} (rel={link.rel})")
                else:
                    lines.append(f"       {link.href or link['template'] or ''} (rel={link.rel})")
        return linesep.join(lines)


def _parse_url(url):
    from urllib.parse import urlsplit
    # TODO: improve this and move it to a URI module
    # See: https://datatracker.ietf.org/doc/html/rfc7565 (The 'acct' URI Scheme)
    parsed = urlsplit(url)
    if parsed.scheme == "acct":
        return parsed.scheme, parsed.path
    else:
        return parsed.scheme, parsed


def webfinger(resource, host=None, *rels):
    scheme, ssp = _parse_url(resource)
    if not scheme:
        # If no scheme is provided, assume "acct:" by default
        resource = f"acct:{resource}"
        scheme, ssp = _parse_url(resource)
    if not host:
        # No explicit host provided, need to derive one
        if scheme == "acct":
            _, _, host = ssp.partition("@")
        else:
            host = ssp.hostname
    url = f"https://{host or 'localhost'}/.well-known/webfinger"
    http = HTTP()
    fields = [("resource", resource)] + [("rel", rel) for rel in rels]
    rs = http.request("GET", url, fields=fields)
    if rs.status == 200:
        try:
            data = rs.json()
        except JSONDecodeError:
            raise
        else:
            return ResourceDescriptor.from_json(data)
    else:
        # TODO: better error handling
        raise OSError(rs.status)


def main():
    parser = ArgumentParser()
    parser.add_argument("-H", "--host")
    parser.add_argument("account")
    args = parser.parse_args()
    print(webfinger(args.account, host=args.host))


if __name__ == "__main__":
    main()
