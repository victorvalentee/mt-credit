# mt-credit

## Overview

This application allows you to manage credit card data, providing an API that can retrieve and store credit card information in an SQLite database. 

This README will guide you through the steps of running the API and interacting with it.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
    - [Running the Test Suite](#running-the-test-suite)
    - [Running the Application](#running-the-application)
    - [Sending Requests](#sending-requests)

## Features

- Retrieve a list of all credit cards in the database.
- Retrieve a specific credit card by its card number.
- Store new credit card data in the database with proper data validation.
    - Securely store credit card data with encryption.
    - Comprehensive data validation triggers to ensure data integrity.

## Installation

To get started with mt-credit, follow these installation steps:

0. [Pre-requisites] For this guide to work, you should have the following programs installed:
    - [`git`](https://git-scm.com/downloads)
    - [`make`](https://www.gnu.org/software/make/#download)
    - [Docker](https://www.docker.com/)
    - [`curl`](https://curl.se/download.html) [Recommended]

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/victorvalentee/mt-credit.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mt-credit
    ```

3. Build the app Docker image:

    ```bash
    make build
    ```

## Usage

### Running the Test Suite

There are two test modules: one for the data validation and one for API routes / server functionality.

```bash
make test
```

### Running the Application:

This will fire up the Flask server in the container and foward it to the localhost.

**The application will be accessible at `http://localhost:5000`.**

```bash
make run
```

### Sending Requests

You can interact with the application by sending HTTP requests. I'm using `curl`, but you can do this with other tools such as [Postman](https://www.postman.com/) and some of these requests can be sent direclty from the browser:

- **List all credit cards:**

  ```bash
  curl http://localhost:5000/api/v1/credit-card
  ```

- **Retrieve a specific credit card by card number:**

  ```bash
  curl http://localhost:5000/api/v1/credit-card/1234567890123456
  ```

- **Store a new credit card:**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"exp_date": "2025-12-31", "holder_name": "John Doe", "card_number": "4111111111111111", "cvv": 123}' http://localhost:5000/api/v1/credit-card
  ```

## Architecture Overview
![Architecture Overview](docs/img/architecture_overview.png)

The architeture of this app can be divided into three sections:
1. Database
2. Functions
3. API

## Development Workflow

### First things first - The Database

I'll start the development process by defining the database schema and constraints. For the sake of speed, I'll use Python's built-in `sqlite3` database, although I think `postgres` would be a better choice in a production setting.

I'll make sure to include **data validation mechanisms in the schema itself**. In that way, software components and even programming languages can change in the future, but data quality will remain pristine.

#### In-Schema Data Validation
These are the data validations constraints enforced at schema level:
- Account holder name must have at least 3 characters.
- CVV must be NULL or have either 3 or 4 characters.
- Expiration date must be in the format YYYY-MM-DD.
- Expiration date must be in the future.
- Expiration date is set to the end of the month after insert.

#### Off-Schema Data Validation
Credit card number validation and encryption will be handled at API level.

### Next Step: API Functions
These are the functions that will be implemented at API level:
- List all credit cards
- Get credit card details (by id)
- Issue new credit card

All of these functions will be implemented using the TDD approach, and I'll focus on unit tests for now.

### Next Step: API Server (Flask)
Now that the API functions are in place, I'll start implementing the Flask server.

My main focus now will be to implement the three "routes":
- GET /api/v1/credit-card - list all credit cards
- GET /api/v1/credit-card/<id> - get credit card by id (card number)
- POST /api/v1/credit-card - store new credit card info

### Next Step: Integration Tests (Flask Server + API functions)
Now that both the API functions and the Flask server are implemented, I'll start creating tests for the routes.
These tests will ensure that:
1. The Flask server is working as expected
2. The http request/response logic is well integrated with the API backend functions

### Next Step: Card Number Validation
I'll incorporate the validation mechanism from `python-creditcard` library. This will probably change all card numbers I've been using so far.
