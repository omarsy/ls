import os
import shutil

def delete_folder(path):
    """ delete a folder is the folder exists

    Args:
        path (string): path
    """
    if os.path.isdir(path):
        shutil.rmtree(path)
def before_scenario(context, _):
    """ before scenario

    Args:
        context (dict): dict
    """
    context.data_path = os.path.join(os.getcwd(), 'data')
    delete_folder(context.data_path)
    os.mkdir(context.data_path)

def after_scenario(context, _):
    """after scenario

    Args:
        context (dict): context
    """
    delete_folder(context.data_path)