# testCRM

# Installation

### Install Python 3.9.0 with `pyenv`

#### Install virtual environment and Python 3.9.0
```
curl https://pyenv.run | bash
pyenv install 3.9.0
pyenv shell 3.9.0
```

#### Install testCRM dependencies
Install in root directory testCRM
```
python -m venv env

source env/bin/activate #for Linux

pip install -r requirements.txt
```
#### Add fake data in db
```
python seed.py
```


#### Test running `testCRM`

```
python manage.py runserver
```


