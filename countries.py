from pygal.maps.world import COUNTRIES

#for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    # return the 2-digit country code for given country name
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
