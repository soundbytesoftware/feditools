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
