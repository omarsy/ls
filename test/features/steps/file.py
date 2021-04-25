# -*- coding: UTF-8 -*-

"""Steps
    """
import os
import subprocess
from datetime import datetime
import platform
from behave import given, when, then


def touch(path: str, time: float, perimissions: str):
    """create an empty file

    Args:
        path (str): file path
        time (str): timestamp
        perimissions (str): your permission example 666 or 777
    """
    with open(path, 'a'):
        os.utime(path, (time, time))
    os.chmod(path, int(perimissions, base=8))
    if platform.system() == 'Windows':
        from win32_setctime import setctime
        setctime(path, time)


@when('we create a file with the name {file_name} on the {date} and which has these permissions {perimissions}')
def step_create_file_impl(context, file_name, date, perimissions):
    """Step to create an empty file

    Args:
        context (dict): context
        file_name (str): file name
        date (str): file creation date. Work only on windows
        perimissions (str): file permission
    """
    touch(os.path.join(context.data_path, file_name), datetime.timestamp(datetime.strptime(date, '%d/%m/%y %H:%M')), perimissions)


@then('executes this command {command} returns this')
def step_execute_impl(context, command):
    """Step to execute a command

    Args:
        context (dict): context
        command (str): the command
    """
    outputs = subprocess.run(command.split(), stdout=subprocess.PIPE).stdout.decode('utf-8').splitlines()
    outputs.sort()
    for index, row in enumerate(context.table):
        assert outputs[index] == row['Output'], 'got {} ; wanted: {}'.format(
            outputs[index], row['Output'])
