from dataclasses import dataclass
import pathlib
import os

@dataclass
class Project():
    name: str
    desc: str
    status: str
    tags: str
    actions: int
    thoughts: int
    corvo_file_path: str
    location_path: str

def generate_project_from(file_full_path):
    with open(file_full_path, 'r') as read_file:
        contents = read_file.read().split('\n')
        try:
            name = contents[0]
            print(name)
        except:
            name = 'No Name Found'
        try:
            desc = contents[1]
        except:
            desc = 'No Desc Found'
        try:
            status = contents[2]
        except:
            status = 'No Status Found'
        try:
            tags = contents[3]
        except:
            tags = 'No Tags Found'
        corvo_file_path = os.path.abspath(file_full_path)
        corvo_file_path = pathlib.PureWindowsPath(corvo_file_path).as_posix()
        location_path = os.path.dirname(file_full_path)
        location_path = pathlib.PureWindowsPath(location_path).as_posix()
        actions = 0
        thoughts = 0
        for line in contents:
            if line:
                if line.startswith('/ '):
                    actions += 1
                if line.startswith('. '):
                    thoughts += 1
        # automatically (and non-destructively!)
        # add the tag "active" to projects with
        # more than 0 actions, and "inactive"
        # if versa
        if actions > 0:
            tags += ', working'
            print('adding active tag')
            print(tags)
        else:
            tags += ', sleeping'
    return Project(
        name = name,
        desc = desc,
        status = status,
        tags = tags,
        actions = actions,
        thoughts = thoughts,
        corvo_file_path = corvo_file_path,
        location_path = location_path
    )

def project_has_tag(Project, tag):
    if tag == 'all':
        return True
    if tag.lower() in str(Project.tags).lower():
        return True
    else:
        return False

def open_project_corvo(Project):
    os.startfile(Project.corvo_file_path)

def open_project_location(Project):
    os.startfile(Project.location_path)