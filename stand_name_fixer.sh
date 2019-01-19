#!/bin/bash

# stand_name_fixer.sh
# Uses mkvtoolnix and another script to replace
# stand names in mkv files of JoJo's Bizzare Adventure

# Extract subtitles from mkv
echo $1
mkvextract tracks "$1" 2:"$1.srt"

# Fix subtitles
python3 stand_name_fixer.py "$1.srt"

# Remove subtitles from mkv
mkvmerge -o "tmp.mkv" --no-subtitles "$1"

# Insert subtitles into mkv
mkvmerge -o "out.mkv" "tmp.mkv" --language 0:eng "$1.srt" --default-track 0

# Cleanup
rm tmp.mkv "$1.mkv.srt"
mv out.mkv "$1"
