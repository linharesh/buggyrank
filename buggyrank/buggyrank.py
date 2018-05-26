import git
from collections import Counter
import re

def is_bugfix(commit):
    #pattern = re.compile("^.*([B|b]ug)s?|([f|F]ix(es|ed)?|[c|C]lose(s|d)?).*$")
    pattern = re.compile("(?i)(fix(e[sd])?|close[sd]?) #[1-9][0-9]*")
    commit_message = str(commit.message)
    if (pattern.match(commit_message)):
        return True
    else:
        return False

def normalize(time, last_commit_time, first_commit_time):
    return (time - first_commit_time) / (last_commit_time-first_commit_time)

def perform_analysis():
    repo = git.Repo("")
    all_commits = list(repo.iter_commits('master'))
    
    last_commit = all_commits[0]
    first_commit = all_commits[-1]

    # to access the datetime of commit:
    # commit.committed_datetime

    print("last commit: ")
    print(last_commit.committed_datetime)

    print("first commit:")
    print(first_commit.committed_datetime)

    bugfixes_commits = []
    for c in all_commits:
        if (is_bugfix(c)):
            bugfixes_commits.append(c)

    file_list = []
    for bugfix in bugfixes_commits:
        nrmlzd = normalize(bugfix.committed_datetime, last_commit.committed_datetime, first_commit.committed_datetime)
        print("$- "+str(nrmlzd))
        #files = bugfix.stats.files
        #for f in files:
        #    file_list.append(f)

    
def main():
    perform_analysis()

if __name__ == '__main__':
    main()
