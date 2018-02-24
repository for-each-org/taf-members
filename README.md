# taf-members
Members site for Tippicanoe Arts Federation.

## Setup (Using Docker for Mac/Windows)
1. Install Docker and Docker Compose 
    - [Mac](https://docs.docker.com/docker-for-mac/install/)
    - [Windows](https://docs.docker.com/docker-for-windows/install/)
    - [Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. Run `docker-compose up` in the root directory of the project
    - If a python error displays such that you can't connect to the database, exit and restart the command and it should connect
3. The site should display at http://localhost:8000

## Setup (Mac Using Brew)
1. Install docker and compose
    - If you're on a Mac, this is just `brew install docker docker-compose` (make sure you have homebrew installed).
2. Make sure you have a docker-machine running.
    - If you don't, you may need to `brew install docker-machine`, then run `docker-machine create default` to create a VM in which to run docker containers.
    - After you create a `default` docker-machine, you can make sure it's running with `docker-machine ls`. If you don't see your `default` machine running in the table, then run `docker-machine start default` to start the docker-machine. (When you're done with docker you can stop the virtual machine with `docker-machine stop`.)
3. Run `docker-compose up`. This should bring up both docker containers, labelled `web` (for Django) and `db`(for Postgres).
    - If you see an error about not being able to connect, you may need to help docker-compose find the existing docker machines by running `eval $(docker-machine env)`. This exports variables about running docker instances to the shell. Now, `docker-compose up` should work.
    - If you want docker to run in the background, do `docker-compose up -d`, which should daemonize the docker containers into the background.
4. The server should be running on port 8000 on localhost.
5. To run a database migration: `docker-compose run web python manage.py migrate`
    - Any `./manage.py` operations should be prefixed with `docker-compose run web`. Otherwise, your computer will try to run Django outside of docker, which won't work.

[Source for Docker Setup](https://docs.docker.com/compose/django/#connect-the-database)
