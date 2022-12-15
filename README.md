# International Spy Agency Platform
Welcome to the international spy agency.
In this document you will know all the necesary steps for up and running your platform

This README file covers local (development) and testing directions.

## Develpoment

### Run with docker

#### Requirements

- Install [Docker and Docker compose](https://docs.docker.com/compose/install/)
- Notice docker-related files are placed under `local` folder.

#### Create an `.env` file in the root of the project

Fill the `.env` with the correct values (It will be send by email)

#### In the root of this project

#### Build the image

```bash
make build
```

#### Start the service

```bash
make up
```

#### Stop the service

```bash
make down
```

### Run migrations

```bash
make migrate
```

### Create superuser

```bash
make createsuperuser
```