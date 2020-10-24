# Dockerize RESTful API using Flask + Gunicorn

For any Linux-like machine installed docker

Run the command to build the image

```docker build -t rest .```

Run this command to run as a container. Please note that adding `-it` flag for easier terminate the process via Ctrl+C. Or you may need to terminate the container by `docker stop container_id` in another CLI window.

```docker run -it -p 8080:8080 rest```
