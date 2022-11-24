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

The `nodeinfo` command provides an entry point into the `feditools.nodeinfo` module.

```bash
$ nodeinfo soundbyte.social
{
  "version": "2.0",
  "software": {
    "name": "mastodon",
    "version": "4.0.1"
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
      "total": 2,
      "activeMonth": 2,
      "activeHalfyear": 2
    },
    "localPosts": 106
  },
  "metadata": {}
}
```

### WebFinger

The `webfinger` command provides an entry point into the `feditools.webfinger` module.

```bash
$ webfinger nigel@soundbyte.social
Subject: acct:nigel@soundbyte.social
Aliases: https://soundbyte.social/@nigel
         https://soundbyte.social/users/nigel
Links: https://soundbyte.social/@nigel (rel=http://webfinger.net/rel/profile-page)
       https://soundbyte.social/users/nigel (rel=self)
       https://soundbyte.social/authorize_interaction?uri={uri} (rel=http://ostatus.org/schema/1.0/subscribe)
```
