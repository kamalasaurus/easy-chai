# Use the nvidia/cuda container as a base image 
FROM nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04

# Set the working directory
WORKDIR /app

# Install Python 3.12
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.12 python3.12-dev python3.12-distutils && \
    ln -s /usr/bin/python3.12 /usr/bin/python && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --upgrade pip && \
    pip install git+https://github.com/chaidiscovery/chai-lab.git
    # pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the application
CMD ["bash", "app.py"]