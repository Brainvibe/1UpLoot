# 1UpLoot

Live version [here](https://brainvibe.github.io/travelportugal/)

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

* Register Account
  * If the user decides to use the app, they're able to create an account and access all app features. All passwords are encrypted in the database, to enhance security.

* Login
  * Simple form where the user can use their created credentials in the "Register Account" page to login and able to use the app.

* Contact
  * Provides a simple way for the user to be able to contact 1UP Loot. It will show a simple form where the users can submit-request for information/feedback/features. User can close the form, and return to the page and keep browsing. EmailJS was used for the email send functionality.

## Features to add

* Detailed search system
* Wishlist
* Forum
* Share feature

## Wireframes

Need to update this

* [Desktop](https://github.com/Brainvibe/travelportugal/blob/master/wireframes/desktop.png)
* [Mobile](https://github.com/Brainvibe/travelportugal/blob/master/wireframes/mobile.png)
* [Tablet](https://github.com/Brainvibe/travelportugal/blob/master/wireframes/tablet.png)

## Technologies Used

* **HTML**
  * Used to create the main structure of the website.

* **CSS**
  * Used to style and layout the website.

* **Flask**
  * Point of communication with mongo db

* **Python**
  * Language used for back-end1

* **[Mongodb](https://cloud.mongodb.com)**
  * Database used for this project

* **[Materialize](https://materializecss.com/)**
  * Framework used

* **[JQuery](https://jquery.com)**
  * The project uses **JQuery** to simplify DOM manipulation.

* **[Font Awesome](https://fontawesome.com/)**
  * All footer icons.

* **[Materialize Icons](https://materializecss.com/icons.html)**
  * All icons in the webpage except the footer are from Materialize

* **[Heroku](https://www.heroku.com/)**
  * Used to host the live website.

* **[Google Fonts](https://fonts.google.com/)**
  * "Covered By Your Grace" for logo and "Open Sans Condensed" with two font weight varieties for the rest of the page.

* **[EmailJS](https://www.emailjs.com/)**
  * Adds the ability to send emails from contact form.

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
    * Edge
    * Chrome
    * Firefox
    * Safari

## Deployment

Write deployment

## Credits

### Media

* Main photos were downloaded from [Broforce Game](https://broforcegame.com/)

### Acknowledgements

* Auto-hide collapse menu code from [here](https://stackoverflow.com/questions/42401606/how-to-hide-collapsible-bootstrap-4-navbar-on-click).
* Smooth Scrolling from [W3schools](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp).
* Webp fallback image load from [CSS-tricks](https://css-tricks.com/using-webp-images/)

As usual I want to thank my mentor *Victor Miclovich* for his great knowledge and experience with valuable feedback in our mentoring sessions.

## Disclaimer

### All content for educational use only
