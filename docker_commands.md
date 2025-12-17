# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash
docker volume create fastapi-db  
```

### Seed the volume (via Docker Desktop)

```bash

```

## Server 1

### Build the image

```bash
docker build -t server_1:v1 .\server_1\  
```

### Run the container

```bash
docker run -d  --name server_1 -p 8000:8000 -v fastapi-db:/app/db server_1:v1
```

## Server 2

### Build the image

```bash
docker build -t server_2:v1 .\server_2\
```

### Run the container

```bash
docker run -d  --name server_2 -p 8001:8000 -v fastapi-db:/app/db server_2:v1
```

