#!/usr/bin/env python


from json import dumps, loads

from urllib3 import PoolManager as HTTP, make_headers


def get_object(uri):
    http = HTTP()
    rs = http.request("GET", uri, headers={
        "Accept": 'application/ld+json; profile="https://www.w3.org/ns/activitystreams"',
        "Authorization": "Bearer v7BLhq8WrZgVem8Q7gkmmVZddvI4uVPIFtFqk5VP9Qc",
    })
    if rs.status != 200:
        raise OSError("Oops!")  # TODO
    data = rs.json()
    data_type = data["type"]
    if data_type == "Person":
        # TODO: this is rubbish
        return Person(data)
    else:
        raise ValueError(f"Unknown type {data_type!r}")


class Object:
    """
    See https://www.w3.org/TR/activitystreams-core/#object
    """

    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    @property
    def uri(self):
        return self.data["id"]


class Actor(Object):

    def post(self, activity):
        """
        https://www.w3.org/TR/activitypub/#client-to-server-interactions
        """
        http = HTTP()
        body = """\
{
    "@context": "https://www.w3.org/ns/activitystreams",
    "type": "Like",
    "object": "https://mastodonapp.uk/@Molly/109376403202293504"
}
        """
        uri = self["outbox"]
        print(uri)
        rs = http.request("POST", uri, body.encode("utf-8"), headers={"Content-Type": "application/ld+json",
                                                                      "Authorization": "Bearer v7BLhq8WrZgVem8Q7gkmmVZddvI4uVPIFtFqk5VP9Qc"})
        print(rs.status)
        print(rs.read())


class Person(Actor):

    pass


def main():
    # Client key: LnDHQS7mtCcKnLarUyDkoo4FRocC4SStwMAXIhHgH7E
    # Client secret: 4U_aE3t5Fsf5fMsZ1_wHOqyPHQWHssYIOh0EMmhCXto
    # Access token: v7BLhq8WrZgVem8Q7gkmmVZddvI4uVPIFtFqk5VP9Qc
    http = HTTP()
    rs = http.request("GET", "https://soundbyte.social/users/nigel",
                      headers={
                          "Accept": 'application/ld+json; profile="https://www.w3.org/ns/activitystreams"',
                          #"Authorization": "Bearer v7BLhq8WrZgVem8Q7gkmmVZddvI4uVPIFtFqk5VP9Qc",
                      })
    print(rs.status)
    print(dumps(loads(rs.data), indent="  "))


if __name__ == "__main__":
    main()
