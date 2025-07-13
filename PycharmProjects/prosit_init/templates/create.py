from params import gl


def create_project_from_template(project_name : str, namespace_id : int):
    with open('/tmp/export.tgz', 'rb') as f:
            new_project = gl.projects.import_project(
                f,
                path=project_name,
                namespace=namespace_id)
            print(new_project)
            return gl.projects.get(new_project['id'])