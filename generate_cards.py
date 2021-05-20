from collections import namedtuple
from random import randrange, random, shuffle
from name_generator import gen_unique_band_names

num_genres = 50
num_artists = 50
num_produces = 50
num_labels = 50

max_genres_per_artist = 3

genres = []
with open('music_genres.txt', 'r') as music:
    genres = [s.strip() for s in music.readlines()]

shuffle(genres)
genres = genres[:num_genres]

Record = namedtuple('Record', ['chart_pos','year','band','producer','genre','label'])
Band = namedtuple('Band', ['name', 'producers', 'genres', 'labels', 'formed', 'years_active'])

def pick_genres(num=1):
	picked_genres = set()
	while len(picked_genres) < num:
		picked_genres.add(genres[randrange(0, len(genres))])
	return list(picked_genres)

def generate_bands():
	artists = gen_unique_band_names(num=num_artists)
	bands = [Band(name,'',pick_genres(randrange(1, max_genres_per_artist)),'', randrange(1956, 2021), randrange(2, 30)) for name in artists]
	return bands

if __name__ == '__main__':
	for b in generate_bands():
		print(b.name + ' (' + str(b.formed) + '-' + str(b.formed + b.years_active) + ')')
		print('\t' + 'genres: ' + (', ').join(b.genres))

