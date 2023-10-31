# doct-cbd3324-backend
Containerization and Container Delivery - Backend Application

## Structure

```
doct-cbd3324-backend/
├── app/
│   ├── main.py
│   ├── ...
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── helm/
│   │   ├── backend/
│   │   │   ├── charts/
│   │   │   │   ├── backend/
│   │   │   │   ├── ...
│   │   ├── values.yaml
│   ├── manifests/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   ├── ...
├── requirements.txt
├── tests/
│   ├── __init__.py
├── .gitignore
└── ...
```

## Dependencies Installation
```pip install -r requirements.txt```

## Run the application
```python3 app/main.py```

## Build and Run Docker Container
To build an image, use the command

```docker build -t apinyarr/dic-backend:test .```

To run a container, use the command

```docker run -d --rm --name dic-backend -p 8088:8088 -e MONGODB_HOST=host.docker.internal apinyarr/dic-backend:test```