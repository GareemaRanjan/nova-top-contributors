
import sys
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from github import Github

# past date is calculated as 6 months since 'now'
past_date = datetime.now() - relativedelta(months=6)
g = Github(login_or_token=sys.argv[1])
repo = g.get_repo(full_name_or_id='openstack/nova')
print("Starting to collect commits...")
# Initialise auth_dict to contain list of authors and number of commits.
auth_dict = dict()
print(f"total {repo.get_commits(since=past_date).totalCount}")
for commit in repo.get_commits(since=past_date):
    commit_author = None
    if commit.committer:
        if commit.committer.login == 'openstack-gerrit':
            parentlist = commit.parents
            for parent in parentlist:
                if parent.committer and parent.committer.login != 'openstack-gerrit':
                    commit_author = parent.committer.login # what to be used here - author or committer?
        elif commit.committer.login:
            commit_author = commit.committer.login
        try:
            g.get_user(commit_author)
            if auth_dict.get(commit_author):
                auth_dict[commit_author] +=1
            else:
                auth_dict[commit_author] = 1
        except Exception as e:
            print(f"user {commit_author} , {commit.html_url} not valid")

print(auth_dict)
top_12=sorted(auth_dict.items(), key=lambda x:x[1], reverse=True)[:12]
df = pd.DataFrame(top_12, columns=['Contributor','Number of commits'])
print(df)
df.to_csv('nova_top_contributors.csv', index=False)

