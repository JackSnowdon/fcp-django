# Project 4

## [Fight Club:Pro](https://fight-club-pro.herokuapp.com/)

Fight Club: Pro (FCP) is a Wolverhampton based wrestling promotion, celebrating its 10th year of business in September this year.
For years FCP existed underground, promoting wrestlers that rarely worked elsewhere, using online promotion and only running bi-monthly shows in first a cricket hut and then The Planet Nightclub In Wolverhampton.
Once they moved out of the Planet to Fixxon, they began to slowly rise from the underground, with the UK scene itself on an upward swing they started to sell out monthly shows with a reputation for incredible bouts becoming the talk of the scene,
Names like Trent Seven and Pete Dunne are entwined in FCP history, and this has led them growing to the one of the biggest promotions in the country, selling out their new home, The Hanger, on a monthly basis.
However, they still maintain an underground presence, with zero physical advertising and proactive use of social media they have slowly grown to an infamous level, with a dedicated worldwide fanbase.

I propose to build a site that helps bring everything together within FCP, free from social media algorithms to deliver prime content and ease of use to a dedicated, growing fanbase.

Currently FCP Has 4 main web presences (off social media)

Main Site: https://www.fightclubpro.co.uk/
BigCartel (Shop/Merch): https://fightclubpro.bigcartel.com/
Tickets: https://www.tickettailor.com/events/fightclubpro
OnDemand: https://vimeo.com/fightclubpro

Using the skills learnt I plan to integrate some of these services and providing a one stop show for all things FCP.
I will build the shop into the main website, keeping users on one site thus improving the UX.

## UX

FCP has a gritty, dark aesthetic to all aspects of their prestation and I have tried to bring this to life in this project. Choosing a dark background, with bright whites brought alive using a streak of gold that has been used in recent advertising. Because of this, all users will understand the concept of FCP and be immersed within their lore. 

All users will see the nav links on a fixed navbar, which also displays if a user is logged in and if they have anything in their cart. Handy back buttons display when users may require to take a step back.
Using bootstrap 4 I have made the website and images responsive down to 320pxs, which covers nearly all potential user screen widths. Using CSS Hover effects I have made the website have a slick feel, providing animations that fit with the graphic designs.

A particular thank you goes out to Robyn Golding, who provided the Roster Screen photos at a recent FCP event, it was a joy to build a roster page using beautifully captured portrait shots.

### User Stories

#### User 1 - Loyal FCP Fan
* Home page informs user of current FCP information
* Follows carousel link to shop
* Clicks on an object for further details 
* Adds to cart
* Follows through to checkout and pays (Stripe not accepting real payments, dummy codes can  be used)
* Order sent through, User can check order details and if shipped on profile

#### User 2 - Causal Wrestling Fan
* Home page informs user of current FCP information
* User navbar to head to roster page
* Notices roster split into 2, hover effects indicate further info upon click 
* Clicks on “Pete Dunne” (Most infamous wrestler present at FCP) and finds title history and Petes social media links
* Uses UX back button to take a step back to full roster page
* Clicks on tickets link to be taken to ticket selling page to check out new event
* May use shop to buy season ticket post first show 

#### User 3 - Potential Trainee Wrestler 
* Home page informs user of training school
* User clicks on carousel link or navbar link to training
* Reads responsive training information 
* Clicks on “Directions” link triggering a current location to training school google map link
“Fills out training form to be contacted 
“Browser displays sent message


### Wireframes

For some reason uploading the png files through C9 became an issue, thus why they are not in a neat folder like the rest of the project. Didn’t have time to fix this issue but they are still linked below!

* [Home](Home.png)
* [Shop](Shop.png)
* [Roster](Roster.png)
* [Training](Training.png)
* [Profile](Profile.png)

TO DO

## Features
### Existing Features

#### User Profiles
* Allows user to create a user (and the back end creates a profile object)
* Users can log in and out of the site
* When user is logged in, navbar reflects logged in user and allows access to profile
* Profile displays users orders

#### Navbar
* Fixed navbar to allow user easy access to website features and external sites
* Collapses for mobile

#### Home Page
* Carousel displays up to date information

#### Shop
* Allows user to browse products and add them to their cart.
* Each product has a detail view accessed via click

#### Cart
* Cart displays all products in users cart
* Total price and allows users to adjust quantity per product

#### Checkout
* Users must be logged in to access checkout page (This is so the order can saved to the users profile)
* Payment and order forms displayed under final cart review
* Dummy stripe codes used, checkout fully working

#### Training
* One page info sheeting for training at FCP
* Form at the bottom can be filled out for interested users
* Google maps link at top can use users current location

#### Footer
* Displays social links on the bottom of every page

#### Roster
* Alphabetically displays all wrestler objects
* Split into Team:FCP or schadenfreude 
* Each Wrestler object has a detail page, with full information, and social links only displaying if the field is full. 

### Future Features

#### Stock/Shop
* Implement a stock system, allowing admin to set amount of certain sizes per product object.
* Different objects for different products 
* Display Sold out items

#### Inbuilt ticket system
* Learn how to use stripe to take payments, and auto send out tickets using supplied data

## Technologies used 

- HTML5
  - The project uses HTML5 to build and style.
- CSS3
  - The project uses CSS3 to further style and hide/show content for game flow 
- Javascript 
  - The project uses Javascript for an interactive user experience and to control stripe
- [Bootstrap](https://getbootstrap.com/)
  - The project uses Bootstrap, helpers and the grid system
- [Google fonts](https://fonts.google.com/)
  - The project uses Google fonts for fonts
- [Python](https://www.python.org/)
  - The project uses Python to handle and run django
- [Django](https://www.djangoproject.com/)
  - The project uses the Django wireframe to speed up production and handle a lot of the python back end requests
- [FontAwesome](https://fontawesome.com)
  - The project uses font awesome icons
- [Stripe](https://stripe.com/gb)
  - The project uses stripe to handle payments
- [Heroku](https://heroku.com/)
  - The project uses Heroku for Postgres database and hosting
- Amazon Web Services S3 & Cloud 9
  - The project uses S3 for hosting of static images and Cloud 9 as my IDE



## Testing

I have mostly used automated testing on this project. Using Django unit tests and coverage to check my progress. My coverage percentages are listed below.

* Accounts: 77%
* Cart: 58%
* Checkout: 79%
* Home: 91%
* Roster: 98%
* Shop: 95%
* Training: 83%

To run these tests locally, use the command 
* “python3 manage.py test”
To test coverage, use the following commands 
* “coverage run --source='name of app' manage.py test”
* “coverage html” *posts report*
* Then open htmlcov and run index.html (preview in AWS C9)

I have manually tested how responsive the website is on different browsers and mobile screens. These are listed below:

* Google Chrome
* Microsoft Edge
* Safiri 
* Firefox
* Opera 
* 16.9” Laptop
* 10.1” Macbook Air
* Honor 10
* Iphone 7/8/x/xr
* Huawei Mate9
* Samsung s10/10+

All HTML has been tested on [W3C](https://validator.w3.org/) and all CSS has been tested on [Jigsaw](https://jigsaw.w3.org/css-validator/) with no errors. Python has been tested and refactored to PEP8 Standards. This project also uses Travis CI, which passes.

[![Build Status](https://travis-ci.org/JackSnowdon/fcp-django.svg?branch=master)](https://travis-ci.org/JackSnowdon/fcp-django)

## Deployment

The code is hosted on [Github](https://github.com/JackSnowdon/fcp-django) with a live version being hosted on [Heroku](https://fight-club-pro.herokuapp.com/) 

I built the project on AWS Cloud9, originally facing issues pushing to github, however I have used the following commands to overcome any issues:

* git config --global user.name "JackSnowdon"     
* git config --global user.email jacksnowdondrums@gmail.com
* git push --set-upstream origin master

To deploy locally:

* Clone repository or use git pull
* Create a virtual environment
* Use the command “sudo pip3 install -r requirements.txt”
* Create an “env.py” file, add it to your .gitignore file and set the following vars
 SECRET_KEY
 STRIPE_PUBLISHABLE
 STRIPE_SECRET
 DATABASE_URL
 EMAIL_ADDRESS
 EMAIL_PASSWORD
* To run use the command “python3 manage.py runserver $IP:$C9_PORT” or set in .bashrc ‘alias run="python3 manage.py runserver $IP:$C9_PORT"’

To deploy on Heroku:

* Create a new heroku project, set the env vars as listed above
* Create a Procfile containing the following web: gunicorn django_app.wsgi:application 
* Link the deploy using github, set either manual or automatic pulls.

The else/if statement within the settings.py file handles the debug setting and database location, this should help speed up deployment processes with minimal var setting.

## Credits

### Media
* I have been given permission to use content created by the wonderfully talented [Oli Sandler](https://www.facebook.com/ringsideperspective/) and [Robyn Golding](https://www.facebook.com/BeyondGorilla/), most of which is taken backstage at Fight Club: Pro, who have also given me permission to fully use any of their resources or imagery.
* These images are not for reuse without express permission of said owners 

### Content
* All FCP has been provided by Fight Club: Pro. 
* Further information for roster has been created either by me, or using [Cagematch](cagematch.com) to source title reigns/bios


### Acknowledgements 
* As ever the Code Institute Team for listening and helping
* Brian Macharia for jumping onboard as my mentor and helping my head focused
* Fight Club: Pro for existing and reaching their tenth year of business.
* Both Oli and Robyn for creating some incredible pieces of work that have been a pleasure to work with.
* Myself, for finally getting the course completed! 
