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
                new_folder = ("/data/web_static/releases/"+ new_arch[-1][:-4])
                cmd = "mkdir " + new_folder
                sudo(cmd)
                cmd = "tar -xzf /tmp/"+ new_arch[-1] + " -C " + new_folder
                sudo(cmd)
                cmd = "mv " + new_folder + "/web_static/* " + new_folder
                sudo(cmd)
                cmd = "rm -rf " + new_folder + "/web_static"
                sudo('rm -rf /data/web_static/current')
                cmd = "ln -s " + new_folder + " /data/web_static?current"
                sudo(cmd)
        return True:
    except:
        return False
