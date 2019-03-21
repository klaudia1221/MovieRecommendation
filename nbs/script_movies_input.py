# Generates input for movies

import movies_utils as m
import os
import sys
from pathlib import Path
from tqdm import tqdm
import numpy as np
import pandas as pd

# after we donlowad a data we can 
# join them by movieId with tyoutube and remove empty values

#def get_cover_urls(mv):
#    return mv['movieId'].map(get_cover_url)
# to generate the input
def generate_input():
    dfm = pd.read_csv('../data/movies_alldata.csv')
    dfmid = pd.read_csv('../data/movies_id.csv')
    dfy = pd.read_csv('../data/ml-youtube.csv')
    
    df_c = pd.read_csv('../data/movies_category.csv')
    
    ratings = pd.read_csv('../data/movies_ratings.csv');
    movies_ratings = pd.DataFrame(ratings['movieId'].value_counts())
    movies_ratings['cnt'] = movies_ratings['movieId']
    movies_ratings['movieId'] = movies_ratings.index

    
    o = dfm.merge(dfy,on='movieId').merge(dfmid,on='movieId')
    o = o.merge(df_c[['movie_ix','category']],on='movie_ix')
    o = o.merge(movies_ratings,on='movieId')
    print(o[:5])
    
    o['genres'] = o['genres'].str.replace('|',',')
    o['length'] = o['length'].str.replace('[','').str.replace('\'','').str.replace(']','')
#     o['imdb_url'] = o['imdbId'].map(lambda x: 'http://www.imdb.com/title/tt0' + str(x) + '/');
    o['title'] = o['title_x']
    o[o['cover'].isnull()!=True][[
        'movieId','movie_ix','imdbId','tmdbId','genres','cover','title',
        'full-title','year','director','producer',
        'imdb_url',  'rating', 'category', 'cnt',
        'small-cover','plot','length','youtubeId']].sort_values(by='movie_ix').to_csv('../data/movie_input.csv',index=False)
    print('saved to ../data/movie_input.csv')
    print('this fields are not exported',)
    return o[o['cover'].isnull()]


generate_input()