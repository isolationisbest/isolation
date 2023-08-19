import os
os.system("pip install gitpython")

try:
    import git

    ## DO NOT SHARE WITH OTHER PEOPLE WHICH DID NOT BOUGHT THIS APP, UNLESS YOU WANT TO LOOSE ACCESS TO THE REPO! ##
    pat = ""
    ## DO NOT SHARE WITH OTHER PEOPLE WHICH DID NOT BOUGHT THIS APP, UNLESS YOU WANT TO LOOSE ACCESS TO THE REPO! ##

    repo = git.Repo.clone_from(f"https://{pat}@github.com/", "isolation/")
    if os.path.exists("isolation/"):
        input("Complete! (press anything)")
    else:
        input("Install failed! Do you run from terminal?")
except Exception as e:
    print("propably git not installed! You should install git before continue")
    print("")
    print("git download: https://git-scm.com/downloads")
    print("(If you see this error even after installing git, you should try run installer inside terminal)")
    print("error: "+ str(e))
    input("press enter to exit")