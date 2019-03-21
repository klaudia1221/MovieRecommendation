import os
import sys
from pathlib import Path
from tqdm import tqdm
import numpy as np
import pandas as pd

path = Path('../../moviebook_data') # data are not in the github folder
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

def _try_get_value(m,val):
    try:
        return m[val]
    except Exception as e:
        print("[E] " + str(m) + ": " + str(e)[:20])
        return '' 

def _try_get_url(m):
    try:
        return ia.get_imdbURL(m)
    except Exception as e:
        print("[E] " + str(m) + ": " + str(e)[:20])
        return '' 
        
    
def _try_get_name(m,val):
    try:
        d =  m[val]
        return m[val][0]['name']
    except Exception as e:
        print("[E] " + str(m) + ": " + str(e)[:20])
        return ''     
 
def get_cover_url(imdbId):  
    global n
    movie = ''
    try:
        movie = ia.get_movie(str(imdbId))
        #print(str(n) + '. ' + str(movie))
        n += 1
        return movie['full-size cover url']
    except Exception as e:
        print(str(imdbId) + ': ' + str(movie) + ": " + str(e)[:20])
        return ''
    
def set_movie_info(df):
    #df['full-title'] = df['title']
    #print(df)
    for index,row in tqdm(df.iterrows(),total=len(df)):
        try:
            movie = ia.get_movie(str(df.loc[index,'imdbId']))
            df.loc[index,'full-title'] = _try_get_value(movie,'long imdb title')    
            df.loc[index,'title'] = _try_get_value(movie,'title')
            df.loc[index,'year'] = (_try_get_value(movie,'year'))
            df.loc[index,'director'] = str(_try_get_name(movie,'director'))
            df.loc[index,'producer'] = str(_try_get_name(movie,'production companies'))
            df.loc[index,'cover'] = _try_get_value(movie,'full-size cover url')
            df.loc[index,'small-cover'] = _try_get_value(movie,'cover url')
            df.loc[index,'plot'] = str(_try_get_value(movie,'plot outline'))
            df.loc[index,'length'] = str(_try_get_value(movie,'runtimes'))
            df.loc[index,'rating'] = str(_try_get_value(movie,'rating'))
            df.loc[index,'imdb_url'] = str(_try_get_url(movie))
            
            df.to_csv('temp_movies.csv')
        except Exception as e:
            print(str(index) + ': ' + str(movie) + ": " + str(e)[:20])
    return df     

def set_movie_rating(df):
    for index,row in tqdm(df.iterrows(),total=len(df)):
        try:
            movie = ia.get_movie(str(df.loc[index,'imdbId']))
            df.loc[index,'rating'] = str(_try_get_value(movie,'rating'))
            df.to_csv('temp_movies.csv')
        except Exception as e:
            print(str(index) + ': ' + str(movie) + ": " + str(e)[:20])
    return df      
    

def img_show(url):
    import matplotlib.pyplot as plt 
    from PIL import Image
    from urllib.request import urlopen
    plt.imshow(Image.open(urlopen(url)))

