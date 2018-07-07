
Chat 1.0
-=-=-=-=-

Creating a Docker container
===========================

Note: Please make sure that Docker is installed correctly and run "docker network create ChatNet".

In order to create a Docker container, use the create.bat batch file. The correct command line is: create <container_name>.

Example: create ChatBot1
The batch file will create the container, get all the requirements and install the correct version of python (3.6) on the container.


Compiling and running the application
=====================================

Keeping in mind the name of the Docker container made earlier, use the batch file chat.bat. The correct command line is: chat <container_name>.

Example: chat ChatBot1
The batch file will run the required command on the container, compiling and running the application. At the end, you will be returned to the command prompt and not left in the container's command bash prompt.

* * *

Have fun and enjoy!