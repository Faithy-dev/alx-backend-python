# Python Generators - 0x00

## 📌 Objective

Create a data ingestion script using Python and MySQL that:
- Sets up a MySQL database called `ALX_prodev`
- Creates a `user_data` table with proper schema
- Seeds the table with user data from a `CSV` file
- Uses Python functions to manage database operations cleanly

---

## 🗃️ Schema: `user_data`

| Field     | Type     | Description                      |
|-----------|----------|----------------------------------|
| user_id   | UUID     | Primary key, indexed             |
| name      | VARCHAR  | Full name of the user (required) |
| email     | VARCHAR  | Email of the user (required)     |
| age       | DECIMAL  | Age of the user (required)       |

---

## 📂 Files

- `seed.py`: Python script to connect, create, and seed the database
- `user_data.csv`: CSV file with user data
- `0-main.py`: Test script provided to validate database setup
- `README.md`: Project documentation

---

## 🔧 Functions

The following functions are implemented in `seed.py`:

```python
connect_db() → connection
create_database(connection)
connect_to_prodev() → connection
create_table(connection)
insert_data(connection, csv_file)
