# Introduction
This is the turn-events webapp to manage artistic gymnastic tournaments.
Someday more sports might be supported.


# Needed Software
- [Python3](https://www.python.org/downloads/) (recomended Version: 3.4.3)
- [MySQL server](http://dev.mysql.com/downloads/mysql/) (with a database called: `turnauswertung`)
- several more Python3 plugins specified [here](https://github.com/saechtner/turn-events/blob/master/Turnauswertung-py3/requirements.txt)


# Installation
1. Install [Python3](https://www.python.org/downloads/) and [MySQL](http://dev.mysql.com/downloads/mysql/) in case you haven't done yet.
2. Install the plugins mentioned [here](https://github.com/saechtner/turn-events/blob/master/Turnauswertung-py3/requirements.txt).
3. Create a database called `turnauswertung`.
4. Start the web app using `python manage.py runserver` from the `Turnauswertung-py3` folder in the project.
  1. You might load some test data using 'python manage.py loaddata gymnastics/fixtures/full_tournament_2_squads.json'


# Versions
Right now this project is in the early alpha. Once we think it is appropriate we'll specify versions.

# Known issues
- PDFs might not be generated on Windows systems
