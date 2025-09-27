import os
import pathlib
import projects

cwd = os.path.dirname(os.path.realpath(__file__))
domains_file = f'{cwd}\domains.txt'
domains = []
with open(domains_file, 'r+') as file:
    domain_contents = file.read()
    if domain_contents:
        for line in domain_contents.split('\n'):
            if line:
                domains.append(line)

projects = []
for domain in domains:
    for (root, dirs, files) in os.walk(domain):
        for file in files:
            if file.endswith('.corvo'):
                x = os.path.join(os.path.abspath(root), file)
                projects.append(x)

def open_domains():
    os.startfile(domains_file)