from db import connect_to_db, query_data
from params import gl


def get_users_bdd_list():
    conn = connect_to_db()
    return [user[1] for user in query_data(conn, "users")]

def get_users_list():
    users_gl_list = gl.users.list()
    users_bdd_list = get_users_bdd_list()
    return [user for user in users_gl_list if user.username in users_bdd_list]