# This is the docker image pea-chat
# It is based on the official jupyter notebook image
# It installs the required packages for the pea-chat project
# It copies the project files into the image
FROM jupyter/datascience-notebook:2023-06-13

WORKDIR /pea-chat

# Copy project files into the image
COPY . .

# Install required packages
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Run with a loop to keep the container running in dockerfile with shell
ENTRYPOINT ["sh", "fake_runner.sh"]

