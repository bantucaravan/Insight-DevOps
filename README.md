## Insight DevOps Engineering Systems Puzzle Submission

See [this doc](</Original Instructions.md>) for rules and instructions of this puzzle challenge.

I am happy to say, I *completed the puzzle!* Feel free to clone this repo and run the server locally using the following command:

```
docker-compose up -d db; docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"; docker-compose up -d
```

The working page should be accessible at `http://localhost:8080/`

Shutdown the server using the following:

```
docker-compose down; docker image rm $(docker image ls -a -q)
```



### What I did

<u>**Solution**</u>: I set the flask app to run on port 5001, the port that is exposed in the docker environment/container

<u>**Problem**</u>: main page not displaying because correct nginx config file is not being used.
<u>**Solution**</u>: I corrected the file path in  file structure mapping between container and host computer in the docker compose yaml, so that location of correct config file was available.

<u>**Problem**</u>:  Main page not diplaying at `http://localhost:8080/`
<u>**Solution**</u>:  I switched the port mapping for the nginx service in the docker compose yaml from 80:8080 to 8080:80

<u>**Problem**</u>:  Form submission redirecting to `http://localhost%2Clocalhost:8080/success` instead of the correct `http://localhost:8080/success` 
<u>**Solution**</u>:  Deleting redundant and incorrect proxy server setting in the nginx config file

<u>**Problem**</u>:  Successful database update page shows a list of empty strings
<u>**Solution**</u>: The models.Items object being returned were being displayed as strings surrounded by angle brackets but being rendered as html, causing them to appear as empty strings because. Initially I repaced angle brackets with the appropriate html entities. Subsequently, I set up models.Items class to evaluate as a json str and used pandas to publish the current database state as a html table.

<u>**Other**</u>:
I made anumber of other changes while working on the above, which were likely critical although I never encountered their effects directly:

- I added an instruction to end the `scoped_session` in sqlalchemy at the end of every request using the `@app.after_request` decorator
- I added instance variables to the models.Items object used to query/insert into the database
- I changed `postgres://` to `postgresql://` in the sqlalchemy login syntax
- I added `enctype="multipart/form-data"` to the form tag of the index.html template