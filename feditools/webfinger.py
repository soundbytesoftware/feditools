#!/usr/bin/env python

"""
This is an implementation of RFC 7033, which defines
the WebFinger protocol. For the full specification,
see https://datatracker.ietf.org/doc/html/rfc7033.
"""

from argparse import ArgumentParser
from json import JSONDecodeError

from urllib3 import PoolManager as HTTP

from feditools.webmetadata import JRD


def _parse_url(url):
    # The acct URI scheme:
    # https://datatracker.ietf.org/doc/html/rfc7565
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
            return JRD(data)
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
