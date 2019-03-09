import movies_utils as m
from tqdm import tnrange, tqdm_notebook, tqdm
tqdm.pandas()  # <- added this line


mv = m.get_movies(m.small_path)
mv.loc[:,['cover']] = mv.loc[:]['imdbId'].progress_map(m.get_cover_url)

mv.to_csv('movies_data.csv')


