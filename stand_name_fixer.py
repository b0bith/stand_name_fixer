#!/bin/python3

# stand_name_fixer.py
# Usage: python3 stand_name_fixer.py "SUBTITLE_FILE"

import sys

if len(sys.argv) is not 2:
    print('Usage: python3 stand_name_fixer.py "SUBTITLE_FILE"')
    sys.exit(0)

# Localization : Acutal name

part_4 = {
'Heart Father' : 'Atom Heart Father',
'Worse Company' : 'Bad Company',
'Boys Man Man' : 'Boy II Man',
'Cheap Trap' : 'Cheap Trick',  
'Fashionista' : 'Cinderella',
'Shining Diamond' : 'Crazy Diamond',
'Terra Ventus' : 'Earth Wind and Fire',
'Reverb' : 'Echoes',
'Highway Go Go' : 'Highway Star',
'Deadly Queen' : 'Killer Queen',
'Love Extra' : 'Love Deluxe',
'Poll Jam' : 'Pearl Jam',
'Chili Pepper' : 'Red Hot Chili Pepper',
'Show Off' : 'Surface'
}

stand_names = {
"Li'l Bomber" : "Aerosmith",
'Babyhead' : 'Baby Face',               # Unknown if Crunchyroll English localization
'Fisher Man' : 'Beach Boy',
'Shadow Sabbath' : 'Black Sabbath',
'Crush' : 'Clash',                      # Unknown if Crunchyroll English localization
'Reverb' : 'Echoes',
'Golden Wind' : 'Gold Experience',
'Thankful Death' : 'Greatful Dead',
'Green Tea' : 'Green Day',              # Unknown if Crunchyroll English localization
'Emperor Crimson' : 'King Crimson',     # Unknown if Crunchyroll English localization
'Arts & Crafts' : 'Kraft Work',
'Tiny Feet' : 'Little Feet',
'Mirror Man' : 'Man in the Mirror',
'Metallic' : 'Metallica',               # Unknown if Crunchyroll English localization
'Moody Jazz' : 'Moody Blues',
'Mr. President': 'Mr. President',       # Is there even an English localization?
'Notorious B.I.G': 'Notorious B.I.G',   # Unknown
'Sanctuary' : 'Oasis',                  # Unknown if Crunchyroll English localization
'Purple Smoke' : 'Purple Haze',
'Rolling Stones' : 'Rolling Stones',    # Unknown
'Six Bullets' : 'Sex Pistols',
'Tender Machine' : 'Soft Machine',
'Spicy Lady' : 'Spice Girl',            # Unknown if Crunchyroll English localization
'Zipper Man' : 'Sticky Fingers',
'Talking Head' : 'Talking Head',        # Unknown
'White Ice' : 'White Album'             # Unknown if Crunchyroll English localization
}

subtitle_file = sys.argv[1]
with open(subtitle_file, 'r') as infile:
    subs = infile.read()

for localization, original in stand_names.items():
    subs = subs.replace(localization, original)

with open(subtitle_file, 'w') as outfile:
    outfile.write(subs)
