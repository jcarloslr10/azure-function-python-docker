# BlobTrigger - Python

The `BlobTrigger` makes it incredibly easy to react to new Blobs inside of Azure Blob Storage. This sample demonstrates a simple use case of processing data from a given Blob using Python.

## How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `raw/{name}.csv` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name.

## Prerequisites

* [Docker](https://docs.docker.com/get-docker) (required)
* [Python 3.7](https://www.python.org/downloads/release/python-370) (needed to run the function not using Docker)
* [Azure Function Core Tools v3](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v3%2Cwindows%2Ccsharp%2Cportal%2Cbash) (needed to run the function not using Docker)

## Installation & dependencies

If you are getting the application up and running not using Docker, first create a Python virtual environment as follows:

```
python -m venv .venv
.venv\scripts\activate
```

To install the dependencies run the following command:

```
pip install -r requirements.txt
```

## Local environment

This project includes a Docker setup for the local environments, although you can also run the function not using Docker.

### Azure Storage Account using Azurite (required)

Azurite is an open source Azure Storage API compatible server that allows you to easily try Azure Storage in a local environment. Run the following command located in the root folder to get the container up and running:

```
docker-compose up --build
```

### Python function

The above command also execute the function. If you want to run the function not using Docker, you need to comment out the following service in the docker-compose.yml file to prevent it from running:

```
  # software_developer_expertise_etl:
  #   container_name: "software_developer_expertise_etl"
  #   build:
  #     context: .
  #     dockerfile: Dockerfile
  #   environment:
  #     FUNCTIONS_WORKER_RUNTIME": python
  #     AzureWebJobsStorage: DefaultEndpointsProtocol=http...
  #   restart: always
```

Then, you just have to run the following command located in the root folder:

```
func start
```
