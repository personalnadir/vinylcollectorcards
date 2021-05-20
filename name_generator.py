from random import randrange, random

female_first_names = []
with open('femalenames.txt', 'r') as female:
    female_first_names = [s.strip() for s in female.readlines()]

male_first_names = []
with open('malenames.txt', 'r') as male:
    male_first_names = [s.strip() for s in male.readlines()]

last_names = []
with open('lastnames.txt', 'r') as last:
    last_names = [s.strip() for s in last.readlines()]

band_words = []
with open('bandwords.txt', 'r') as band:
    band_words = [s.strip() for s in band.readlines()]

name_adjectives = []
with open('name_adjectives.txt', 'r') as adjectives:
    name_adjectives = [s.strip() for s in adjectives.readlines()]

def gen_male_name():
    return male_first_names[randrange(0, len(male_first_names))]

def gen_female_name():
    return female_first_names[randrange(0, len(female_first_names))]

def gen_first_name():
    if random() > 0.5:
        return gen_male_name()
    return gen_female_name()

def gen_solo_artist_name():
    first_name = gen_first_name() if random() > 0.4 else ""
    nick_name = name_adjectives[randrange(0, len(name_adjectives))] if random() > 0.8 else ""
    last_name = last_names[randrange(0, len(last_names))] if random() > 0.2 else ""

    if first_name:
        first_name = (first_name[0] + '.') if random() > 0.5 else first_name
    if nick_name:
        nick_name = (nick_name[0] + '.') if random() > 0.5 else nick_name
    if last_name:
        last_name = (last_name[0] + '.') if random() > 0.5 else last_name

    if len(first_name+last_name+nick_name) < 5:
        return gen_solo_artist_name()
    return (nick_name + ' ' + first_name + ' ' + last_name).strip()


def gen_band_name():
    if random() > 0.5:
        return gen_solo_artist_name()
    band_name = 'The ' if random() > 0.7 else ''
    num_words = randrange(1, 4)

    words = [band_words[randrange(0, len(band_words))] for i in range(0, num_words)]

    band_name += ' '.join(words)

    band_name = band_name.title()
    if random() > 0.95:
        band_name = gen_solo_artist_name() + "'s " + band_name

    return band_name

def gen_unique_band_names(num=10):
    unique_names = set([])

    while len(unique_names) < num:
        unique_names.add(gen_band_name())

    return list(unique_names)


if __name__ == '__main__':
    for x in range(1, 10):
        print(gen_unique_band_names())