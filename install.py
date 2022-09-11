#!/bin/env python3

from os import getenv, getcwd, listdir
from subprocess import run
from shutil import move

HOME = getenv("HOME")
CWD = getcwd()
USER = listdir("/home/")[0]

if getenv("USER") == "root":
    run(["sudo", "-u", USER, "python", __file__])
    exit(0)

# Remove previous shell config
run(["rm", "-f", f"{HOME}/.zshrc"])
run(["rm", "-f", f"{HOME}/.bashrc"])
run(["rm", "-f", f"{HOME}/.posixshellrc-personal"])

# Install new shell config
run(["ln", "-s", f"{CWD}/.zshrc", f"{HOME}/.zshrc"])
run(["ln", "-s", f"{CWD}/.bashrc", f"{HOME}/.bashrc"])
run(["ln", "-s", f"{CWD}/.posixshellrc-personal", f"{HOME}/.posixshellrc-personal"])

# Install zsh-syntax-highlighting
run(["wget", "https://github.com/zsh-users/zsh-syntax-highlighting/archive/refs/tags/0.7.1.tar.gz", "-O", f"{HOME}/.cache/a.tar.gz"])
run(["tar", "-axvf", f"{HOME}/.cache/a.tar.gz", "-C", f"{HOME}/.cache"])
move(f"{HOME}/.cache/zsh-syntax-highlighting-0.7.1", f"{HOME}/.zshsh")

print("INTALLED SUCCESSFULLY!")