# Django Portfolio

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT License](https://camo.githubusercontent.com/a307f74a14e41e762300323414ddef81f3d53ae2/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f736f757263657265722d696f2f736f757263657265722d6170702e7376673f636f6c6f72423d666630303030)](https://github.com/BrianRuizy/covid-19-dashboard/blob/master/LICENSE.md)
[![Made with Pthon](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![Dashboard screenshot](https://github.com/JGSangara/Django-Portfolio/blob/main/static/Images/download_2.png)

## Getting Started

### Prerequisites

* Python
* Pip

### Installing

Get the project up and running locally in just 5 easy steps.

1. Create a personal [Fork](https://github.com/JGSangara/Django-Portfolio.git) of this repository.

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
https://github.com/JGSangara/Django-Portfolio.git

Cloning into 'Django-Portfolio'...
remote: Enumerating objects: 52, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (48/48), done.
Rremote: Total 52 (delta 3), reused 47 (delta 1), pack-reused 0eceiving objects:  94% (49/52),

Receiving objects: 100% (52/52), 1.46 MiB | 321.00 KiB/s, done.
Resolving deltas: 100% (3/3), done.

cd Django-Portfolio/
```

3. Create your virtual environment, and activate it.

```bash
virtualenv env

source env/bin/activate  # Linux/Mac
env/Scripts/activate  # Windows
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run local server, and **DONE**!

```bash
python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

January 14, 2021 - 23:42:33
Django version 3.1.5, using settings 'Portfolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Deployment

Heroku app is already configured to this repository for *automatic deploys* from any push to the **master** branch. Create a pull request containing your respective changes and wait for merge.

## Built With

* [Django](https://www.djangoproject.com/) Django is a high-level Web framework that encourages rapid development and clean, pragmatic design.
* [Bootstrap](https://getbootstrap.com/)

## License

[@MIT](https://github.com/JGSangara/Django-Portfolio/blob/main/LICENSE)
