# 1UpLoot

Live version [here](https://oneuploot.herokuapp.com/)

## Index

* [Project description](#project-description)
* [UX](#ux)
* [Features](#features)
* [Wireframes](#wireframes)
* [Technologies](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Disclaimer](#disclaimer)

## Project Description

1UP Loot is a web application, designed for physical game collectors to plan, track and organize their collections. All information the user creates is saved into a database, so they can easily access their collections on every device. All major platforms are supported including retro gaming systems and all genres.
Users can add, search, edit, delete their games into the web app. Each game entry has several fields like: Game Name, Game Platform, Game Genre, Pickup Date, Game Store, Game Price, Current Value, Game condition and Game Image.
With Game Image users can add a url 200x200 hosted cover image of their choice.

## UX

### Who is it for

* Avid Game collectors that have big collections for several game systems.
* New collectors that are starting game collecting.
* General users that want a place to organize and manage their games library.

### User Stories

* As a user/collector, I want to easy navigate and find the information I need quickly.
* As a collector, I want to add all information possible I have about my games.
* As a user/collector, I want to be able to use my collection on all my devices.
* As a collector, I want to be able to edit information on all my games, so I can update their current value, prices or vendors.
* As a user/collector, I want to be able to remove any games from my library, in case I sell or trade any of them.
* As a user/collector, I want to be able to filter my games per game system or genres, so I can have a overview on what I already have for each system.
* As a collector, I want to have the option to add retro gaming systems, in case I decide to collect for those systems.
* As a user/collector, I want to have all major platforms available to me so I can add all games from my collection.

* Add more stories with session implemented -----

## Features

### Existing Features

* Navbar
  * Allows user to navigate easily through the different sections of the page.

* About
  * A simple introduction to the app, so the user can have a brief idea on what it does without overloading with lof of information. They have a sign up button below if they decide to discover more about it.

* Features section
  * Gives a brief description on the app's features. The user can have an overview idea on what they can do with the app, in a simple way with easy to read icons for each feature with a little describtion below.

* Footer
  * Provides links to the relevant social websites.

* Login
  * Simple form where the user can use their created credentials in the "Register Account" page to login and able to use the app.

* Register Account
  * If the user decides to use the app, they're able to create an account and access all app features. All passwords are encrypted in the database, to enhance security.

* User Session
  * When the user is logged in, they're able to create their collection, Add/Edit/Delete/Modify their games, in a more private and personalized way.
  
## Features left to implement

As I develop my skills I would like to implement more features in this app like:

* Detailed search system
  * Would be useful for users with bigger collections to be able to have access to a more detailed search.
* Upload game images
  * Ability to upload images, instead of using URLs.
* Wishlist
  * A feature for collectors to help them find the games they don't have in their collection.
* Share feature
  * Ability to share their private collections to fellow collectors through the app with a public generated link with read only permissions.
* Community/Forum
  * A blog/forum for all users and collectors curious about the subject, can join and discuss their favourite hobby.

## Wireframes

Need to update this

* [Desktop](https://github.com/Brainvibe/travelportugal/blob/master/wireframes/desktop.png)
* [Mobile](https://github.com/Brainvibe/travelportugal/blob/master/wireframes/mobile.png)
* [Tablet](https://github.com/Brainvibe/travelportugal/blob/master/wireframes/tablet.png)

## Technologies Used

* **HTML**
  * The project uses HTML to structure the DOM.

* **CSS**
  * Used to style webpages.

* **[Flask](http://flask.palletsprojects.com/en/1.1.x/)**
  * Used to generate pages, generate dynamic links, and content within the application.

* **[Python 3](https://www.python.org/)**
  * Python is an interpreted, high-level, general-purpose programming language, used to integrate Flask in this project and CRUD tasks.

* **[Mongodb](https://cloud.mongodb.com)**
  * Database used for this project, for CRUD (create, read, update & delete) tasks.

* **[PyMongo](https://api.mongodb.com/python/current)**
  * used to connect and transfer data to and from MongoDB.

* **[Materialize](https://materializecss.com/)**
  * A responsive CSS framework based on Material Design by Google.

* **[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)**
  * Flask extension that provides bcrypt hashing, used to encrypt all users passwords in the database.

* **[JQuery](https://jquery.com)**
  * The project uses JQuery to initialize Materialize CSS components

* **[Font Awesome](https://fontawesome.com/)**
  * Used for footer icons.

* **[Materialize Icons](https://materializecss.com/icons.html)**
  * All icons in the webpage except the footer which are from Font Awesome.

* **[Heroku](https://www.heroku.com/)**
  * Used to deploy the live website.

* **[Google Fonts](https://fonts.google.com/)**
  * "Covered By Your Grace" for logo and "Open Sans Condensed" with two font weight variants for the rest of the page.

## Testing

* **W3C Validation Services**
  * Markup Validation Service
    * Test result

  * W3C Link Checker
    * No errors, all links working properly. Only two links were not able to be tested by the tool. Here's the console log:

            info Line: 333 https://www.facebook.com/
            Status: (N/A) Forbidden by robots.txt
            The link was not checked due to robots exclusion rules. Check the link manually. 
           
            info Line: 338 https://www.twitter.com/
            Status: (N/A) Forbidden by robots.txt
            The link was not checked due to robots exclusion rules. Check the link manually. 

    * Both links were tested manually and working.

  * CSS Validation service
    * Test result

* **JSHint**
  * test results

* **Google dev tools**
  * Audit tool
    * Accessibility - test result

    * SEO - test result

      * Best Practices  
            - test result

    * Performance
      * test result

* **Non-automated testing:**

  * Links:

    * Checked all links especially the footer social icons, to make sure they were opening on a new tab correctly.

  * Contact form:

    * Tried to submit the empty form and verify that an error message about the required fields appears

    * Tried to submit the form with an invalid email address and verify that a relevant error message appears

    * Tried to submit the form with all inputs valid and verify that a success message appears with a alert message.

* **Tested Devices**
  * Apart from using the dev tools to see if the site was responsive across different resolutions I've tested all features on the following devices:
    * One Plus 7 pro
    * Fire HD 10
    * Ipad
    * Iphone 11
    * Macbook Pro 13"
    * Windows Desktop

* **Browsers**
  * To ensure browser compatibility I've tested all features above on the following browsers:
    * Chrome
    * Firefox
    * Safari

## Deployment

### Running this project locally

In order to deploy this project locally you'll need the following:

* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/downloads)
* [Python 3](https://www.python.org/)
* [MongoDB Atlas](https://www.mongodb.com/) account
* [pip](https://pypi.org/project/pip/)

After you have everything installed, first clone the project from GitHub:

* Go to [GitHub repository](https://github.com/Brainvibe/1UpLoot).
* Under the repository name, click the green "Clone or download" button.
* In the Clone with HTTPs section, copy the clone URL for the repository.
* Open the terminal in your IDE.
* Change the current working directory to the location where you want the cloned directory to be made.
* Copy paste the following command:

```git clone https://github.com/Legaeldan/milestone-3```

The repository is now cloned.

* Install the requirements needed to run the project from the terminal using the following command:

```pip3 install -r requirements.txt```

* After pip installs all packages, just type ```python app.py``` in the terminal and it will now run locally.

### Deployment to Heroku

To deploy this project to Heroku, follow these steps:

* Log into [Heroku](https://dashboard.heroku.com/).
* From the main dashboard, select the **New** dropdown, then select **Create new app**.
* Give you app a unique name, and select the region you wish to deploy to.
* After the app is created, select **Deploy** from the top of the page, and scroll down to **Deployment Method**.
* Select **GitHub** as the method of deployment.
* Log in using your **Github credentials.**
* Select your username, and search for the reposity in the **repo-name** box.
* Select **Connect** on the repository you wish to connect to.
* Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**
* After the application is built, select **Settings** from the top of the page.
* Select **Reveal Config Vars**.
* Add the config keys for **IP**, **PORT**, **MONGO_URI**, **MONGO_DBNAME**, and **SECRET_KEY**
* Select **More** from the top right of the page, and select **Restart all dynos**.

## Credits

### Media

* Main photos were downloaded from [Broforce Game](https://broforcegame.com/)

### Acknowledgements

* Auto-hide collapse menu code from [here](https://stackoverflow.com/questions/42401606/how-to-hide-collapsible-bootstrap-4-navbar-on-click).
* Smooth Scrolling from [W3schools](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp).
* Webp fallback image load from [CSS-tricks](https://css-tricks.com/using-webp-images/)
* Login system based on [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE)

As usual I want to thank my mentor *Victor Miclovich* for his great knowledge and experience with valuable feedback in our mentoring sessions.

## Disclaimer

### All content for educational use only
