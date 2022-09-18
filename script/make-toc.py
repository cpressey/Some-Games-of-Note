#!/usr/bin/env python


import json
import os
import re
import subprocess
import sys
import urllib


def generate_toc_line(document):
    title = document['title']
    filename = urllib.quote(document['filename'])
    sections = document.get('sections', [])
    properties = document.get('properties', {})

    signs = []
    section_count = len(sections)
    if title not in (
        "Retrospective on Language Design",
        "Programming Languages as an Artistic Medium",
        "The Aesthetics of Esolangs",
        "A Basic Theory of Video Games",
        "Perspective on Text Adventures",
        "Blurry Memories of DOS Programming",
        "Befunge Silver Jubilee Retrospective",
        "Some Notes on Drawing",
        "Some Notes on Proving Programs Correct",
    ):
        signs.append('({})'.format(section_count))

    if properties.get('status') == 'under construction':
        signs.append('*(U)*')

    if properties.get('publication-date'):
        pubdate = properties['publication-date']
        match = re.search(r'(\w+\s+\d\d\d\d)', pubdate)
        if match:
            pubdate = match.group(1)
        signs.append('({})'.format(pubdate))

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
    output_toc('### Programming Languages and Programming', [
        "Retrospective on Language Design.md",
        "Programming Languages as an Artistic Medium.md",
        "The Aesthetics of Esolangs.md",
        "An Esolang Reading List.md",
        "Some Production Programming Languages.md",
        "Blurry Memories of DOS Programming.md",
        "Befunge Silver Jubilee Retrospective.md",
        "Some Notes on Proving Programs Correct.md",
    ])
    output_toc('### Games', [
        "A Basic Theory of Video Games.md",
        "Perspective on Text Adventures.md",
    ])
    output_toc('#### Games of Note', [
        "Video Games of Note.md",
        "Commodore 64 Games of Note.md",
        "Apple II Games of Note.md",
        "Atari 2600 Games of Note.md",
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
    output_toc('### Art', [
        "20th-Century Visual Artists of Note.md",
        "Some Notes on Drawing.md",
    ])
