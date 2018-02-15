# -*- coding: UTF-8 -*-

import json

from emoji import UNICODE_EMOJI_ALIAS, EMOJI_ALIAS_UNICODE


def write_dict_to_json(data, filename):
	with open(filename, 'w+') as emoji_file:
		json.dump(data, emoji_file, indent=4)


