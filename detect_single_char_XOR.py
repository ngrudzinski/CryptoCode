import urllib2
from single_byte_XOR import xor_2_strings

FIXED_URL = "http://cryptopals.com/static/challenge-data/4.txt"


def get_strings_from_file(url):
    data = urllib2.urlopen(url)
    for raw_line in data:
        line = raw_line.rstrip('\n')
        xor_2_strings(line)

get_strings_from_file(FIXED_URL)