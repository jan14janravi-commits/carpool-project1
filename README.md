carpool project

Inchara R Javgal-4MC23IS046
Janhavu TR-4MC23IS047
Harshith S-4MC23IS042
Manya B-4MC23IS058


Setup Instructions

Follow these steps to set up and run the application locally.

Clone the repository
Open your terminal and clone the project, then navigate into the main project directory:

git clone [https://github.com/anishjrall/Micro-project-fullstack-15.git cd Micro-project-fullstack-15/contactbook_project](https://github.com/jan14janravi-commits/carpool-project1)

Install dependencies
Install the necessary Python packages, including Django 


Run migrations
Apply the database schema changes to set up the necessary tables (including user authentication and contacts model):

python manage.py makemigrations python manage.py migrate

Run server
Start the local development server:

python manage.py runserver
