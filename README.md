
## Language

- Python v3.10.5

## Framework

- Django v4.1.3
- Djangorestframework v3.14.0

## Database

- MySQL


## API Reference
### Authentication

|ACTIONS|HTTP METHODS|ENDPOINTS|
|-----------------|---|--------------|
|REGISTER FOR AN ACCOUNT|POST|/api/register|
|LOGIN WITH AN ACCOUNT| POST |/api/login|
|LOGOUT FROM AN ACCOUNT|POST|/api/logout|

### JWT Authenticated Endpoints


- get all profiles

```bash
  GET               /app/profile  
```

- get friend list

```bash
  GET               /app/friend  
```
- get all user list

```bash
  GET               /app/user  
```

- search user by username in URL
```bash
                    /app/user/?search=  
```
- invite user
```bash
  POST              /invite/<int:pk>  
```
- decline user request
```bash
  POST              /decline/<int:pk>  
```


#### CRUD Child Data

|ACTIONS|HTTP METHODS|ENDPOINTS|
|-----------------|----------------------|--------------|
|GET ALL CHILD DATA |GET| /user/child/|
|CREATE CHILD DATA|POST|/user/parent/{pk}/child/|
|RETRIEVE/MODIFY INDIVIDUAL CHILD DATA|GET, PUT, PATCH, DELETE|/user/child/{id}|


  [Documentation](https://www.dropbox.com)


#### Repsitory Structure



## Installation
## Step 1 - Download and Install Python
- Download [python v3.10.5](https://www.python.org/downloads/release/python-3104/)
- Run the executable file as an administrator
- Add python path to environment variables
## Step 2 - Repository
- Clone the following [repository](https://github.com/mohammadjayeed/DRF_FriendSystem_v2.git),
```bash
  git clone  https://github.com/mohammadjayeed/DRF_FriendSystem_v2
```
## Step 3 - Virtual Environment
- Make a virtual environment with the following command
```bash
  python -m venv venv
```
-  Activate the virtual environment with the command
```bash
  venv/scripts/activate
```
## Step 4 - Dependencies
- Install dependencies
```bash
  pip install -r requirement.txt
```
## Step 5 - Migrations
- Run the following command which creates migrations based on models or change of models
```bash
  python manage.py makemigrations
```
- Run the following command to apply it to the database
```bash
  python manage.py migrate
```
## Step 6 - Superuser
- Run the following command to create a superuser to access admin panel by adding the required information. We will require username and password to login to the admin panel
```bash
  python manage.py createsuperuser
```
## Step 7 - Start App
- Start the application by typing the following command
```bash
  python manage.py runserver
```