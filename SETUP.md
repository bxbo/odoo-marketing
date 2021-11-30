#TRIP : comment to be removed if published

# Mac-os initial setup

## needed tools

- python : brew install python@3.8
- git
- oh my zsh
- virtualenvwrapper : pip3 install virtualenv virtualenvwrapper <br/> zshrc :

```# Setting PATH for Python 3 installed by brew
export PATH=/usr/local/share/python:$PATH

# Configuration for virtualenv
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh`
```

- pycharm
- postgres + pgadmin <br/> https://www.robinwieruch.de/postgres-sql-macos-setup/
- click-odoo + click-odoo-contrib VIA PIPX

## odoo config

- git clone odoo
- createuser -s [username]
- createdb [dbname]
- install wkhtmltopdf :

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null ; brew install caskroom/cask/brew-cask 2> /dev/null
brew install --cask wkhtmltopdf
```

- install odoo into venv from odoo : pip install -r requirement.txt

- ./odoo-bin -d test --addons-path ./addons -s -c odoo_config.cf <br/> on monterey :
  there is an issue for now : set limit_hard to 0
