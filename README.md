# How to Start Django
## Install Django
```bash
conda create -n <name> python=3.9
conda activate <name>
pip install -r requirements.txt
```

## Run Django app
```bash
python manage.py runserver 
```
もしポートを指定したい場合は
```bash
python manage.py runserver 127.0.0.1:8000
```
のように実行