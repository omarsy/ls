# -*- coding: UTF-8 -*-

"""Functions to filter a folder item
    """
import os


def is_basename_prefixed(context) -> bool:
    """The is_basename_prefixed method checks if a basename  starts with the specified prefix(string).

    Args:
     context (dict): must have an item item_path(str) a,d an item prefix(str)

    Returns:
        bool: returns True if a basename starts with the specified prefix(string).
       If not, it returns False.
    """
    return os.path.basename(context['item_path']).startswith(context['prefix'])


def is_file(context) -> bool:
    """The is_file check if path is a file

    Args:
      context (dict): must have an item item_path(str)

    Returns:
        bool: returns True if it is a file.
       If not, it returns False.
    """
    return os.path.isfile(context['item_path'])
