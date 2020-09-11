import os, yaml, github, sys

e = os.environ
repo = e['GITHUB_REPOSITORY']
auth = github.Github(e['USERNAME'], e['PASSWORD'])
r = auth.get_repo(repo)

f = open('_data/issues.yml')
issues = yaml.load(f, Loader = yaml.FullLoader)

def reportissue():
  print('New issue detected, ')
  title = 'New issue detected!'
  body = 'One or more below mentioned site(s) did not respond correctly to the CI ping. ```{}```'.format(f.read())
  labels = r.get_label('outage')
  assignee="shreejoy"
  r.create_issue(title=title, body=body, assignee=assignee, labels=[labels])

def noissues():
  print('No new problem detected.')

if len(issues) == 0:
  noissues()
else:
  reportissue()

os.remove('_data/issues.yml')
sys.exit(0)
