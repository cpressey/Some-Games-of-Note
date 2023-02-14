#!/bin/sh -x

ARTICLES=./article

(cd $ARTICLES && feedmark --output-refdex --output-refdex-single-filename \
                          *.md \
                 >../refdex.json) || exit 1

#lists
feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Text\ adventure.md \
         "$ARTICLES/Text Adventures of Note.md" \
         "$ARTICLES/Classic Text Adventures.md" \
         "$ARTICLES/Point-and-Click Adventures of Note.md" \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Video\ game.md \
         "$ARTICLES/8-bit Home Computer Games of Note.md" \
         "$ARTICLES/Some Modern Retrogames.md" \
         "$ARTICLES/Commodore 64 Games of Note.md" \
         "$ARTICLES/Apple II Games of Note.md" \
         "$ARTICLES/Arcade Games of Note.md" \
         "$ARTICLES/Classic Arcade Games.md" \
         "$ARTICLES/Atari 2600 Games of Note.md" \
         "$ARTICLES/British TV-Derived Games of Note.md" \
         "$ARTICLES/Sports Video Games of Note.md" \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Computer\ game.md \
         "$ARTICLES/Classic Computer Games.md" \
         "$ARTICLES/Computer Games of Note.md" \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Lost\ game.md \
         "$ARTICLES/Lost Games.md" \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         "$ARTICLES/Recollected Games.md" \
         --rewrite-markdown || exit 1

# Not done:
# - Role-Playing Games of Note
