## Extract 12 most active commit authors from Openstack/Nova - Python3.7


## Step 1: Install python dependencies
```
pip3 install -r requirements.txt
```

## Step 2: Get your GitHub access token

## Step 3: Run the python script
```
python3 get_top_authors.py <your_github_access_token>
```
Result: Dataframe consisting of top 12 committers with total number of commits they made. 
        Also, the data is saved as a csv file titled 'nova_top_contributors.csv'.