This is the turn-events web app to manage artistic gymnastics tournaments.

Currently runs on Python 3.9+.


## Set up / Installation / Build
- Make sure current folder is `Turnauswertung-py3`
- Set up pyenv: `pyenv install 3.9.16 && pyenv local 3.9.16`
- Install poetry: `curl -sSL https://install.python-poetry.org | python3 -`
- Install dependencies: `poetry install`
- Start poetry shell: `poetry shell`
- Set up db schemas: `cd Turnauswertung-py3 && ./manage.py migrate`

## Alternative setup using nix
- Install nix: `curl -L https://nixos.org/nix/install | sh`
- Install direnv `brew install direnv`
- Configure poetry layouting as described in [this github comment](https://github.com/direnv/direnv/issues/592#issuecomment-1277617137)
- Create a file `.envrc` in the project root with the following content:
  ```
  use flake
  layout poetry
  ```
- Run `direnv allow` and wait for the environment to build
- Set up db schemas: `cd Turnauswertung-py3 && ./manage.py migrate`
- Note: This setup contains the Latex setup

## Run
- Run web server: `python manage.py runserver`
- (Optional) load test data: `python manage.py loaddata gymnastics/fixtures/full_tournament.json`

## Latex Support
- Install `basictex` (`brew install basictex`)
- Install missing latex packages (`tlmgr update --self && tlmgr install titlesec multirow hyphenat`)

## Test
todo ;-)
