import domains
import projects

entries = []

for project in domains.projects:
    entries.append(projects.generate_project_from(project))

global_actions = 0
global_thoughts = 0
global_projects = 0
tags = []

for entry in entries:
    global_projects += 1
    global_actions += entry.actions
    global_thoughts += entry.thoughts
    if entry.tags != 'No Tags Found':
        tag_string = str(entry.tags).lower()
        if ',' in tag_string:
            tags_list = tag_string.split(', ')
            for t in tags_list:
                tags.append(t)
        else:
            tags.append(tag_string)

tags = set(tags)
tags = list(tags)

print(f'  Total projects: {global_projects}')
print(f'  Total thoughts: {global_thoughts}')
print(f'  Total actions: {global_actions}')
print(tags)