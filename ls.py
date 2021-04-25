#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
    Main
    """
import argparse
from src.list_folder_items import list_folder_items_with_prefix
from src.folder_item_information import creation_date, mode, item_name
from src.folder_item_filter import is_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='lists files of a specified folder.')
    parser.add_argument('path', type=str,
                        help='path of the folder if the folder exist or path + prefix')
    parser.add_argument('-l', dest='file_info', action='store_const',
                        const=[mode, creation_date,  item_name], default=[item_name],
                        help='display the mode and the creation date of the files')
    args = parser.parse_args()
    for result in list_folder_items_with_prefix(args.path, [is_file], args.file_info):
        print(result)
