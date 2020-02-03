#!/usr/bin/env bash

# this file surrounds the XML with a main root tag to stop python shouting at me

for sample in chords/*.xml; do
	echo -e "<root>\n$(cat $sample)\n</root>" > $sample
done
