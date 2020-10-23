
FROM python:3.8.6-slim-buster

# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# Create the working directory (and set it as the working directory)
RUN mkdir -p /home/flask/app/application
WORKDIR /home/flask/app

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY requirements.txt /home/flask/app
RUN pip3 install --no-cache-dir -r requirements.txt


# Copy the source code into the container
RUN chown -R flask:flaskgroup /home/flask
COPY . /home/flask/app

RUN chmod a+x /home/flask/app/entrypoint.sh

# Add folder to PYTHONPATH so packages can be found
ENV PYTHONPATH "${PYTHONPATH}://home/flask/app"

USER flask

CMD /home/flask/app/entrypoint.sh
