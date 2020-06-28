import re
from urllib import request
from urllib.error import HTTPError

site = input("Enter the site you would like to analyze for keywords: ")
keyword_file = open('keywords.txt', 'r')

def keyword_checker():
    result_list = []
    try:
        site_content = request.urlopen(site).read().decode('utf-8')
    except HTTPError as e:
        print(e)

    for each_line in keyword_file:
        stripped_line = each_line.lower().strip()

        matches = re.findall(stripped_line, site_content)

        if len(matches) == 0:
            result = f' \u274C No match was found for {stripped_line}'
        else:
            result = f' \u2705 {stripped_line} appears {len(matches)} times'

        print(result)
        



keyword_checker()