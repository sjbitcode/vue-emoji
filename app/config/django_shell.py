import json
import os
import sys

import django


def print_header():
    header = """
      _   _                                    _            _  _
   __| | (_)  __ _  _ __    __ _   ___    ___ | |__    ___ | || |
  / _` | | | / _` || '_ \  / _` | / _ \  / __|| '_ \  / _ \| || |
 | (_| | | || (_| || | | || (_| || (_) | \__ \| | | ||  __/| || |
  \__,_|_/ | \__,_||_| |_| \__, | \___/  |___/|_| |_| \___||_||_|
       |__/                |___/
    """
    print(header)
    print("")


if __name__ == '__main__':
    sys.path.insert(0, os.path.abspath('/usr/src/app'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()

    # Import django modules.
    from django.conf import settings
    from django.contrib.auth.models import User
    from django.db.models import Q
    from django.utils import timezone

    # Import models.
    from emojis.models import *

    # Import serializers.
    from emojis.serializers import *

    # Easy model functions.
    uu = lambda: User.objects.all()
    em = lambda: Emoji.objects.all()
    mc = lambda: MainCategory.objects.all()
    sc = lambda: SubCategory.objects.all()
    kw = lambda: Keyword.objects.all()

    # Helper functions.
    def dumps(data):
        print(json.dumps(data, indent=2))

    print_header()
    print(timezone.now().strftime("%a %b %d, %Y %H:%M:%S"))
    if settings.DEBUG:
        print('Local dev environment')
    else:
        print('! Production environment ! (Be careful)')