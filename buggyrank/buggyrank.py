import git
import re
import math
import operator
import sys

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
        print("Developer that most changed "+str(f)+" :")
        for commit,lines in repo.blame('HEAD', f):            
            author_name = str(commit.author.name)
            author_counter[author_name] = author_counter.get(author_name, 0) + len(lines) 
            print(author_name+" => "+str(len(lines)))
        print(Counter(author_counter).most_common(1)[0][0])
        
def main():
    if (len(sys.argv) > 1):
        perform_analysis(sys.argv[1])
    else:
        perform_analysis()

if __name__ == '__main__':
    main()
