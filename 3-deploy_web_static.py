#!/usr/bin/python3
""" documentation """

from datetime import datetime
from fabric.api import local
import os
from fabric.api import *
from fabric.operations import run, put, sudo

created_path = None
env.hosts = ['104.196.123.176', '54.91.99.170']


def do_pack():
    """ doc """

    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    name = "versions/web_static_{}.tgz".format(time)
    try:
        local("mkdir -p ./versions")
        local("tar -cvz --file={} ./web_static".format(name))
        return name
    except:
        return None


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    if os.path.isfile(archive_path) is False:
        return False
    try:
        name = archive_path.split("/")
        name = name[1].split(".")
        name = name[0]
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name))
        run("sudo tar -xzf /tmp/{}.tgz -C \
            /data/web_static/releases/{}/".format(name, name))
        run("sudo rm /tmp/{}.tgz".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """ doc """
    global created_path
    if created_path is None:
        created_path = do_pack()
    if created_path is None:
        return False
    return do_deploy(created_path)
