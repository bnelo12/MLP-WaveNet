#!/usr/bin/env bash

sonic-annotator -s vamp:nnls-chroma:chordino:simplechord > chords.n3

for sample in data/*.wav; do
	sample=${sample##*/}
	sonic-annotator -t chords.n3 data/"$sample" -w default >> chords/"${sample%.*}".xml
done

