#!/usr/bin/env python3


import json
import os
import re
import subprocess
import sys
from urllib.parse import quote as url_quote


def generate_toc_line(document):
    title = document['title']
    filename = url_quote(document['filename'])
    sections = document.get('sections', [])
    properties = document.get('properties', {})

    signs = []
    section_count = len(sections)
    signs.append('({})'.format(section_count))

    if properties.get('status') == 'under construction':
        signs.append('*(U)*')

    return '*   [{}]({}) {}\n'.format(title, filename, ' '.join(signs))


def output_toc(heading, filenames):
    sys.stdout.write('{}\n\n'.format(heading))
    filenames = ['article/' + filename for filename in filenames]
    data = json.loads(subprocess.check_output(["feedmark", "--output-json"] + filenames))
    for document in data['documents']:
        line = generate_toc_line(document)
        sys.stdout.write(line)
    sys.stdout.write('\n')


if __name__ == '__main__':
    output_toc('#### Games of Note', [
        "Arcade Games of Note.md",
        "8-bit Home Computer Games of Note.md",
        "Commodore 64 Games of Note.md",
        "Apple II Games of Note.md",
        "Atari 2600 Games of Note.md",
        "British TV-Derived Games of Note.md",
        "Computer Sports Games of Note.md",
        "Computer Games of Note.md",
        "Role-Playing Games of Note.md",
        "Text Adventures of Note.md",
        "Classic Computer Games.md",
        "Classic Text Adventures.md",
        "Lost Games.md",
        "Recollected Games.md",
        "Some Modern Retrogames.md",
    ])
