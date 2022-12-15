#!/usr/bin/env python

import os
import re
import sys

def conv_number(n):
    return chr(65+n%25)+chr(65+n//25)

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

tickettitle_regex = r"\\tickettitle{.*}{(.*)}"

files = []
tickets = {}

for file in os.listdir(folder):
    if file == "book.tex" or file=="book-list.tex":
        continue

    ticket_number = int(file[:-4])
    files.append(ticket_number)

    ticket_contents_file = open(os.path.join(folder, file))
    ticket_contents = ticket_contents_file.readlines()
    ticket_contents_file.close()

    ticket_title = list(filter(lambda v: v!=None, map(lambda line: re.match(tickettitle_regex, line), ticket_contents)))[0].group(1)

    tickets[ticket_number] = ticket_title

#  print(tickets)

files.sort()

booklist = []

for file in files:
    fullpath=os.path.join(folder, f"{file}.tex")
    booklist.append(f"\\input{{{fullpath}}}")

booklist_data="""
\\newcommand\\subjectname{{{subject_name}}}

{titles}

\\newcommand\\ticketlist{{{ticket_list}}}

\\newcommand\\contents{{
{contents}
}}
""".format(
    titles="\n".join(map(lambda file:f"\\newcommand\\ticket{conv_number(file)}{{{tickets[file]}}}", files)),
    subject_name=subject_name, contents="\n\\pagebreak\n".join(booklist),
    ticket_list=",".join(map(lambda file:f"{file}/\\ticket{conv_number(file)}",files))
)

booklist_file = open(outfile, "w")
booklist_file.write(booklist_data)
booklist_file.close()
