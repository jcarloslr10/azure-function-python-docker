# BlobTrigger - Python

The `BlobTrigger` makes it incredibly easy to react to new Blobs inside of Azure Blob Storage. This sample demonstrates a simple use case of processing data from a given Blob using Python.

## How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `raw/{name}.csv` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name.

## Prerequisites

## Installation

To install dependencies run the following command:

```
pip install -r requirements.txt
```

## Local environment

This project includes a Docker setup for the local environments.

### Azure Storage Account using Azurite

Azurite is an open source Azure Storage API compatible server that allows you to easily try Azure Storage in a local environment. Run the following command to get the container up and running:

```
docker-compose up --build
```
