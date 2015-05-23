This is the turn-events web app to manage artistic gymnastics tournaments.


## Needed Software
- [Python3](https://www.python.org/downloads/) (recomended Version: 3.4.3)
- [MySQL server](http://dev.mysql.com/downloads/mysql/)
- Python3 plugins as specified [here](https://github.com/saechtner/turn-events/blob/master/Turnauswertung-py3/requirements.txt)


## Installation
1. Install [Python3](https://www.python.org/downloads/) and [MySQL](http://dev.mysql.com/downloads/mysql/) in case you haven't done yet.
2. Install the Python plugins specified [here](https://github.com/saechtner/turn-events/blob/master/Turnauswertung-py3/requirements.txt).
3. Adjust database settings in [settings.py](https://github.com/saechtner/turn-events/blob/master/Turnauswertung-py3/Turnauswertung/settings.py)
4. Create a database/schema (default: `turnauswertung`).
5. Migrate: `python manage.py migrate`
6. Start the web app using `python manage.py runserver` from the `Turnauswertung-py3` folder in the project.
  1. You might want to load some test data using `python manage.py loaddata gymnastics/fixtures/full_tournament.json`
