import requests
from bs4 import BeautifulSoup
import os
import re

GeniusAPIToken = '3Tu3IPR0NJMYMH0_UnBx5m7sFD_Uuj8bGrATCdTAvEa6Zcia6fVjEOGKeEi2-D9K'

def getArtistObj (artist: str, pageNum: int): 
  headers = {'Authorization': 'Bearer ' + GeniusAPIToken}
  search = 'https://api.genius.com/search?per_page=10&page=' + str(pageNum) 
  data = {'q': artist}
  return requests.get(search, data=data, headers=headers)


def songURL (artist: str, numSongs: int):
  pageNum = 1
  songURL = list()

  while True:
    response = getArtistObj(artist, pageNum)
    json = response.json()

    for hit in json['response']['hits']:
      if artist.lower() in hit['result']['primary_artist']['name'].lower():
        if (len(songURL) < numSongs):
          url = hit['result']['url']
          songURL.append(url)
      
    if (len(songURL) >= numSongs):
      break
    else:
      pageNum += 1
        
  print('Found {} songs by {}'.format(len(songURL), artist))
  return songURL 

def main():
  songURL('Queen', 250)

if __name__ == "__main__":
  main()