#!/usr/bin/python3
"""doc"""

import os
import re
from fabric.api import *
from fabric.operations import run, put, sudo

env.hosts = ['104.196.123.176', '54.91.99.170']


def do_deploy(archive_path):
    """
        using fabric to distribute archive
    """
    try:
        stat(archive_path)
    except:
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
