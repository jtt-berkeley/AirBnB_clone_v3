#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['52.90.98.156', '52.207.85.204']


def do_pack():
    """ package """
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("sudo mkdir -p versions/")
        local("sudo tar -zcvl versions/web_static_{}.tgz web_static".
              format(timestr))
    except:
        return None


def do_deploy(archive_path):
    """ deploy """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_name = new_comp.split(".")[0]
        new_folder = ("/data/web_static/releases/" + new_name)
        put(archive_path, "/tmp/")
        run("sudo mkdir -p /data/web_static/releases/{}".format(new_name))
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}".
            format(new_comp, new_name))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {}/ /data/web_static/current".format(new_folder))
        return True
    except Exception as e:
        return False
