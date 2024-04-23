import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

url = "https://itunes.apple.com/search?entity=song&limit=10&term="

req = requests.get(url + sys.argv[1])

data = req.json()

for song in data["results"]:
    print(song["trackName"])
