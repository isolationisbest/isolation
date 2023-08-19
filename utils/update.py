import git
import os
import customtkinter as ctk
def update_repo(repo_path, pat,username,repository):
	# Clone or open existing repo
	if not os.path.exists(repo_path):
		git.Repo.clone_from(f"https://github.com/{username}/{repository}.git", repo_path, branch='main', env={'GIT_ASKPASS': 'echo', 'GIT_SSH_COMMAND': f'ssh -o "StrictHostKeyChecking no" -i {pat}'})
		print("Repo cloned.")
		return

	repo = git.Repo(repo_path)

	# Check if repo is up-to-date
	origin = repo.remotes.origin
	origin.fetch()
	local_head = repo.head.commit
	origin_head = origin.refs.main.commit
	if local_head == origin_head:
		print ("Up to Date")
		return "Up to Date"
	try:
		# Pull new changes
		repo.remotes.origin.pull(force=True)
		print("Repo updated.")
	except:
		try:
			window = ctk.CTk()
			really = ctk.CTkInputDialog(window,title="Are you sure?",text="Are you sure you wanna do this? All changes you made to the repo will overwrite to repository changes. Are you really sure? (type 'yes')")
			#really = input("Are you sure you wanna do this? (type 'yes'): ")
			if really == "yes":
				repo.git.reset('--hard', origin_head)
				print("Repo updated (overwritten local changes to repo)")
			else:
				print("Abort")
		except:
			#window = ctk.CTk()
			#really = ctk.CTkInputDialog(window,title="Are you sure?",text="Are you sure you wanna do this? All changes you made to the repo will overwrite to repository changes. Are you really sure? (type 'yes')")
			really = input("Are you sure you wanna do this? (type 'yes'): ")
			if really == "yes":
				repo.git.reset('--hard', origin_head)
				print("Repo updated (overwritten local changes to repo)")
			else:
				print("Abort")
def check_updates(repo_path, pat,username=None,repository=None):
	try:
    	# Clone or open existing repo
		if not os.path.exists(repo_path):
			git.Repo.clone_from(f"https://github.com/{str(username)}/{str(repository)}.git", repo_path, branch='main', env={'GIT_ASKPASS': 'echo', 'GIT_SSH_COMMAND': f'ssh -o "StrictHostKeyChecking no" -i {pat}'})
			print("Repo cloned.")
			return "0 -- Unknown"

		repo = git.Repo(repo_path)

		# Check if repo is up-to-date
		origin = repo.remotes.origin
		origin.fetch()
		local_head = repo.head.commit
		origin_head = origin.refs.main.commit
		if local_head == origin_head:
			return f"v{len(list(repo.iter_commits('main'))) - 1} -- v{len(list(repo.iter_commits('origin/main'))) - 1}\n (Up-to-Date)"
		else:
			return f"v{len(list(repo.iter_commits('main'))) - 1} -- v{len(list(repo.iter_commits('origin/main'))) - 1}\n (update available)"
	except:
		return "No connection/error occured"
def latest_commit_message(path):
	try:
		repo = git.Repo(path)

		# Get the latest commit and its message
		latest_commit = repo.head.commit
		latest_commit_message = latest_commit.message
		return latest_commit_message
	except:
		return "No connection/error occured"
