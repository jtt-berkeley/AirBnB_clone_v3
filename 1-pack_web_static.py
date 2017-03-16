#!/usr/bin/python3
"""
file to practice use of Fabric
"""
import tarfile
import time
import os


def do_pack():
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except:
        return None
