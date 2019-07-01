# -*- coding: utf-8 -*-
import uuid
import random
import string


def generate_vbrid():
    return 1

def generate_poid():
    return 0

def generate_appoinmentid():
    return uuid.uuid1()

def generate_itemsid():
    return uuid.uuid1()

def generate_containerid():
    return uuid.uuid1()

def generate_itemsid():
    return uuid.uuid1()

def generate_poid():
    return 0

def generate_random_str(randomlength=16):
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str

