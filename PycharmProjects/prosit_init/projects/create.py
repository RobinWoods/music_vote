import gitlab
from params import gl
from templates import create_project_from_template


def create_project(user, prosit_group = None):
    if prosit_group is not None:
        new_project = create_project_from_template(user.username, prosit_group.id)
    else:
        new_project = gl.projects.create(user.username)

    new_project.members.create({
        'user_id': user.id,
        'access_level': gitlab.const.AccessLevel.MAINTAINER,
        })

    return new_project

