import git
import re
import math
import operator
import sys
import os

from collections import Counter

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

def score(normalized_time):
    return (1 / (1 + math.exp(-12 * normalized_time + 12)))

def perform_analysis(branch='master'):
    repo = git.Repo("")
    all_commits = list(repo.iter_commits(branch))
    
    last_commit = all_commits[0]
    first_commit = all_commits[-1]

    # to access the datetime of commit:
    # commit.committed_datetime

    bugfixes_commits = []
    for c in all_commits:
        if (is_bugfix(c)):
            bugfixes_commits.append(c)


    print("Number of bugfix commits: "+str(len(bugfixes_commits)))
    print(" - - - - - - - - - - - - - -")
    score_dict = dict()
    for bugfix in bugfixes_commits:
        normalized_time = normalize(bugfix.committed_datetime, last_commit.committed_datetime, first_commit.committed_datetime)
        scr = score(normalized_time)
        files = bugfix.stats.files
        for f in files:
            score_dict[str(f)] = score_dict.get(str(f), 0) + scr

    sorted_dict = sorted(score_dict.items(), key=operator.itemgetter(1), reverse=True)
    print("Bug prone files (in order, to most bug-prone to less bug-prone):")
    for value in sorted_dict:
        print(str(value[0]))

    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - --")
    # matching bug-prone files to commits
    print("Matching bug-prone files to commits ")
    for value in sorted_dict:
        f = value[0]
        print("Commits that changed "+str(f)+ " :")
        for c in bugfixes_commits:
            files = c.stats.files
            if (f in files):
                print(c)
        print()

    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - --")
    # matching bug-prone files to developer
    print("matching bug-prone files to author")
    author_counter = dict()
    for value in sorted_dict:
        f = value[0]
        if os.path.isfile(f): 
            print("Developer that most changed "+str(f)+" :")
            for commit,lines in repo.blame('HEAD', f):   
                    author_name = str(commit.author.name)
                    author_counter[author_name] = author_counter.get(author_name, 0) + len(lines) 
            print(Counter(author_counter).most_common(1)[0][0])
        
def display_help():
    print(" # # # # # # # # # BUGGYRANK # # # # # # # # # ")
    print(" # A Defect Prediction Technique That Uses   # ")
    print(" # Information From Version Control Systems  # ")
    print(" # # # # # # # # # # # # # # # # # # # # # # # ")
    print()
    print(" # # # # # #      HOW TO USE ?     # # # # # # ")
    print(" 1) Get inside the project directory that    # ")
    print(" contains the '.git' directory   # ")
    print(" # # # # # # # # # # # # # # # # # # # # # # # ")
    print(" 2) Type in the console:                     # ")
    print(" $ buggyrank [BRANCH-NAME]                   # ")
    print(" # // The default branch is master //        # ")
    print(" # # # # # # # # # # # # # # # # # # # # # # # ")
    print(" 3) See the results!                         # ")
    print(" # # # # # # # # # # # # # # # # # # # # # # # ")
    print(" More information: https://github.com/linharesh/buggyrank")    

def main():
     
    if not os.path.isdir('.git'):
        sys.exit("Error: .git directory not found. Make sure that you are in the correct directory.")

    if (len(sys.argv) > 1):
        arg = sys.argv[1]
        if (arg == '-h' or arg == '--help'):
            display_help()
        else:
            perform_analysis(sys.argv[1])
    else:
        perform_analysis()

if __name__ == '__main__':
    main()
