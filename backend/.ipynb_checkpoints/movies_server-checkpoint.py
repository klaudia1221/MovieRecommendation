import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
import pickle
import torch


# server to copy to the `back` to use
def get_all_movies():
    movies = pd.read_csv('../data/movie_input.csv');
    movies.index = movies['movie_ix']
    return movies

movies = get_all_movies()
y_range=[0.5,5.5]

with open('../data/movie_recommendation.pickle', 'rb') as handle:
    (matrix,
     movies_weights,
     movies_bias,
     user_weights,
     user_bias) = pickle.load(handle)
    
    
# functions
def get_sample(cat, n=5,head=100, min_cnt=20):
    global movies
    
    return movies[(movies['category']==cat) & (movies['cnt']>min_cnt) ].sort_values(by='rating',ascending=False).head(head).sample(n)


# return random maximum number of movies for each of 5 categories done by pca
def get_movies_cold(): # 20 elements
    return pd.concat([
        get_sample(0,5),
        get_sample(1,5),
        get_sample(2,5),
        get_sample(3,5),
        get_sample(4,5),
    ],ignore_index=True)

# get forward
def forward(users_w,users_b,movies_w,movies_b):
    #print(users_w.shape,movies_w.shape)
    dot = ((users_w@torch.t(movies_w)+users_b).squeeze()+torch.t(movies_b)).squeeze()
    res = torch.sigmoid(dot)*(y_range[1]-y_range[0])+y_range[0]
    return res

# get recommendations
def get_movies_recommendations(lists, n = 20): #movie_ix, rating
    global matrix, user_weights, user_bias, movies_bias,movies_weights, movies
    
    lists = np.array(sorted(lists, key=lambda a_entry: a_entry[0]))  #sortowanie po movieId
    movie_ixs = lists[:,0]
    movie_ratings=lists[:,1]
    
    # 2. filtrowanie po zaznaczonych listach, matrix zawiera już oceny dla wsystkich użytkowników
    reduced_matrix=matrix[:,movie_ixs] 
    
    # 3. Obliczamy pearson-a
    from scipy.stats.stats import pearsonr
    
    pearsons = np.array([])
    for ind, i in enumerate(reduced_matrix):
        #print(i, pearsonr(movie_ratings,i.numpy()), pearsonr(movie_ratings,i.numpy())[0])
        p_coeff=pearsonr(movie_ratings,i.numpy())[0]
        pearsons=np.append(pearsons,p_coeff)
    
    # 4. Pobieramy top 10 użytkowników i jego macierze
    top10_users=np.argsort(pearsons)[-10:]
    reduced_users_matrix_weights=user_weights[top10_users] # 10x40
    reduced_users_matrix_bias=user_bias[top10_users] # 10x1
    # print(reduced_users_matrix_weights.shape,reduced_users_matrix_bias.shape)
    
    # 5. Obliczamy średnio wektor dla użytkownia
    mean_vec_weights=reduced_users_matrix_weights.mean(0)[None] # 1x40
    mean_vec_bias=reduced_users_matrix_bias.mean(0)[None]       # 1x1
    
    # 6. forward
    result = forward(mean_vec_weights, mean_vec_bias, movies_weights, movies_bias)
    
    # 7. top 30 films, we will get 50 best movies and random sample 
    size = (len(movie_ixs)+n+50)
    sample_size = (len(movie_ixs)+n)
    top40_films=result.argsort(0,descending=True)[:size].numpy()[np.random.choice(size,sample_size)]
    #print(top40_films, movies.loc[top40_films]['title'], result[result.argsort(0,descending=True)])
    
    # 8. get top 20 movies (n=20)
    #print(top40_films.isin(movie_ixs))# .loc[top40_films].loc[movie_ixs]['movie_ix'])
    
    # top20=top40_films[movie_ixs];
    top20 = np.array([],int)
    for ix in top40_films:
        if len(top20)>=n: break
        if ix not in movie_ixs:
            top20=np.append(top20, ix)
    
    return  movies.loc[top20]