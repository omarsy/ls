# -*- coding: UTF-8 -*-

""" Functions to get a additional information from a item path
    """
import os
import stat
from datetime import datetime


def creation_date(context: dict) -> str:
    """Get the item creation date.
    Warning(Support only file)

    Args:
        context (dict): must have an item item_path(str)

    Returns:
        str: Creation date in this format 'YYYY-MM-DD hh:mm'
    """
    return datetime.fromtimestamp(os.path.getctime(context['item_path'])).strftime('%Y-%m-%d %H:%M')


def mode(context: dict) -> str:
    """Get the item permission
         Warning(Support only file)
    Args:
        context (dict): must have an item item_path(str)

    Returns:
        str: file mode in this format 'rwxrwxrwx'
    """
    return stat.filemode(os.stat(context['item_path']).st_mode)[1:]


def item_name(context: dict) -> str:
    """Get the item name from a path
         Warning(Support only file)
    Args:
        context (dict): must have an item item_path(str)

    Returns:
        str: the item name
    """
    return os.path.basename(context['item_path'])
