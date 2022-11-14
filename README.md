
## Language

- Python v3.10.5

## Framework

- Django v4.1.3
- Djangorestframework v3.14.0

## Database

- MySQL


## API Reference
### __Authentication__
#### __Refresh Token__ while logging out, should be provided in the request body as per JWT convention
#### __Login Endpoint__ will provide token which is needed in the header to get authenticated

|ACTIONS|HTTP METHODS|ENDPOINTS|
|-----------------|---|--------------|
|REGISTER FOR AN ACCOUNT|POST|/api/register|
|LOGIN WITH AN ACCOUNT| POST |/api/login|
|LOGOUT FROM AN ACCOUNT|POST|/api/logout|

### __JWT Authenticated Endpoints__

```bash
get profile data of all users

  GET     
        /app/user  

search user by username 

        /app/user/?search= 

get friend list of authenticated user

  GET     
        /app/friend

invite a particular authenticated user

  GET       
        /app/user/{user-id}/invites/

decline request from a user with his user id assuming he sent a request to the authenticated user

  POST     
        /app/user/{user-id}/declines/ 

accepts request from a user : his user id assuming he sent a request to the authenticated user

  POST
        /app/user/{user-id}/accepts/

view posts created by the authenticated user

  GET      
        /feed/self-posts

view authenticated user friend posts like, comment

  GET       
        /feed/friends-posts

like/unlike friend posts with post id

  POST     
        /feed/friends-posts/{post-id}/likes

comment on friend posts with post id

  POST     
        /feed/friends-posts/{post-id}/comments
```

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
## Step 5 - Configure MySQL
- Configure MySQL
```bash
  configure MySQL client and make necessary changes in database section of the project settings folder
```
## Step 6 - Migrations
- Run the following command which creates migrations based on models or change of models
```bash
  python manage.py makemigrations
```
- Run the following command to apply it to the database
```bash
  python manage.py migrate
```
## Step 7 - Superuser
- Run the following command to create a superuser to access admin panel by adding the required information. We will require username and password to login to the admin panel
```bash
  python manage.py createsuperuser
```
## Step 8 - Start App
- Start the application by typing the following command
```bash
  python manage.py runserver
```