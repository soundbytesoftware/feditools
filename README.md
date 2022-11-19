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

### Get node info

```bash
$ python -m feditools.nodeinfo soundbyte.social | jq
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
  "usage": {
    "users": {
      "total": 2,
      "activeMonth": 2,
      "activeHalfyear": 2
    },
    "localPosts": 97
  },
  "openRegistrations": false,
  "metadata": {}
}
```
