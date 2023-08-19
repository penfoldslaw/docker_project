import pandas as pd
from sqlalchemy import create_engine
from faker import Faker

# Create a Faker generator
fake = Faker()

# Generate dummy data
num_records = 100  # Adjust the number of records you want to generate
dummy_data = []

for _ in range(num_records):
    name = fake.name()
    email = fake.email()
    age = fake.random_int(min=18, max=80)
    dummy_data.append((name, email, age))

# Create a pandas DataFrame from the dummy data
columns = ['name', 'email', 'age']
df = pd.DataFrame(dummy_data, columns=columns)

# Database connection settings (SQLite in this example)
db_path = '/app/database.db'  # desired database file path
db_engine = create_engine(f'sqlite:///{db_path}')

# Insert data into the database table
table_name = 'dummy_table'  # desired table name
df.to_sql(table_name, db_engine, index=False, if_exists='replace')

print(f'Dummy data loaded into {table_name} in {db_path}')
