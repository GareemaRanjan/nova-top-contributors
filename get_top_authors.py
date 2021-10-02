
import sys
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from github import Github

# past date is calculated as 6 months since 'now'
past_date = datetime.now() - relativedelta(months=6)
g = Github(login_or_token=sys.argv[1])
repo = g.get_repo(full_name_or_id='openstack/nova')

# Initialise auth_dict to contain list of authors and number of commits.
auth_dict = dict(No_comm=0)
for commit in repo.get_commits(since=past_date):
    if not commit.committer:
        auth_dict['No_comm'] +=1
    else:
        if auth_dict.get(commit.committer.login):
            auth_dict[commit.committer.login] +=1
        else:
            auth_dict[commit.committer.login] = 1


top_12=sorted(auth_dict.items(), key=lambda x:x[1], reverse=True)[:12]
df = pd.DataFrame(top_12, columns=['Contributor','Number of commits'])
print(df)
df.to_csv('nova_top_contributors.csv', index=False)

