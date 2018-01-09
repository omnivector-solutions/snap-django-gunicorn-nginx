# Django-Gunicorn, Snapped!

Django-Gunicorn, Snapped! Is an awesome new way to deploy your Django applications.


This snap delivers two processes:
* Gunicorn
* Nginx

Nginx listens on the snap's private /tmp filesystem at `/tmp/django-gunicorn.sock` and is not visible to any other application or filesystem.


# Build
Build the snap

```bash
$ sudo snapcraft
```

# Install
1) Install the snap

```bash
$ sudo snap install django-gunicorn_0.1_amd64.snap --classic --dangerous
```

2) Migrate/create the database
```bash
$ django-gunicorn.django-manage migrate
```

# Usage
After building and installing the snap, visit
```
http://<your-ip-address>:5000
```
and view your Django application running in the snap!


# Development
Follow the steps below to setup a development environment.

1. Ensure python3-venv is installed
```bash
sudo apt install python3-venv
```
2. Create a virturalenv
```bash
python3 -m venv .venv
```
3. Activate the venv
```bash
source .venv/bin/activate
```
4. Install dependancies + test deps
```bash
pip install -r requirements.txt
pip install -r test-requirements.txt

```
5. Run dev server
```bash
./manage.py runserver <host>:<port>
```


#### TODO
* Make snap strictly confined instead of classic
* Follow snapping best practices more closely by removing unneeded files and dirs (I'm sure there are other things I've overlooked)
* Add wrapper for manage.py to facilitate lifecycle more easily via charm
* Snap nginx separate from django-gunicorn snap (this will make builds faster and a bunch of good/cool things possible)
* Possibily template this demo (ex `./create mynewproj` will create the directory layout and files with the correct names)


#### Author
* James Beedy (c) 2017 <jamesbeedy@gmail.com>

#### Copyright
* AGPLv3 (see `copyright`)
