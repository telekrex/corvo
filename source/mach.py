import domains
import projects

entries = []
for project in domains.projects:
    entries.append(projects.generate_project_from(project))

tags = []
for entry in entries:
    if entry.tags != "No Tags Found":
        tag_string = str(entry.tags).lower()
        if "," in tag_string:
            tags_list = tag_string.split(", ")
            for t in tags_list:
                tags.append(t)
        else:
            tags.append(tag_string)
tags = set(tags)
tags = list(tags)


def get_filtered_entries(filter="all"):
    filtered_entries = []
    for entry in entries:
        if projects.project_has_tag(entry, filter):
            filtered_entries.append(entry)
    return filtered_entries