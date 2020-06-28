import re
import gzip
from urllib import request
from urllib.error import HTTPError

site = input('Enter the site you would like to analyze for keywords: ')
keywords = input(
    'Enter the keywords you would like to analyze for, seperated by a space: ').split()

def keyword_checker():
    result_list = []
    try:
        site_content = request.urlopen(site).read().decode('utf-8')
    except HTTPError as e:
        print(e)

    for keyword in keywords:
        matches = re.findall(keyword, site_content, re.IGNORECASE)

        if len(matches) == 0:
            result = f' \u274C No match was found for {keyword}'
        else:
            result = f' \u2705 {keyword} appears {len(matches)} times'

        print(result)
        



keyword_checker()