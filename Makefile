# Define the Docker image name
DOCKER_IMAGE = mt-credit

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE) src/

# Run tests using pytest
test:
	@docker run -it --rm $(DOCKER_IMAGE) sh -c "python3 server/create_encryption_key.py && pytest"

# Start the Flask server inside the Docker container
run:
	docker run -it --rm -p 5000:5000 $(DOCKER_IMAGE) sh -c "python3 server/create_encryption_key.py && python3 server/app.py"
