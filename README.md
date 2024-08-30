## Projector

# High Level Overview

Projector is an application that allows a user to create projects and delegate tasks to other users.

## Getting Started
1. Clone the following repository onto your local computer:
```
git clone https://github.com/austintkim/Projector.git
````

2. Run the following command in your terminal to install the relevant files and packages for this project:
```
pip install --upgrade pip
pip install - r requirements.txt
```

3. Create a Django superuser
```
python manage.py createsuperuser
```

4. Answer the prompts that populate in your terminal - it will ask for:
     - A **required** username
     - An optional email address
     - A **required** password
     - A **required** password confirmation

5. Run the following command to start your local development server:
```
python manage.py runserver
```

6. Type localhost:8000/admin/ into your browser to access Django admin:
    - Log in as a superuser using the credentials you input earlier
    - Feel free to add and remove Users and Groups as you please

7. Type localhost:8000 into your browser to access the application

8. Explore and enjoy!
