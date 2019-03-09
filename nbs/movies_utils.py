import os
import sys
from pathlib import Path
from tqdm import tqdm
import numpy as np
import pandas as pd

path = Path('./data') # data are not in the github folder
small_path = path/'movies_small'
latest_path = path/'movies_latest'

small_url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
latest_url = 'http://files.grouplens.org/datasets/movielens/ml-latest.zip'

small_ratings = small_path/'ratings.csv'
small_movies = small_path/'movies.csv'

latest_ratings = latest_path/'ratings.csv'
latest_movies = small_path/'movies.csv'

def _prepare_path():
    Path(path).mkdir(exist_ok=True)
    Path(small_path).mkdir(exist_ok=True)
    Path(latest_path).mkdir(exist_ok=True)
_prepare_path(); # prepare pathes for python 

def _move_subfiles(path):
    import os, shutil, glob
    # move all files to main folder
    for d in  os.listdir(path):
        if os.path.isdir(path/d):
            path_str = os.path.join(str(path/d),'**','*')
            print(path_str)
            for file in glob.iglob(path_str, recursive=True):
                shutil.copy(file, small_path)
                print(file)
    
def _downlad_unzip(path,url):
    import requests
    import zipfile
    
    file_size = int(requests.head(url).headers["Content-Length"])
    req = requests.get(url,  stream=True)

    pbar = tqdm(
        total=file_size, initial=0,
        unit='B', unit_scale=True, desc=url.split('/')[-1])
    
    file = (path/'data.zip')
    with( open(file,'wb')) as f:
        for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
    pbar.close()            
    with zipfile.ZipFile(file,"r") as zip_ref:
        zip_ref.extractall(path)
    _move_subfiles(path)

    
# Download all ratings from the webpage
# source: movie1k-lens
def small_download():
    _downlad_unzip(small_path,small_url)
    return small_path

def latest_download():
    _downlad_unzip(latest_path,latest_url)
    return latest_path


def get_movies(path_data):
    m = pd.read_csv(path_data/'movies.csv')
    l = pd.read_csv(path_data/'links.csv')
    df = m.merge(l)
    df['cover'] = ''
    return df

from imdb import IMDb
ia = IMDb()
n = 0

def get_cover_url(imdbId):  
    global n
    movie = ''
    try:
        movie = ia.get_movie(str(imdbId))
        #print(str(n) + '. ' + str(movie))
        n += 1
        return movie['full-size cover url']
    except Exception as e:
        print(str(imdbId) + ': ' + str(movie) + ": " + str(e))
        return ''

#def get_cover_urls(mv):
#    return mv['movieId'].map(get_cover_url)

def img_show(url):
    import matplotlib.pyplot as plt 
    from PIL import Image
    from urllib.request import urlopen
    plt.imshow(Image.open(urlopen(url)))
