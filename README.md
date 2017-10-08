# National OA Ceremonies Training System
Ceremonies are hard. It's not uncommon for you, (the ceremonies adviser,) to get a call driving to a fellowship. "I can't make it" says Allowat Sakima. You hand another arrowman the script binder and he tries his best to memorize the script before sundown. Sounds familiar, doesn't it? NOACTS is the premier training platform for Ceremonialists across the country.

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
## Installing Locally
#### 1. Clone the project:
    $ git clone git@github.com:Tenderfoot14/National-OA-Ceremonies-Training-System.git
    $ cd National-OA-Ceremonies-Training-System
    
#### 2. Create and initialize virtualenv for the project:
    $ virtualenv venv
    $ pip install -r requirements.txt
    
#### 3. Run the development server:
    $ ./manage.py runserver
    
#### 4. Open [http://localhost:5000](http://localhost:5000)
    
## Deploying
### Deploying on Heroku
#### 1. Open the local app directory:
    cd National-OA-Ceremonies-Training-System
#### 2. Create a new Heroku app for the app:
    $ heroku create
#### 3. Upload the local repository to Heroku:
    $ git push heroku master
#### 4. Ensure a web dyno is provisioned for the app:
    $ heroku ps:scale web=1
#### 5. Open the app:
    $ heroku open