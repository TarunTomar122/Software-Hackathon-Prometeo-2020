# Software-Hackathon-Prometeo-2020
This is our official web app related to smart health care under the Software Hackathon Event being organised at IIT Jodhpur in Prometeo(2020).

HomePageView

![Home](https://github.com/TarunTomar122/Software-Hackathon-Prometeo-2020/blob/master/ui/dashboard.PNG)

# Requirements
1.Django - To install django type 'pip install django' in cmd.
2.Crispy_Forms - To install Crispy_Forms type 'pip install crispy_forms' in cmd.
3.Django-allAuth - To install allAuth type 'pip install django-allauth' in cmd.

To run the server follow the given steps below: 
1. Open CMD in the forked local directory where manage.py file is located.
2. Type 'python manage.py makemigrations' and hit enter to create track of migrations.
3. Type 'python manage.py migrate' and hit enter to migrate the tracked files.
4. Type 'python manage.py runserver' and hit enter to run the server.
5. While the server is running, navigate to your favourite browser and navigate to 'localhost:9001' to view the webapp.

If you want to make a new admin id just hit following command - 
'python manage.py createsuperuser'
Then provide the asked information and you are all set up!

# Features - 
1. Councellors/Doctors/Researchers can Signup and fill in their required details and then they will have to wait till their details get verified by the admins of the app.

![profile](https://github.com/TarunTomar122/Software-Hackathon-Prometeo-2020/blob/master/ui/profile.PNG)

2. Registered Users after getting verified will have the ability to post some article on the site itself.

![post](https://github.com/TarunTomar122/Software-Hackathon-Prometeo-2020/blob/master/ui/createarticle.PNG)

3.Normal Users can have a look at the latest posts and articles from the registered ones.

![looking at posts](https://github.com/TarunTomar122/Software-Hackathon-Prometeo-2020/blob/master/ui/showarticles.PNG)

4.Users can also have a look at the registered Doctors and Users.

![doctors](https://github.com/TarunTomar122/Software-Hackathon-Prometeo-2020/blob/master/ui/doctors.PNG)

5.There is one Map View where users can see the nearest health centres and even fitness gyms.

![maps](https://github.com/TarunTomar122/Software-Hackathon-Prometeo-2020/blob/master/ui/maps.PNG)

# Some unimplemented Feature (due to time constraints) :
1. An AI based chatbot so that users can directly interact with it and get required informations.
2. Login for patiences so that they can directly chat with Councellors/Doctors.
3. Payment Features to be added for the same.
4. More Information about nearby health care centres and fitness gyms.



