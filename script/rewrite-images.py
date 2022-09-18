#!/usr/bin/env python3

# Invoke like the following, rewrites the file in-place:
# PYTHONPATH=../Feedmark/src ./script/rewrite-images.py article/Some\ Modern\ Retrogames.md

from argparse import ArgumentParser
import json
import sys
try:
    from urllib import unquote, quote_plus
except ImportError:
    from urllib.parse import unquote, quote_plus
assert unquote and quote_plus

from feedmark.checkers import Schema
from feedmark.loader import read_document_from
from feedmark.formats.markdown import feedmark_markdownize


def url_to_dirname_and_filename(url):
    """Lifted from yastasoti: https://catseye.tc/node/yastasoti """
    parts = url.split(u'/')
    parts = parts[2:]
    domain_name = parts[0]
    domain_name = quote_plus(domain_name)
    parts = parts[1:]
    filename = u'/'.join(parts)
    filename = quote_plus(filename.encode('utf-8'))
    if not filename:
        filename = 'index.html'
    return (domain_name, filename)


def main(args):
    argparser = ArgumentParser()

    argparser.add_argument('docs', nargs='+', metavar='FILENAME', type=str)

    options = argparser.parse_args(args)

    for filename in options.docs:
        document = read_document_from(filename)

        schema = None
        schema_name = document.properties.get('schema')
        if schema_name:
            schema_filename = "schema/{}.md".format(schema_name)
            schema_document = read_document_from(schema_filename)
            schema = Schema(schema_document)
            results = schema.check_documents([document])
            if results:
                sys.stdout.write(json.dumps(results, indent=4, sort_keys=True))
                sys.exit(1)
        else:
            continue
        for section in document.sections:
            new_images = []
            for alt_text, url in section.images:
                if url.startswith(('http://catseye.tc', 'https://catseye.tc', 'http://static.catseye.tc', 'https://static.catseye.tc',)):
                    rewritten_url = url
                else:
                    dirname, filename = url_to_dirname_and_filename(url)
                    rewritten_url = 'https://static.catseye.tc/archive/{}/{}'.format(dirname, quote_plus(filename))
                new_images.append((alt_text, rewritten_url))
            section.images = new_images
        s = feedmark_markdownize(document, schema=schema)
        with open(document.filename, 'w') as f:
            f.write(s)


if __name__ == '__main__':
    main(sys.argv[1:])
