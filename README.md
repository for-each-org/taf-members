# taf-members
Members site for Tippicanoe Arts Federation.


## Instructions to run
1. Install docker and compose
2. Run `docker-compose up`. The server should be running on port 8000
3. To run a database migration: `docker-compose run web python manage.py migrate`

[Source for Docker Setup](https://docs.docker.com/compose/django/#connect-the-database)