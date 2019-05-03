## Insight DevOps Engineering Systems Puzzle Submission

See [this doc](</Original Instructions.md>) for rules and instructions

I partially completed the puzzle.

Here are some things I did:

- I set the flask app to run on port 5001, the port that is exposed in the docker environment/container

- I corrected the file path for that nginx config file in the redirect/mapping between container and host computer docker compose yaml


- I switched the port mapping from 80:8080 to 8080:80 for the nginx service in the docker compose yaml

  

Next up:

Figure out why a successfull form submission redirects to `<http://localhost%2Clocalhost:8080/success>` instead of `<http://localhost:8080/success>` 