#!/bin/env python3

from os.path import exists
from os import getenv, remove, getcwd, listdir
from subprocess import run

HOME = getenv("HOME")
CWD = getcwd()
USER = listdir("/home/")[0]

if getenv("USER") == "root":
    run(["sudo", "-u", USER, "python", __file__])
    exit(0)

run(["rm", "-f", f"{HOME}/.zshrc"])
run(["rm", "-f", f"{HOME}/.bashrc"])

run(["ln", "-s", f"{CWD}/.zshrc", f"{HOME}/.zshrc"])
run(["ln", "-s", f"{CWD}/.bashrc", f"{HOME}/.bashrc"])

print("INTALLED SUCCESSFULLY!")