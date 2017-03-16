#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['52.90.98.156', '52.207.85.204']


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


def do_deploy(archive_path):
    try:
        new_arch = archive_path.split("/")
        new_comp = new_arch[-1]
        new_folder = ("/data/web_static/releases/" + new_arch[-1][:-4])
        put(archive_path, "/tmp/{}".format(new_comp))
        run("sudo mkdir -p /data/web_static/releases/{}".format(new_comp))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/".
            format(new_comp))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False
