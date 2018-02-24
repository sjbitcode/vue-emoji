import json
import requests
from bs4 import BeautifulSoup


url = 'http://www.unicode.org/emoji/charts/emoji-list.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

output = {}

def clean_keyword(keyword):
    # ex. 'travel | place | mountain '
    if keyword != '|':
        return list(
            filter(None, keyword.split(' | '))
        ) 


# remember state of object, main category & sub category
curr_main_category = ''
curr_sub_category = ''


for row in rows:
    '''
    Parse emoji unicode table and build data dictionary:
    {
        'main-category': {
            'sub-category': [
                {
                    'codepoint': 'some-codepoint',
                    'shortcode': 'some-shortcode',
                    'keywords': ['foo', 'bar']
                }
            ] 
        }
    }
    '''

    # Is it a main category? If yes, add string as key, val: {} to output
    if row.find('th', {'class': 'bighead'}):
        name = row.find('a').string
        # print('Main Category: {}'.format(name))
        curr_main_category = name
        output[name] = {}

    # Is it a sub category? If yes, add string as key, val: [] to previous key's val
    if row.find('th', {'class': 'mediumhead'}):
        name = row.find('a').string
        # print('Sub Category: {}'.format(name))
        curr_sub_category = name
        output[curr_main_category][name] = []

    # Else, find all td in that tag, extract data
    elif row.find_all('td'):
        emoji_dict = {}

        data = row.find_all('td')

        # Parsing code
        code = data[1].string
        _code = []

        for c in code.split(' '):
            if len(c) == 6:
                _code.append(c.replace('+', '0000'))
            else:
                _code.append(c.replace('+', '000'))

        code = ''.join(_code).replace('U', '\\U')
        emoji_dict['codepoint'] = code

        # Parsing shortcode
        shortcode = data[3].string
        shortcode = shortcode.replace(' ', '_') \
                        .replace(':', '') \
                        .replace(',', '') \
                        .replace('“', '') \
                        .replace('”', '') \
                        .strip()
        emoji_dict['shortcode'] = shortcode


        # Parsing keywords
        keywords_td = data[4]
        keywords = []

        for chunk in keywords_td.strings:
            keywords += clean_keyword(chunk)

        emoji_dict['keywords'] = keywords
        
        output[curr_main_category][curr_sub_category].append(emoji_dict)


def write_dict_to_json(data, filename):
    with open(filename, 'w+') as emoji_file:
        json.dump(data, emoji_file, indent=4)
