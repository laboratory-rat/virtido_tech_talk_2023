import os
import re

import html2text
from bs4 import BeautifulSoup
import cleantext

from src.tools.file import read_file_as_string, get_file_name_with_no_extension, write_file
from src.tools.pubmed import parse_pubmed_content

# set up directories
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
DIRECTORY_DATA = os.path.join(CURRENT_DIRECTORY, 'datasets')
DIRECTORY_RAW = os.path.join(DIRECTORY_DATA, '1_raw')
DIRECTORY_TEXT = os.path.join(DIRECTORY_DATA, '2_cleaned')


def parse_files():
    amount_of_files = 0

    # for each file in raw directory
    for file in os.listdir(DIRECTORY_RAW):

        # if not .html file, skip
        if not file.endswith('.txt'):
            continue

        # read file
        file_path = os.path.join(DIRECTORY_RAW, file)
        raw_text_content = read_file_as_string(file_path)
        TI_sections, AB_sections = parse_pubmed_content(raw_text_content)

        for i in range(len(TI_sections)):
            title = TI_sections[i].replace('\n', '').replace('\r', '').replace('\t', '').replace('\v', '').replace('\f','').replace('?', '').replace('.', '').replace('/', '-')
            title = (title[:75] + '..') if len(title) > 75 else title
            abstract = AB_sections[i]
            file_name = title.strip() + ".txt"
            file_path = os.path.join(DIRECTORY_TEXT, file_name)
            write_file(file_path, abstract)
            print('Saved file: ' + file_name)
            amount_of_files += 1

    return amount_of_files


def main():
    parse_files()


if __name__ == '__main__':
    main()
