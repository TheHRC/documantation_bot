# Use Python 3.9 image
FROM python:3.9

# Set working directory in the container
WORKDIR /rasa

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Rasa files into the container
COPY . .
COPY ./data /rasa/data
RUN rasa train

VOLUME /rasa
VOLUME /rasa/data
VOLUME /rasa/models

# Expose port 5005
EXPOSE 5005

# Command to run Rasa server
CMD ["rasa", "run", "-m", "/rasa/models", "--enable-api", "--cors", "*"]
#CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "endpoints.yml", "--log-file", "out.log", "--debug"]