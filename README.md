This is the turn-events web app to manage artistic gymnastics tournaments. 

Currently runs on Python 3.9+.


## Set up / Installation / Build
- Make sure current folder is `Turnauswertung-py3`
- Set up pyenv: `pyenv install 3.9.16 && pyenv virtualenv 3.9.16 turn-events && pyenv local turn-events`
- Install requirements: `pip install -r requirements.txt`
- Set up db schemas: `python manage.py migrate`

## Run
- Run web server: `python manage.py runserver`
- (Optional) load test data: `python manage.py loaddata gymnastics/fixtures/full_tournament.json`

## Latex Support
- Install `basictex` (`brew install basictex`)
- Install missing latex packages (`tlmgr update --self && tlmgr install titlesec && tlmgr install multirow`)

## Test
todo ;-)
