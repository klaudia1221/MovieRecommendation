# UWAGA BARDZO DŁUGIE URUCHAMIANIE - 8 godzin

import movies_utils as m
from tqdm import tnrange, tqdm_notebook, tqdm
tqdm.pandas()  # <- added this line


mv = m.get_movies(m.small_path)
#mv = mv[:4]
mv = m.set_movie_info(mv)
#mv.loc[:,['cover']] = mv.loc[:]['imdbId'].progress_map(m.get_cover_url)

mv.to_csv('../data/movies_alldata.csv')


