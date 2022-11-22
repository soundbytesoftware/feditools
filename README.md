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
$ python -m feditools.nodeinfo soundbyte.social
# NodeInfo version 2.0
software: mastodon 4.0.1
protocols: activitypub
services:
  inbound:
  outbound:
open registrations: False
usage: {'users': {'total': 2, 'activeMonth': 2, 'activeHalfyear': 2},
  'localPosts': 102}
metadata:
```
