
# Library API

This project is a Flask-based web application with PostgreSQL as its database. The application supports Docker for containerized deployment and includes Swagger for API documentation.

## Table of Contents

- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [Accessing Swagger API Documentation](#accessing-swagger-api-documentation)
- [Running Unit Tests](#running-unit-tests)

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Python 3.12+** (if running locally)

---

## Environment Variables

Create a `.env` file in the root directory and configure the following variables:

```dotenv
# Configuration
DB_HOST=db
DB_PORT=5432
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

FLASK_ENV=development

ORIGINS=remote_origin


```

---

## Running the Application

### Using Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/adolfo9castro/library-api.git
   cd library-api
   ```

2. Build and run the containers:

   ```bash
   docker-compose up --build
   ```

3. The application should now be running at:

   - **API**: [http://localhost:5000](http://localhost:5000)

4. To stop the containers:

   ```bash
   docker-compose down
   ```

---

## Accessing Swagger API Documentation

Swagger is available for testing and exploring the API endpoints.

1. After starting the application, navigate to:

   - **Swagger UI**: [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

2. Use the interactive interface to explore and test the endpoints.

---

## Running Unit Tests

Unit tests for this application are written with `pytest`.

1. Ensure dependencies are installed (if running locally):

   ```bash
   pip install -r requirements.txt
   ```

2. Run the tests:

   ```bash
   pytest
   ```

3. Check the results in your terminal.
