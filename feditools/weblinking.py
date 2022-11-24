#!/usr/bin/env python

"""
RFC5988

See https://datatracker.ietf.org/doc/html/rfc5988
"""


class Link:
    """ A link can be viewed as a statement of the form "{context IRI} has a
    {relation type} resource at {target IRI}, which has {target
    attributes}".
    """

    def __init__(self, context, rel, href=None, **attributes):
        self.context = context
        self.rel = rel
        self.href = href
        self._attributes = attributes
        # type
        # titles
        # properties

    def __getitem__(self, key):
        return self._attributes[key]

    def __setitem__(self, key, value):
        self._attributes[key] = value
