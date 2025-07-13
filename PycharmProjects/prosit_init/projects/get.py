from gitlab import GitlabGetError

from params import gl, block, prosit_name

def get_block_group():
    try:
        block_group = gl.groups.get(block)
    except GitlabGetError as e:
        if e.response_code == 404:
            block_group = gl.groups.create({'name': block, 'path': block})
        else:
            raise e
    return block_group


def get_prosit_group(block_group):
    prosit_group = [group for group in block_group.subgroups.list() if group.name == prosit_name]
    prosit_group = prosit_group[0] if len(prosit_group) == 1 else None

    if prosit_group is None:
        prosit_group = gl.groups.create({'name': prosit_name, 'path': prosit_name, 'parent_id': block_group.id})

    return gl.groups.get(prosit_group.id)


def get_template_list():
    try:
        utils_group = gl.groups.get('utils')
    except GitlabGetError as e:
        raise e
    return utils_group.projects.list()


def get_template_project(template_name):
    template_list = get_template_list()
    for template in template_list:
        if template.name == template_name:
            return gl.projects.get(template.id)
    return None