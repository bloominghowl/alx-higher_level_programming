#!/usr/bin/python3
"""The read_file function container"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "read", encoding="utf-8") as file:
        files = file.read()
        print(files, end="")
