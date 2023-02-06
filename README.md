## Python Chalice PropelAuth Starter

This repo contains a forkable Python/Chalice backend which uses [PropelAuth](https://www.propelauth.com/?utm_campaign=github) where users can sign up, login, manage their accounts, and view organization and member information.

[Here](https://docs.propelauth.com/example-apps/apps) are guides which will walk you through how to use this frontend code with a variety of frontend library options.

You can use this with any compatible frontend, like the [React PropelAuth Starter](https://github.com/PropelAuth/react-frontend-starter)

### Using this repo

Make sure to update `example/app.py` with your project's information. Then setup your venv, install, and run:

```shell
python3 -m venv venv
$ source venv/bin/activate
$ pip install propelauth-py python-dotenv chalice
$ aws configure
$ chalice new-project example
$ cd example
$ chalice deploy
```