# Cadastral check emulator

The app accepts requests specifying a cadastral number, latitude and longitude, then emulates a forward request to an external server that can process the request for up to 60 seconds. Then the app can return the result of the request(`true` or `false`).

Admin panel: http://127.0.0.1:8000/admin/


Interactive Swagger documentation: http://127.0.0.1:8000/docs/


Endpoints:


/query : post a query (returns a query json with assigned id)


/result : get the most recent query (can take up to a minute to check the query)


/result/{id} : get any query with given id


/history : get all queries


/ping : test if server is online (returns current time)

Runs on Python 3.11 using FastAPI, SQLAlchemy, Alembic, SQLAdmin.

# Deployment

Clone repo:

```
git clone git@github.com:thesupercalifragilisticexpialidocious/cadastral.git
```

Switch to project directory, build and launch the image:
```
cd cadastral
docker build -t cadastral .
docker run --name cadastral -it -p 8000:8000 cadastral
```
