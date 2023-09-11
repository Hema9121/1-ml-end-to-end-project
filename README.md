# 1-ml-end-to-end-project

----Start Machine Learning project.

----Software and account Requirement:

1.Github Account

2.Heroku Account

3.VS Code IDE

4.GIT cli

5.[GIT Documentation](https://git-scm.com/docs/gittutorial)

----what is docker?

Docker is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.

----What is Docker container used for?

Docker lets you build, test, and deploy applications quickly

Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime.

----What is a Docker image?

A Docker image is a file used to execute code in a Docker container. Docker images act as a set of instructions to build a Docker container, like a template. Docker images also act as the starting point when using Docker. An image is comparable to a snapshot in virtual machine (VM) environments.

----what is Heroku?

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

----what is continuous deployment and continuous integration?

Continuous Integration (CI) and Continuous Deployment (CD) are two important practices in software development that aim to improve the efficiency of software development and deployment.

Continuous Integration (CI) is the process of automatically building, testing, and validating changes to software code in a shared repository. By doing so, it allows developers to detect integration issues and bugs early in the development process. This practice encourages developers to test their code regularly and frequently, and it helps to improve the quality of the code in the repository.

Continuous Deployment (CD), on the other hand, is the practice of automatically deploying new changes to the codebase in a production environment. Once the code has been integrated and tested successfully, it is automatically deployed to a staging environment for further testing. If the code passes the staging environment, it is then deployed to a production environment where end-users can use it.

In summary, CI and CD work hand-in-hand to ensure that software code is integrated, tested, and deployed quickly and efficiently. CI helps to ensure that all changes to the codebase are continuously tested and validated, while CD ensures that those changes are safely and efficiently deployed to end-users. Together, these two practices help to increase the speed and quality of software development while reducing the risk of errors and issues.

----Creating conda environment===> conda create -p venv python==3.11 -y

----to activate the created conda env===>

conda activate venv/

OR

conda activate venv

----to install the requirements.txt file

pip install -r requirements.txt

----To Add files to git

git add .

OR

git add <file_name>

Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

----To check the git status

git status

----To check all version maintained by git

git log

----To create version/commit all changes by git

git commit -m "message

----To send version/changes to github

git push origin main

----To check remote url

git remote -v

----Git rollback? refers to the process of undoing changes made to a Git repository.

1. Git reset command: This is the most basic approach for rolling back to a previous commit. The git reset command is used to change the current head to the specified commit.

2. Git revert command: This method reverses a commit by creating a new commit with the inverse changes. This is a better option when changes have already been pushed to the repository.

----To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = hemasrinivasulu.ds@gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = <>

----BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .

Note: Image name for docker must be lowercase

----To list docker image

docker images

----Run docker image

docker run -p 5000:5000 -e PORT=5000 <image id>

----To check running container in docker

docker ps

----To stop docker conatiner

docker stop <container_id>

python setup.py install

----Install ipykernel

pip install ipykernel

----Data Drift: When your datset stats gets change we call it as data drift

----what is gunicorn?

Gunicorn (short for Green Unicorn) is a WSGI (Web Server Gateway Interface) HTTP server that is used to serve Python web applications. It is a pure-Python HTTP server that can run a number of concurrent HTTP requests and handle them efficiently. It is designed to work well with frameworks such as Django, Flask, Pyramid, and others. Gunicorn can handle more traffic than the default development server and can improve performance with multiple worker processes. It is widely used in production environments to serve Python web applications.