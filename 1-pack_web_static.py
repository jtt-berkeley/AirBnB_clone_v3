#!/usr/bin/python3
"""
file to practice use of Fabric
"""
import tarfile
import time
import os
from subprocess import call

def do_pack():
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        os.stat("./versions")
    except:
        os.mkdir("./versions")
    try:
        tar = tarfile.open("./versions/web_static_"+timestr+".tgz", "w:gz")
        tar.add("./web_static")
        return (os.getcwd()+"/versions/web_static_"+timestr+".tgz")
    except:
        return None
