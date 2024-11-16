const shell = require('shelljs');
const path = require('path');

const IMAGE_FILE = 'askappreciationpage.tar';
const IMAGE_NAME = 'askappreciationpage';
const CONTAINER_NAME = 'askappreciationpage';

// Function to execute shell commands
function exec(command) {
  if (shell.exec(command).code !== 0) {
    shell.echo(`Error: Command failed - ${command}`);
    shell.exit(1);
  }
}

// Load the Docker image
shell.echo('Loading the Docker image...');
exec(`docker load -i ${IMAGE_FILE}`);

// Stop and remove any existing container
shell.echo('Stopping and removing existing container if it exists...');
exec(`docker rm -f ${CONTAINER_NAME} || true`);

// Run the Docker container
shell.echo('Running the Docker container...');
exec(`docker run -d -p 80:80 --name ${CONTAINER_NAME} ${IMAGE_NAME}`);

shell.echo('Your React app is now running at http://localhost');
