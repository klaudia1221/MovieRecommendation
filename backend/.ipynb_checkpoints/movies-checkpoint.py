import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd

path = Path('../data');
movies = ''

def get_data():
    global movies
    movies = pd.read_csv(path/'movie_input.csv')
get_data()


def img_show(url):
    import matplotlib.pyplot as plt 
    from PIL import Image
    from urllib.request import urlopen
    plt.imshow(Image.open(urlopen(url)))