import gitlab

gitlab_url = "https://gitlab.derenty.net"
gitlab_token = "glpat-x4sdt3522fe4JzAzGvCh"
prosit_name = "prosit1"
block = "Web"
users_list = ["Auxou", "RobinWoods"]


gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_token)
