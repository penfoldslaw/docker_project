import time
import pandas as pd
from sqlalchemy import create_engine
from faker import Faker
from flask import Flask, jsonify

# Create a Flask app
app = Flask(__name__)

# Create a Faker generator
fake = Faker()

# Database connection settings (SQLite in this example)
db_path = '/app/database.db'  # desired database file path
db_engine = create_engine(f'sqlite:///{db_path}')

# Table name
table_name = 'dummy_table'  # desired table name

# Route to fetch data from the database and return as JSON
@app.route('/get_data')
def get_data():
    # Fetch data from the database
    data = pd.read_sql(f'SELECT * FROM {table_name}', db_engine)
    
    # Convert the DataFrame to a dictionary for JSON serialization
    data_dict = data.to_dict(orient='records')
    
    return jsonify(data_dict)

# Loop to keep generating and inserting data
while True:
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

    # Insert data into the database table
    df.to_sql(table_name, db_engine, index=False, if_exists='replace')

    print(f'Dummy data loaded into {table_name} in {db_path}')

    # Wait for 60 seconds before generating and inserting data again
    time.sleep(60)

    if __name__ == '__main__':
    # Run the Flask app
        app.run(host='0.0.0.0', port=5000)
