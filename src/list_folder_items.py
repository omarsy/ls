# -*- coding: UTF-8 -*-

"""Function to list folder elements

    """
import os
from src.folder_item_filter import is_basename_prefixed


def list_folder_items(context: dict, filters: list, decorators: list) -> list:
    """Lists all items of a folder  then decorate the items

    Args:
        context ([type]): [description]
        filters (list): list of func that permit to filter an item
        decorators (list): list of func informations to add for folder item
    Yields:
        Iterator[list]: list of str that contain the informations that we add for an item
    """
    for filename in os.listdir(context['path']):
        context['item_path'] = os.path.join(context['path'], filename)
        for filt in filters:
            if not filt(context):
                break
        else:
            yield ' '.join(map(lambda file_decorator: file_decorator(context), decorators))


def list_folder_items_with_prefix(path: str, filters: list, decorators: list) -> list:
    """Lists all items of a folder if the folder exists,
        if not, list all items prefixed by the basename of the Path, then decorate the items

    Args:
        path (str): path of directory if the directory exists or path + prefix
        filters (list): list of func that permit to filter an item
        decorators (list): list of func informations to add for folder item

    Returns:
        list: list of str that contain the informations that we add for an item
    """
    context = {'path': path}
    if os.path.isdir(path):
        return list_folder_items(context, filters, decorators)
    context['path'] = os.path.dirname(path)
    context['prefix'] = os.path.basename(path)
    if not os.path.isdir(context['path']):
        return []
    filters.append(is_basename_prefixed)
    return list_folder_items(context, filters, decorators)
