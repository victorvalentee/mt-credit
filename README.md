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
