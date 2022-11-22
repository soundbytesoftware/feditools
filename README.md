# feditools

Python tools for the Fediverse.


## Installation

### Install the latest stable version
No stable versions are yet available.

### Install the latest experimental version
```bash
$ pip install --pre feditools
```


## Usage

### NodeInfo

```bash
$ python -m feditools.nodeinfo mastodon.social
{
  "version": "2.0",
  "software": {
    "name": "mastodon",
    "version": "4.0.2"
  },
  "protocols": [
    "activitypub"
  ],
  "services": {
    "outbound": [],
    "inbound": []
  },
  "openRegistrations": false,
  "usage": {
    "users": {
      "total": 879403,
      "activeMonth": 245520,
      "activeHalfyear": 422601
    },
    "localPosts": 42641202
  },
  "metadata": {}
}
```

### WebFinger

```bash
$ python -m feditools.webfinger soundbyte.social nigel
{
  "subject": "acct:nigel@soundbyte.social",
  "aliases": [
    "https://soundbyte.social/@nigel",
    "https://soundbyte.social/users/nigel"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://soundbyte.social/@nigel"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://soundbyte.social/users/nigel"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://soundbyte.social/authorize_interaction?uri={uri}"
    }
  ]
}
```