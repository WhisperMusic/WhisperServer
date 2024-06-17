# Set up and Launch Muse-Store Server

## Download repository

First you need to download sources of the server. To do that you must clone the repo using the following command line:

```batch
git clone "https://github.com/soucelover/MuseStoreServer/" "MuseStoreServer"
cd "MuseStoreServer"
```

After you've downloaded the repo you should set up server to use it. You can do it manually or by running  automated script.

## Setting up by running script

To run script just run the following command line:

```batch
setup
```

Note: This Automated script can be ran only on Windows platform.

## Setting up manually

### Create of Python Virtual Environment

After repo was downloaded create new virtual environment from the newly created directory:

```batch
python -m venv ".venv"
```

After creating environment you need to activate it:

```batch
.venv\Scripts\activate.bat
```

Or for bash:

```bash
source ".venv/bin/activate"
```

Activation command line is platform specific. [Here](https://docs.python.org/3/library/venv.html#how-venvs-work) is full list of VENV activation commands.

Note: You must activate you virtual environment every time you start new command line session.

### Install all dependencies

You can download and install all the server's dependencies just by running `pip` package manager which by default is included with every virtual environment.

Run the following command line:

```batch
pip install -r requirements.txt
```

File `requirements.txt` contains list of all libraries with their versions so you don't need to install every library manually.

### Environment variables

Before running server you should set some environment variables:

- `SECRET_KEY` - secret key used to encrypt data. Remember: this key must be kept in production secret!
- `SERVER_DEBUG` - server running mode. By default set to `False`.

You can set these variables in `server\.venv` file using the following syntax:

```text
variable=value
```

## Set up server's database

This step isn't included to automated script.

To set up server's database you only need to run Django's migration mechanism.

Firstly ensure that there are no unmade migrations:

```batch
server\manage makemigrations
```

After that you must apply all migrations. This will create your database.

```batch
server\manage migrate
```

## Launching the server

Before you launch server you must ensure your virtual environment is activated.

Then to launch server run the following command line:

```batch
server\manage runserver
```

Or instead of manually activating venv you can run this automated script:

```batch
launch
```

Then you can open the displayed site domen in the browser or start making HTTP requests.
