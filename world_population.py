import json
from countries import get_country_code
import pygal.maps.world as py
from pygal.style import RotateStyle, LightColorizedStyle as LCS

# load the data into a list
filename = 'population_data.json'
f = open(filename)
pop_data = json.load(f)

# build a dictionary of population population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# group the countries into 3 population levels: 0-10m, 10m-1bn, >1bn
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc in cc_populations:
    pop = cc_populations[cc]
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

# create population map of the world by get_country
wm_style = RotateStyle('#115599', base_style=LCS)
wm = py.World(style=wm_style)
wm.title = ('World population in 2010, by country')
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)

wm.render_to_file('world_population.svg')
