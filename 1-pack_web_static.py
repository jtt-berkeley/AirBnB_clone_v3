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
        os.stat("./version/")
    except:
        os.mkdir("./version/")
    try:
        tar = tarfile.open("./version/web_static_"+timestr+".tgz", "w:gz")
        tar.add("./web_static/")
        return ("./version/web_static_"+timestr+".tgz")
    except:
        return None
