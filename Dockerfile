# This is the docker image pea-chat
# It is based on the official jupyter notebook image
# It installs the required packages for the pea-chat project
# It copies the project files into the image
FROM jupyter/datascience-notebook:2023-06-01

WORKDIR /pea-chat

# Install required packages
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN PIP install -r requirements.txt

# Copy project files into the image
COPY . .

# Run the main.py script
CMD ["python", "main.py"]
