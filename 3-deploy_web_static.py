#!/usr/bin/python3
"""A Script to create and distributes archive to web servers"""
import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['34.201.165.113', '54.90.52.235']


def do_pack():
    """Function to generate tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except Exception:
        return None


def do_deploy(archive_path):
    """Function to distribute archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except Exception:
        return False


def deploy():
    """Function to create and distribute archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
