#!/usr/bin/python3
""" A function that will clean following deploy """
from fabric.api import *


env.hosts = ['34.201.165.113', '54.90.52.235']
env.user = "ubuntu"


def do_clean(number=0):
    """ A Function that will clean """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
