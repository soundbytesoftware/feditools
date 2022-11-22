#!/usr/bin/env python


class Link:
    """
    See: https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link
    """

    @classmethod
    def from_data(cls, data):
        return cls(data["href"], href_lang=data.get("hreflang"), rel=data.get("rel"),
                   media_type=data.get("mediaType"), name=data.get("name"), id=data.get("id"),
                   width=data.get("width"), height=data.get("height"), preview=data.get("preview"))

    def __init__(self, href, href_lang=None, rel=None, media_type=None, name=None,
                 id=None, width=None, height=None, preview=None):
        self.href = href
        self.href_lang = href_lang
        self.rel = rel
        self.media_type = media_type
        self.name = name
        self.id = id
        self.width = width
        self.height = height
        self.preview = preview

    def __repr__(self):
        args = [repr(self.href)]
        if self.href_lang:
            args.append(f"href_lang={self.href_lang!r}")
        if self.rel:
            args.append(f"rel={self.rel!r}")
        if self.media_type:
            args.append(f"media_type={self.media_type!r}")
        if self.name:
            args.append(f"name={self.name!r}")
        if self.id:
            args.append(f"id={self.id!r}")
        if self.width:
            args.append(f"width={self.width!r}")
        if self.height:
            args.append(f"height={self.height!r}")
        if self.preview:
            args.append(f"preview={self.preview!r}")
        return f"{self.__class__.__name__}(%s)" % ", ".join(args)
