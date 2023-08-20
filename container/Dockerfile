FROM python:3.10.12

# Setting the working directory in the container
WORKDIR /app

#Copy the requirements file into the container
COPY requirements.txt /app/

#Any needed packages specified in the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copycing the rest of the application into the container
COPY  . /app/

EXPOSE 5000

#The command that run Python script

CMD ["python", "dummydata.py"]