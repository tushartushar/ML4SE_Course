import os
import subprocess


def download_repo(repo_name, repos_base_path):
    repo_fullname = repo_name.strip('\n')
    if not repo_fullname == "":
        project_url = "https://github.com/" + repo_fullname + ".git"
        folder_name = repo_fullname.replace("/", "_")
        folder_path_new = os.path.join(repos_base_path, folder_name)

        if not os.path.exists(folder_path_new):
            _download_with_url(project_url, folder_path_new)
        else:
            print(folder_name + " already exists. skipping ...")


def _download_with_url(project_url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    print("cloning... " + project_url)
    try:
        # depth=1 is only to get the current snapshot (rather than all commits)
        subprocess.call(["git", "clone", "--depth=1", project_url, folder_path])
    except Exception as ex:
        print("Exception occurred!!" + str(ex))
        return
    print("cloning done.")
