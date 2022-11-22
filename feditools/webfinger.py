#!/usr/bin/env python

from argparse import ArgumentParser
from json import JSONDecodeError, dumps

from urllib3 import PoolManager as HTTP


class WebFinger:
    """
    See: https://www.rfc-editor.org/rfc/rfc7033
    """

    @classmethod
    def get(cls, host, resource):
        http = HTTP()
        rs = http.request("GET", f"https://{host}/.well-known/webfinger?resource={resource}")
        try:
            data = rs.json()
        except JSONDecodeError:
            raise ValueError("Host does not export a well-known webfinger API")
        else:
            return cls(data["subject"], data.get("aliases"), data.get("properties"), data.get("links"))

    @classmethod
    def get_account(cls, host, account):
        if "@" in account:
            resource = f"acct:{account}"
        else:
            resource = f"acct:{account}@{host}"
        return cls.get(host, resource)

    def __init__(self, subject, aliases, properties, links):
        self.subject = subject
        self.aliases = aliases
        self.properties = properties
        self.links = links

    def __repr__(self):
        return (f"{self.__class__.__name__}(subject={self.subject!r}, aliases={self.aliases!r}, "
                f"properties={self.properties!r}, links={self.links!r})")

    def __str__(self):
        return dumps(dict(iter(self)), indent="  ")

    def __iter__(self):
        yield "subject", self.subject
        if self.aliases:
            yield "aliases", self.aliases
        if self.properties:
            yield "properties", self.properties
        if self.links:
            yield "links", self.links


def main():
    parser = ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("account")
    args = parser.parse_args()
    try:
        print(WebFinger.get_account(args.host, args.account))
    except ValueError as e:
        print(f"{e}")
        exit(1)


if __name__ == "__main__":
    main()
