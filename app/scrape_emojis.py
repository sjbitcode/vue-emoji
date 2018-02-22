import json
import requests
from bs4 import BeautifulSoup

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;"
}

def html_escape(text):
    # Produce entities within text
    return ''.join(html_escape_table.get(c, c) for c in text)


url = 'http://www.unicode.org/emoji/charts/emoji-list.html'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

output = {}

# Shorten
# rows = rows[:10]

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

    # import pdb; pdb.set_trace();

    # Is it a main category? If yes, add string as key, val: {} to output
    if row.find('th', {'class': 'bighead'}):
        name = row.find('a').string
        # print('Main Category: {}'.format(name))
        curr_main_category = name
        output[name] = {}

    # Is it a sub category? If yes, add string key, val: [] to previous key
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
        emoji_dict['code'] = code

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

        # print(emoji_dict)
        
        output[curr_main_category][curr_sub_category].append(emoji_dict)

# print(output)

def write_dict_to_json(data, filename):
    with open(filename, 'w+') as emoji_file:
        json.dump(data, emoji_file, indent=4)

write_dict_to_json(output, 'emoji-full-3.json')

# print(json.dumps(output, indent=4))


#https://stackoverflow.com/questions/47716217/converting-emojis-to-unicode-and-vice-versa-in-python-3
# s2 = "\U0001F631"
# print s2 to get emoji
# s2_unicode = 'U+{:X}'.format(ord(s2))
# print s2_unicode to get unicode codepoint
# s2.encode('unicode-escape').decode('ASCII') to get '\\U0001f631'
# print(s2.encode('unicode-escape').decode('ASCII')) to get '\U0001f631'


# Emoji to Unicode
# emoji.encode('unicode-escape').decode('utf-8')

# Surrogate pairs to Emoji
# "\ud83d\ude4f".encode('utf-16', 'surrogatepass').decode('utf-16')

# Load json file
# with open('filename.json', encoding='utf-8') as input:
#     data = json.load(input)

