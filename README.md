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

#### 1. Build the image

```bash
make build
```

#### 2. Start the service

```bash
make up
```

#### 3. Run migrations

```bash
make migrate
```

#### 4. Load data

```bash
make load_data
```

### Reconstruct the data base

#### Stop the service

```bash
make down
```

#### Stop the service

```bash
docker volume rm justo-backend-challenge_postgres_data
```

#### Repeat the step 1 so on and so forth

### Create superuser

```bash
make createsuperuser
```