import git
from collections import Counter
import re

def is_bugfix(commit):
    #words = ["FIX", "FIXING", "FIXED", "BUG FIXED"]
    pattern = re.compile("^.*([B|b]ug)s?|([f|F]ix(es|ed)?|[c|C]lose(s|d)?).*$")
    commit_message = str(commit.message)
    if (pattern.match(commit_message)):
        return True
    else:
        return False

def perform_analysis():
    repo = git.Repo("")
    recent_commits = list(repo.iter_commits('master', max_count=200, since='60.days.ago'))
    bugfixes_commits = []
    for c in recent_commits:
        if (is_bugfix(c)):
            bugfixes_commits.append(c)

    file_list = []
    for bugfix in bugfixes_commits:
        files = bugfix.stats.files
        for f in files:
            file_list.append(f)

    result = Counter(file_list).most_common()
    for key,value in result:
        print(str(key)+" => "+str(value))

def main():
    perform_analysis()

if __name__ == '__main__':
    main()
