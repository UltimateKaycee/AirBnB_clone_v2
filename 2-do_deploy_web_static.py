#!/usr/bin/python3
"""
A script - Fabric script based on the
file 1-pack_web_static.py to distribute an
archive to web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['34.201.165.113', '54.90.52.235']


def do_deploy(path):
    """Function to distribute an archive to web servers"""
    if exists(path) is False:
        return False
    try:
        file_n = path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
