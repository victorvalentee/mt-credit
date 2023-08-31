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
