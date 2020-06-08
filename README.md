# Instagram clone
 
 <img src="./p.png">

## Description
At Moringa school you create a lot of projects (IPs, Mid-week projects) but you never know how those projects rate with your peers.
## User story

User stories
As a user, I would like to:

1. View posted projects and their details.
2. Post a project to be rated/reviewed.
3. Rate/ review other users' projects.
4. Search for projects.
5. View projects overall score.
6. View my profile page.
## BDD

| Behaviour | Input | Output |
| --------- | ------| ------ |
|On loading the app you see the landing page with login up form with a register link at the bottom of the form.| Clicking `sign up`.| You are redirected to a page where you enter your details and sign up then redirected to the login page.|
|Enter your username and password on the login page.| Clicking `login`. |You are redirected to a page where all the projects are visible.|
|Clicking any project's landing_page.|Mouse click.|You are redirected to a page showing just the project you clicked.|
|Clicking `RATE PROJECT` button.|Mouse click.|You are redirected to a page with a from where you fill your ratings under **content**, **design** and **usability** in the range of 1 to 10. |
|Clicking `VISIT SITE` button.|Mouse click.|You are redirected to the project's website.|
|Clicking the `New Project` link on the navbar. | Mouse click. |You are redirected to a page where you enter the details of your project then post.|
|Clicking the `Profile` link on the navbar.| Mouse click. | You are redirected to a page where you can view your profile or create your profile if you didn't have any.|
|||

## Setup and Installation  
To get the project .......  
#### Cloning the repository:  

##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
```  

##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 2.2.9](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
* [Git](for version control)
  
  
## Known Bugs  
* There are no known bugs currently,though i encountered many of it during deployment,but i finally managed 
## Support and contact details
call me on

<img src="https://bit.ly/2H4L6UZ" width="109" style="border-radius:50%;">:0798734442

<img src="https://bit.ly/383xk0Z" width="109" style="border-radius:50%;">:0778378174
 
 <img src="https://bit.ly/2Smueyp" width="109" style="border-radius:50%;">:nungari100@gmail.com

## License

[MIT License](LICENSE.md)
Copyright (c) [2020] [Joseph Nganga]
</a>