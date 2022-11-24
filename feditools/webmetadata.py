#!/usr/bin/env python


"""
This is an implementation of RFC 6415, describes
a method for locating host metadata as well as
information about individual resources controlled
by the host. For the full specification, see
https://datatracker.ietf.org/doc/html/rfc6415.
"""


from os import linesep

from feditools.weblinking import Link


class ResourceDescriptor:
    """
    """

    @classmethod
    def from_json(cls, data):
        return cls(data.get("subject"), data.get("aliases"), data.get("properties"), data.get("links"))

    def __init__(self, subject, aliases, properties, links):
        self.subject = subject
        self.aliases = aliases
        self.properties = properties
        self.links = [Link(self.subject, **link) for link in links]

    def __str__(self):
        lines = []
        if self.subject:
            lines.append(f"Subject: {self.subject}")
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


JRD = ResourceDescriptor.from_json
