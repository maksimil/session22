#!/usr/bin/env python

import os
import sys

args = sys.argv
if len(args) != 2:
    print("Usage: gen-book-list.py [folder]")
    exit()

folder = args[1]

files = []

for file in os.listdir(folder):
    if file == "book.tex" or file=="book-list.tex":
        continue

    files.append(int(file[:-4]))

files.sort()

booklist = []

for file in files:
    fullpath=os.path.join(folder, f"{file}.tex")
    booklist.append(f"\\input{{{fullpath}}}")

booklist_file = open(os.path.join(folder, "book-list.tex"), "w")
booklist_file.write("\n\\pagebreak\n".join(booklist))
booklist_file.close()
