#!/usr/bin/python3
#coding:utf-8
import sys
from cx_Freeze import setup, Executable

path = sys.path
includes = []
excludes = []
packages = ["Plan_Rapt"]

options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
    name = "Prise_otage",
    version = "0.5",
    description = 'Prise_otage',
    options = {"build_exe": options},
    executables = [Executable("Rapt.py")]
)
