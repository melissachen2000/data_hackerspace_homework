import requests
import re
import matplotlib.pyplot as plt


def lyrics_word_count_easy(artist, song, phrase):
    r = requests.get("https://api.lyrics.ovh/v1/" + artist + "/" + song)
    if (r.status_code != 200): return -1
    r = r.json()
    r = r["lyrics"]
    return len(re.findall("(?i)^$" + phrase, r)) #needs to include regex for substringing

print(lyrics_word_count_easy("Rick Astley", "Never Gonna Give You Up", "never"))
#on 50
#na 54

def lyrics_word_count(artist, phrase):
    pass

def visualize():
    pass
