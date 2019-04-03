# Generates input for books

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
    dfm = pd.read_csv('./books/books.csv')
    dfmid = pd.read_csv('../data/books_id.csv')
    #dfy = pd.read_csv('../data/ml-youtube.csv')
    
    #df_c = pd.read_csv('../data/movies_category.csv')
    
    #ratings = pd.read_csv('../../moviebook_data/books/ratings.csv');
    #books_ratings = pd.DataFrame(ratings['book_id'].value_counts())
    #books_ratings['cnt'] = books_ratings['book_id']
    #books_ratings['book_id'] = movies_ratings.index

    
    o = dfm.merge(dfmid,on='book_id')
    #o = o.merge(df_c[['movie_ix','category']],on='movie_ix')
    #o = o.merge(movies_ratings,on='movieId')
    #print(o[:5])
    
    #o['genres'] = o['genres'].str.replace('|',',')
    #o['length'] = o['length'].str.replace('[','').str.replace('\'','').str.replace(']','')
#     o['imdb_url'] = o['imdbId'].map(lambda x: 'http://www.imdb.com/title/tt0' + str(x) + '/');
    #o['title'] = o['title_x']
    o[[
        'book_ix', 'book_id','goodreads_book_id','isbn','isbn13',
        'authors','original_publication_year','original_title',
        'title','language_code','average_rating','ratings_count',
        'image_url', 'small_image_url']].sort_values(by='book_ix').to_csv('../data/book_input.csv',index=False)
    print('saved to ../data/book_input.csv')
    print('this fields are not exported',)
    return o[o['image_url'].isnull()]


generate_input()