# Define the Docker image name
DOCKER_IMAGE = mt-credit

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE) src/

# Run tests using pytest
test:
	@docker run -it --rm -e PYTHONPATH=/src/server $(DOCKER_IMAGE) sh -c "python3 server/create_encryption_key.py && PYTHONPATH=/src/server; pytest"

# Start the Flask server inside the Docker container
run:
	docker run -it --rm -p 5000:5000 $(DOCKER_IMAGE) python3 server/create_encryption_key.py; python3 server/app.py

# Generate and store cryptographic key into 'encryption.key' file
create_encryption_key:
	docker run -it --rm $(DOCKER_IMAGE) python3 server/create_encryption_key.py
