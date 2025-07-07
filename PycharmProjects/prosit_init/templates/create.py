from params import gl


def import_project_from_template(project_name : str, namespace_id : int):

    with open('/tmp/export.tgz', 'rb') as f:
            return gl.projects.import_project(
                f,
                path=project_name,
                namespace=namespace_id)