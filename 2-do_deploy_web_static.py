#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os
from fabric.api import env
from fabric.operations import run, put, sudo
env.hosts = ['52.90.98.156', '52.207.85.204']


def do_deploy(archive_path):
    if (os.path.exists(archive_path) is False):
        return False
    try:
        for ip_add in env.hosts:
            put(archive_path, "/tmp/")
            with (settings(host_string=ip_add)):
                new_arch = archive_path.split("/")
                new_folder = ("/data/web_static/releases/" + new_arch[-1][:-4])
                run("mkdir {}".format(new_folder))
                run("tar -xzf /tmp/{} -C {}".format(new_arch[-1], new_folder))
                run("rm /tmp/{}".format(new_arch[-1]))
                run("mv {}/web_static/* {}".format(new_folder, new_folder))
                run("rm -rf {}/web_static".format(new_folder))
                run('rm -rf /data/web_static/current')
                run("ln -s {} /data/web_static/current".format(new_folder))
        return True
    except:
        return False
