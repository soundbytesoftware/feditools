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

### Lookup an ActivityPub-compatible actor

```bash
$ python -m feditools.actor soundbyte.social | jq
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "toot": "http://joinmastodon.org/ns#",
      "featured": {
        "@id": "toot:featured",
        "@type": "@id"
      },
      "featuredTags": {
        "@id": "toot:featuredTags",
        "@type": "@id"
      },
      "alsoKnownAs": {
        "@id": "as:alsoKnownAs",
        "@type": "@id"
      },
      "movedTo": {
        "@id": "as:movedTo",
        "@type": "@id"
      },
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value",
      "discoverable": "toot:discoverable",
      "Device": "toot:Device",
      "Ed25519Signature": "toot:Ed25519Signature",
      "Ed25519Key": "toot:Ed25519Key",
      "Curve25519Key": "toot:Curve25519Key",
      "EncryptedMessage": "toot:EncryptedMessage",
      "publicKeyBase64": "toot:publicKeyBase64",
      "deviceId": "toot:deviceId",
      "claim": {
        "@type": "@id",
        "@id": "toot:claim"
      },
      "fingerprintKey": {
        "@type": "@id",
        "@id": "toot:fingerprintKey"
      },
      "identityKey": {
        "@type": "@id",
        "@id": "toot:identityKey"
      },
      "devices": {
        "@type": "@id",
        "@id": "toot:devices"
      },
      "messageFranking": "toot:messageFranking",
      "messageType": "toot:messageType",
      "cipherText": "toot:cipherText",
      "suspended": "toot:suspended"
    }
  ],
  "id": "https://soundbyte.social/actor",
  "type": "Application",
  "inbox": "https://soundbyte.social/actor/inbox",
  "outbox": "https://soundbyte.social/actor/outbox",
  "preferredUsername": "soundbyte.social",
  "url": "https://soundbyte.social/about/more?instance_actor=true",
  "manuallyApprovesFollowers": true,
  "publicKey": {
    "id": "https://soundbyte.social/actor#main-key",
    "owner": "https://soundbyte.social/actor",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuiGT1M4A+5zZZvr1nCYP\nPlhTEd6OeFm/YCDSEt/J5p7g9FU/V+UnjrntM8Rr9s7P751ElMXQUoyObQKMcPFY\nG3lOlGXv5NxgbK2Riw1eMnUcrSwxZ0rrPGfrWJsSPbFb7ANwWwnmW8BYjmCHc/dG\nXkIa9zixFaBDZIH/kcNsrSRdjjC4otRJG2wfcqzKeSv2RaHfVPeXdsWWBbHuPTU4\nhXSymWMWPF3yzmrW5a/2K+AhYvEWqNJZJewW4OUx6cnhreUmuv3rKc/QrnxfozFM\nOgtHVC0CfBul31MwExo+LByo28C+DTULIhP53xn3gkxhnPr5ZBSBHOhW7iiywi3H\nxQIDAQAB\n-----END PUBLIC KEY-----\n"
  },
  "endpoints": {
    "sharedInbox": "https://soundbyte.social/inbox"
  }
}
```