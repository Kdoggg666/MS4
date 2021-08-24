# GbgZoo.se

Welcome to GbgZoo.se. For my fourth milestone project I have chosen to make an online store for my friend's petstore. Combining the ability to purchase reptiles as well as get detailed care guides for each animal. The site is made with django and features full login/account functionality, CRUD functionality for administrators and full payments with stripe. The goal is to sell reptiles and promote the petstore as well as offer care guides for the users who have purchased an animal. 

A live preview of the website can be found [Here](https://gbgzoo.herokuapp.com/) 

## Table of Contents

1. [UX](#ux)

2. [Wireframes](#wireframes)

3. [Database](#db)

4. [Features](#features)

5. [Technologies Used](#technologies)

6. [Testing](#testing)

7. [Deployment](#deploy)

8. [Credits](#credits)

9. [Acknowledgements](#acknowledgements)

10. [Disclaimer](#disclaimer)


<a name="ux"></a> 
## UX

### Site Goals

The goal of GbgZoo.se is to offer a large selection of reptiles and amphibians for users to purchase as well as provide them with detailed care information. It is also the goal to make it easy for users to check their past orders and update their information easily. The site should be easy to navigate as well as aesthetically pleasing. Administrators should be able to easily add products and care guides.  
 
### User Stories
#### As a Shopper: 
- I want to quickly find a new pet reptile or amphibian.
- I want to be able to easily sort and search for a specific animal.
- I want to easily find care information about my animals.
- I want to be able to login to the site.
- I want to be able to create a profile.
- I want to be able to add a review for an animal.
- I want to be able to Edit and Delete my reviews.
- I want to be able to add animals to a shopping cart which keeps a running total of all the animals in my cart.  
- I want to see my previous orders and user information on my profile page.
- I want to be able to easily purchase my animal using secure checkout functionality using my credit/debit card.
- I want to be able to select the quantity of animals when adding them to my cart.
- I want to be able to recover my password if I have lost it.

#### As the site Administrator:
- I want to be able to add new animals.
- I want to edit existing animals.
- I want to be able to add new care guides.
- I want to edit existing care guides.
- I want to be able to remove reviews if need be.

<a name="wireframes"></a>
### Wireframes

To see all wireframes created in the UX stage [Click Here!](/wireframes.md)

<a name="db"></a>
### Database Overview
For this project I have used Sqlite in production and postgres for the deployed version.

#### Database structure
To see the full relational database structure [Click Here!](/database_structure.md)

<a name="features"></a>
## Features

### Home Page
- The home page displays a large image with two articles directing the user to the animal selection as well as the care guide selection. 
- The footer shows information about the business as well as links to follow the store on social media. 
- The search bar allows users to search easily for animals and care guides.
 
  
![Home page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629647886/images/albums/MS4/features%20images/home_page_fwngrr.png "Home Page" )

### All Animals Page
- Animals are dynamically generated from the relational database and displayed in groups of 6 entries using pagination.
- Buttons on the page allow the user to sort results by Snakes, Lizards, Amphibians or all animals.  

![All Animals Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629647955/images/albums/MS4/features%20images/all_animals_page_utboxb.png "All Animals Page")

### Care Guides Page
- Animals are dynamically generated from the relational database and displayed in groups of 6 entries using pagination just the same as the all animals page.
- Clicking on an animal will take you to the care guide for the specific animal.  

![Care Guides Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629647955/images/albums/MS4/features%20images/all_animals_page_utboxb.png "Care Guides Page")

### Animal Details Page
- Animals details are dynamically generated from the relational database and displayed to the user in an easy to read layout.
- On this page the user can select the quantity of animal and add it to the cart.
- Users can access the care guide for the specific animal if there is a care guide for that animal. If there is no care guide the user will not see a button for the guide.
- Users will see reviews for the selected animal on the bottom of the page. If no review exists the user will not see the review section. Users may only edit and delete reviews that they have created. Suerusers can delete and edit any reviews.
- Users can click "Review this animal to leave a review on the selected animal"
- Super users will see a button to edit the animal and delete the animal. Regular users will not see this option. 
- Once a user adds to the cart or leaves a review they will recieve a toast message showing information relating to their actions.   
- Users can also see the average rating by other users on the specific animal page. 

![Animal Details Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629807406/images/albums/MS4/features%20images/animal_details_page_fksfk0.png "Animal Details Page")

### Care Details Page
- Care details are dynamically generated from the relational database and displayed to the user in an easy to read layout.
- The user is provided with detailed care information on the selected animal as well as a link to an external article.
- Users will also have the option to see the animal in the online store.
- Super users will see a button to edit and delete the care guide. 
   
![Care Details Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629636023/images/albums/MS4/features%20images/care_details_kzmn6z.png "Care Details Page")

### Shopping Cart Page
- The shopping cart page displays which animals the user has added to their cart and allows them to change the quantity or remove items while displaying a running total of the price.
- Users can either proceed to secure checkout or go back to the online store. 
- Whenever a user adds a product to their cart the shopping cart icon in the upper right hand side of the nav bar will display the running total in Swedish Krona. 

![Shopping Cart Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629636154/images/albums/MS4/features%20images/shopping_cart_jcczhc.png "Shopping Cart Page")

### Secure Checkout Page
- The secure checkout page shows a summary of the customers order as well as a form to fill in customer details and shipping information. 
- The user has the option to login or create an account in order to save order information as well as customer details for easy checkout. 
- The user has a check box asking to save delivery information to their profile. 
- The user is shown a payment area to add their credit card information using stripe securely. 
- once all information is added the user can click checkout and the order will be completed. The user will be notified via toast message that the order is successfull and will receieve an email confirmation. 
- after checkout the customer will be redirected to a checkout confirmation page with the order summary.

![Secure Checkout Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629636397/images/albums/MS4/features%20images/secure_checkout_aelsux.png "Secure Checkout Page")

### Checkout Confirmation Page
- The checkout confirmation page shows a summary of the customers order as well as confirmation that the order was processed. 

![Checkout Confirmation Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629640844/images/albums/MS4/features%20images/checkout_confiim_yrsap6.png "Checkout Confirmation Page")

### Login Page
- The login page requires a users name and password. A user can also register from here if they do not have an account.

![Login Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641010/images/albums/MS4/features%20images/login_gnthpo.png "Login Page")

### Registration Page
- The signup page will allow a user to register a profile by filling in the required fields. The backend is handled by allauth. 

![Login Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641108/images/albums/MS4/features%20images/sign_up_hff1le.png "Login Page")

### Logout Page
- The logout page asks the user to confirm that they would like to logout and clears the user from cookies. 

![Logout Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641240/images/albums/MS4/features%20images/signout_xale1w.png "Logout Page")

### Profile Page
- The profile page shows a form prepopulated with the users information if provided as well as the option to update the information. 
- The profile page also shows previous orders and a link to the order summary.

![Profile Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641385/images/albums/MS4/features%20images/profile_wg5eau.png "Profile Page")

### Add Animal Page
- The add animal page allows superusers the ability to add new animals via a form that is connected to the animal model. once the form is saved the animal will appear on the list of animals in the store.


![Add Animal Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641532/images/albums/MS4/features%20images/add_animal_a5yncn.png "Add Animal Page")

### Add Care Guide Page
- The add care guide page allows superusers the ability to add new care guides for animals via a form that is connected to the care model. Once the form is saved the care guide will appear on the list of care guides in the care guides section as well as a button on the animal details page.


![Add Care Guide Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641733/images/albums/MS4/features%20images/care_guide_xtge78.png "Add Care Guide Page")

### Add Review Page
- The add reveiw page is accessed by clicking review this animal on the animal details page. The user will be presented with a form to review the animal. Once the form is submitted the review will be visiable on the animal reviewed's details page to all users. Only super users and the user that created the review will be able to delete or edit reviews.


![Add Review Page](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641953/images/albums/MS4/features%20images/add_review_crzvrp.png "Add Review Page")

### Admin Panel
- The admin panel is accessed via the /admin/ url and super users can login and edit users, models and database entries.  
- All models have been registered on the admin panel.


![Admin Panel](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629642112/images/albums/MS4/features%20images/admin_panel_pzycyr.png "Admin Panel")

### Features Left to Implement
- User profile picture which displays in the navbar when logged in and on user reviews. 
- Model and page for animal care products. 
- Option to select home delivery or collect in store. 
- Custom error screens such as 500, 404 etc. Django defaults are currently being used. 
- Remove unused fields in models, Ive had many issues with migration so I didn't want to mess with that so close to submission as it works currently and don't have time to fix if an issue crops up.

<a name="technologies"></a>
## Technologies Used
 
- **Postgres** - Postgres was used as the DB for the live version of the site.
- **Sqlite3** - Sqlite was used to store and access database items in development.  
- **Django** - Used as web app framework to make creating the app faster and easier.   
- **Heroku** - Heroku was used to host the live version of this app.  
- **Github** - Github was used for storing my code and version control.    
- **Gitpod** - I used Gitpod to code the site as well as push updates to Github.    
- **Python** - Python 3 was used for the backend code to run the app and logic.    
- **Prettier Code** - I used Beautify to keep my code properly indented and easily readable.
- **Flake8** - I used Flake8 to keep my python code properly indented and easily readable as well as PeP8 compliant.    
- **HTML5** - The core of the site was built with HTML version 5.  
- **CSS** - CSS was used to style the website and define fonts and layout.  
- **Bootstrap** - Bootstrap was used for layout and alignment with the grid system, forms and inputs as well as pagination.   
- **JavaScript** - JavaScript was used to provide logic and funtionality to certain elements such as the running total for the checkout cart.  
- **Jquery** - Jquery was used to write the click functions that append extra inputs to the forms as well as to enable Bootstrap selectors and sidenav.   
- **Font Awesome** - Social Media icons from Font Awesome.  
- **Google Chrome** - The website was built and tested in google Chrome.  
- **Google Fonts** - Bitter, Akaya and Cormorant from Google.  
- **Auto close tag** - self explanitory.  
- **HTML hint** - for faster coding.  
- **Cloudinary** - Hosting images to make the site load faster.
- **Apple Safari** - Used for testing.  
- **Mozilla Firefox** - Used for testing.  
- **Opera** - Used for testing.  
- **Amazon Web Services S3** - AWS S3 was used for the static files for deployment.

<a name="testing"></a>
## Testing

The testing section of the README can be found [Here](testing.md)

<a name="deploy"></a>
## Deployment
GbgZoo.se was deployed to [Heroku](https://www.heroku.com/)

The deployment section of the README can be found [Here](deploy.md)

<a name="credits"></a>
## Credits

### Code
- Majority of the code was taken and modified from the Code Institute Boutique Ado walkthrough project which I relied heavily on. Other code taken and modified from the Bootstrap, Django and Python documentation. 

### Content
- Care guide text taken and modified from [Reptiles Magazine](https://www.reptilesmagazine.com/) and [Reptile Advisor](https://www.reptileadvisor.com)



#### Photo Credits
I have credited all the photos that I have used however as users can upload their own images I can not ensure that they own the rights to those images as well as I can not credit them here. 

### Website
- Favicon: https://commons.wikimedia.org/wiki/File:Snake_icon.svg  
- Website Background: https://www.popsci.com/uploads/2019/03/18/MAWBLTWLVA5IIBN34YJYSH2L5A.jpg 

### Snakes
- Kenyan Boa - https://dubiaroaches.com/blogs/snake-care/kenyan-sand-boa-care-sheet
- Boa Constrictor - https://www.twinkl.de/teaching-wiki/boa-constrictor
- Ball Python - https://fineartamerica.com/featured/5-ball-python-python-regius-david-kenny.html
- Western Hognose Snake - https://reptilehow.com/western-hognose-snake-price/
- Garter Snake - https://sv.m.wikipedia.org/wiki/Fil:Coast_Garter_Snake.jpg
- Burmese Python - https://www.sciencemag.org/news/2018/03/tracking-elusive-burmese-python-dna-clues-dirt

### Lizards
- Bearded Dragon - https://www.everythingreptiles.com/bearded-dragon/
- Collared Lizard - https://tucsonherpsociety.org/amphibians-reptiles/lizards/eastern-collared-lizard/
- Ackie Monitor - https://www.everythingreptiles.com/ackie-monitor-care-sheet/
- Leopard Gecko - https://www.reptilecentre.com/blog/2020/02/how-to-care-for-a-leopard-gecko/
- Frilled Dragon - https://www.reptilesmagazine.com/frilled-lizard-care-sheet/
- Crested Gecko - https://www.reptilecentre.com/info-crested-gecko-care-sheet

### Amphibians
- Red Eyed Tree Frog - https://www.nationalgeographic.com/animals/amphibians/facts/red-eyed-tree-frog

<a name="acknowledgements"></a>
## Acknowledgements

I received inspiration for this project from 
- [The Real GBGZoo.se](https://www.gbgzoo.se)


<a name="disclaimer"></a>
## Disclaimer
This project is for educational purposes only and will not be used for commercial use. All media has been credited and any similarities to other companies/websites/applications are purely unintentional.  






