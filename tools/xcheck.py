#!/usr/bin/env python3
"""Locate each sutra's statement in its own + neighboring files (mapping check)."""
import glob
import json
import os
import re
import unicodedata


def fold(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s)
                if unicodedata.category(c) != "Mn").lower()
    return s.replace("h", "")


BASE = "/home/ubuntu/shiva-sutras"
tests = {
    "3.17": ["svamatr", "nirmina", "apad"],
    "3.18": ["vidyavi", "janmav"],
    "3.19": ["kavarg", "mahesvar", "pasumat"],
    "3.20": ["trisu", "caturt", "tailav"],
    "3.21": ["magna", "svacit", "pravis"],
    "3.22": ["pranas", "samadar"],
    "3.23": ["madye", "avar"],
    "3.24": ["matrasv", "pratyay", "nastas"],
}
for v, keys in tests.items():
    fn = os.path.join(BASE, "text", "lak_" + v.replace(".", "_") + ".txt")
    print("==", v)
    n = 0
    for line in open(fn, encoding="utf-8"):
        f = fold(line)
        if sum(1 for k in keys if k in f) >= 2:
            print("  ", line[:11].rstrip(), line[11:85].rstrip())
            n += 1
            if n >= 6:
                break
    if n == 0:
        print("   (no hits)")
