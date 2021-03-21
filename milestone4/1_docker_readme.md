# Docker instruction

## Steps to run the docker image
1. Please download `team9_interface.tar` along with this instruction, and place in a directory that is easy to access.
2. Make sure Docker is running.
2. Navigate to the directory containing `team9_interface.tar` using terminal/command line.
3. Enter the following command to load the image: `docker load < team9_interface.tar`
4. Enter the following command to connect to local host, **the port number is 9999**: `docker run -p 9999:9999 team9_interface`
5. Open a browser and enter the following address: `http://localhost:9999/`

*Ta-Da! You now have access to our corpus*