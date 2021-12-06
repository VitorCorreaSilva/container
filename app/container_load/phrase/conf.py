from os import environ as env
import random

try:
    logfile_name = env['AMBIENTE']
except KeyError:
    logfile_name = ''
