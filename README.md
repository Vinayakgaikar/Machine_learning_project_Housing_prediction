# ML_Project_deployment
## Start Machine Learning Project

The goal of this project, to built a model for analyzing and predict the housing price in California. It will 
help in checking the median house value by using input features like total rooms in house, housing 
median age, population, households etc. 

Application url:
[HousingPredictor](https://mncmiq2utb.us-east-1.awsapprunner.com/)

### Software and Accout Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code](https://code.visualstudio.com/download)
4. [GIT CLI](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)                                                                                                           

### Steps
1. `git status` To check the git status 
2. `git add . or git add <file_name>` To Add files to git
3. `git commit -m "message"` To create version/commit all changes by git
4. `git push origin main` To send version/changes to github
5. 'git log' To check all version maintained by git
5. `git remote -v` To check remote url 

### Virtual environment and requirements.txt
1. Creating conda virtual env
`conda create -p <env_name> python==3.9 -y` -p to create venv in project folder itself
2. Activate venv
`conda activate <env_name>/`
3. Creating requirement.txt file
`pip freeze > requirements.txt`
4. To install requirements.txt
`pip install -r requirements.txt`

### To setpup CI/CD pipeline in heroku we need following information
1. HEROKU_EMAIL: vinayakgaikar1998@gmail.com
2. HEROKU_API_KEY: <API_KEY>
3. HEROKU_APP_NAME: testingapps12

### BUILD DOCKER IMAGE
1. `docker build -t <image_name>:<tag_name> .`
> image_name should be in lower case and tag_name generally use 'latest'
2. `docker images` To list Docker Image and get IMAGE_ID
3. Run Docker Image
   `docker run -p 5000:5000 -e PORT=5000 <IMAGE_ID>`
4. `docker ps` To check running container in docker
5. `docker stop <container_id>` to stop docker container 


## Notes
> If adding '-e .' then we must have setup.py file in root directory. This will create <custom_pkg_name>-egg.info file for every package which contains "__init__.py" file.
> Where "-e ." executed inside "requirements.txt". Its actually lunching the "setup.py" hence the egg.info file will get created for all custom packages.
