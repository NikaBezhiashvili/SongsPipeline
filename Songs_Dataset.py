import pandas as pd
import requests as req
import urllib.request
import os


datasetUrl = 'http://millionsongdataset.com/sites/default/files/AdditionalFiles/unique_artists.txt'
file_name = 'songsData'

try:
    os.remove(file_name)
    urllib.request.urlretrieve(datasetUrl, file_name)
except:    
    urllib.request.urlretrieve(datasetUrl, file_name)


dataSet = pd.read_csv(file_name, sep='<SEP>', header=None, names=['artist_id', 'serial_id', 'song', 'title'], engine='python')

