import json
import sys
from datetime import datetime
from functools import lru_cache
from datetime import datetime
import os
import re

from helper import get_date



def parse(file_name):
    complete_object = {}
    current_object = {}

    with open(file_name) as f:
        text = f.read()

    for i in text.split('\n'):
        splitted  = re.split(']|: ',i)

        if len(splitted[0].strip())!=0:
            print(get_date(splitted[0]))


if __name__ == '__main__':
    for i in sys.argv[1:]:
        parse(i)
