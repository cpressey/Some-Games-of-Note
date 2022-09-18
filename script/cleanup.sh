#!/bin/sh -x

ARTICLES=../The-Dossier/article

(cd $ARTICLES && feedmark --output-refdex --output-refdex-single-filename \
                          *\ of\ Note.md \
                          "Recollected Games.md" \
                          "Some Modern Retrogames.md" \
                          "Classic Computer Games.md" \
                          "Classic Text Adventures.md" \
                          "An Esolang Reading List.md" \
                 >../refdex.json) || exit 1

# non-lists
feedmark --input-refdex=refdex.json \
         "$ARTICLES/A Basic Theory of Video Games.md" \
         "$ARTICLES/Blurry Memories of DOS Programming.md" \
         "$ARTICLES/Perspective on Text Adventures.md" \
         "$ARTICLES/The Aesthetics of Esolangs.md" \
         "$ARTICLES/Retrospective on Language Design.md" \
         "$ARTICLES/Befunge Silver Jubilee Retrospective.md" \
         --rewrite-markdown || exit 1

#lists
feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Text\ adventure.md \
         $ARTICLES/Text\ Adventures\ of\ Note.md \
         $ARTICLES/Classic\ Text\ Adventures.md \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Book.md \
         "$ARTICLES/An Esolang Reading List.md" \
         --rewrite-markdown || exit 1

feedmark --input-refdex=refdex.json \
         --check-against-schema=schema/Video\ game.md \
         "$ARTICLES/Some Modern Retrogames.md" \
         "$ARTICLES/Commodore 64 Games of Note.md" \
         "$ARTICLES/Apple II Games of Note.md" \
         "$ARTICLES/Atari 2600 Games of Note.md" \
         "$ARTICLES/Computer Sports Games of Note.md" \
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
