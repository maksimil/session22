#!/usr/bin/env python

import os
import sys

args = sys.argv
if len(args) != 3:
    print("Usage: gen-book-list.py [subject] [outfile]")
    exit()

subject = args[1]
outfile = args[2]

subject_name, folder = {
    "algebra": ["Алгебра", "src/algebra"],
    "analysis":["Анализ", "src/analysis"],
    "geometry":["Геометрия", "src/geometry"],
}[subject]


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

booklist_data="""
\\newcommand\\subjectname{{{subject_name}}}

\\newcommand\\contents{{
{contents}
}}
""".format(subject_name=subject_name, contents="\n\\pagebreak\n".join(booklist))

booklist_file = open(outfile, "w")
booklist_file.write(booklist_data)
booklist_file.close()
