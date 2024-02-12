# proyecto0

The repository contains both the project's backend and frontend, in the back and front directories, respectively.

Each directory has its own Dockerfile. These are used to build independents Docker images for the backend and frontend.

The construction of the images is automated using Docker Compose. The `docker-compose.yml` file contains the configuration for both services.

## Build the application

To run the application, you will need to have Docker and Docker Compose installed on your machine. Then you can navigate to the project directory and use the following command in a Unix-like command prompt to build and run the application.

```bash
sudo docker pull ubuntu:latest;sudo docker-compose up
```

In a Windows command prompt, which must be ran as an administrator, you can use the following command:

```bash
docker pull ubuntu:latest && docker-compose up
```

## API documentation

The API was built using FastAPI. You can access the API documentation, created automatically using Swagger, by navigating to the following URL:

```bash
http://localhost:8000
```

## Access the application

Once the backend and frontend are running, you can access the application by opening a web browser and navigating to the following URL:

```bash
http://localhost:3000
```

The webpage will prompt you to enter a username and password. You can use the following credentials to log in:
**Username**: Janedoe
**Password**: John123
