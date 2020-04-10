#!/usr/bin/python3
""" documentation """

from datetime import datetime
from fabric.api import local


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
