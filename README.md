I was not able to complete the puzzle: 

Here are some things I did:

- I setthe flask app to run on port 5001, the port the is exposed in the docker environment/container


-I corrected the file path of config file redirect/mapping between container and the host computer for the nginx service in the docker compose yaml


- I changed to index.html file location in app.py to be set within the templates folder

- I switched the port mapping from 80:8080 to 8080:80 for the nginx service in the docker compose yaml
