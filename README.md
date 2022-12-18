# International Spy Agency Platform
Welcome to the international spy agency.
In this document you will know all the necesary steps for up and running your platform

This README file covers local (development) and testing directions.

## Develpoment

You can import de Insomnia file to test the endpoint with a prepared environment

**INSOMNIA_ISA_PROJECT.json**

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

#### You can check the documentation at:
```
http://localhost:8000/docs/
```

Once the data is loaded, the users are these. 
You can access with email and password and for the admin seccion
you can access with the Boss credentials

NAME	EMAIL	PASS


| NAME   |      EMAIL      |  PASS |
|----------|:-------------:|------:|
|boss|	boss@isa.com| admin123-3	
hiteigth|hiteigth@isa.com|admin123-3
hitfive|hitfive@isa.com|admin123-3
hitfour|hitfour@isa.com|admin123-3
hitnine|hitnine@isa.com|admin123-3
hitone|hitone@isa.com|admin123-3
hitseven|hitseven@isa.com|admin123-3
hitsix|hitsix@isa.com|admin123-3
hitthree|hitthree@isa.com|admin123-3
hittwo|hittwo@isa.com|admin123-3
igniz|igniz@isa.com|admin123-3
jener|jener@isa.com|admin123-3
zero|zero@isa.com|admin123-3