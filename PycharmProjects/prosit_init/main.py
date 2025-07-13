from projects import get_block_group, create_project
from projects.get import get_prosit_group, get_template_project
from templates import download_export, create_export
from users import get_users_list

block_group = get_block_group()
prosit_group = get_prosit_group(block_group)

template_project = get_template_project("nodeJS-template")
download_export(create_export(template_project))

users = get_users_list()

for user in users:
    create_project(user, prosit_group)