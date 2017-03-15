#!/usr/bin/python3
"""
script that distributes archive to webservers
"""
import os
from fabric.api import env
from fabric.operations import run, put
env.hosts = ['52.90.98.156', '52.207.85.204']


def do_deploy(archive_path):
    if (os.path.exists(archive_path) is False):
        return False
    try:
        for ip_add in env.hosts:
            put(archive_path, "/tmp/")
        return True
    except:
        return False
