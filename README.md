# GbgZoo.se

Welcome to GbgZoo.se. For my fourth milestone project I have chosen to make an online store for my friend's petstore. Combining the ability to purchase reptiles as well as get detailed care guides for each animal. The site is made with django and features full login/account functionality, CRUD functionality for administrators and full payments with stripe. The goal is to sell reptiles and promote the petstore as well as offer care guides for the users who have purchased an animal. 

A live preview of the website can be found [Here](https://gbgzoo.herokuapp.com/) 

## Table of Contents

1. [UX](#ux)

2. [Wireframes](#wireframes)

3. [Features](#features)

4. [Technologies Used](#technologies)

5. [Testing](#testing)

6. [Deployment](#deploy)

7. [Credits](#credits)

8. [Acknowledgements](#acknowledgements)

9. [Disclaimer](#disclaimer)


<a name="ux"></a> 
## UX

### Site Goals

The goal of GbgZoo.se is to offer a large selection of reptiels and amphibians for users to purchase as well as provide them with detailed care information. It is also the goal to make it easy for users to check their past orders and update their information easily. The site should be easy to navigate as well as aesthetically pleasing. Administrators should be able to easily add products and care guides.  
 
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


### Database Overview
For this project I have used Sqlite in production and postgres for the deployed version.

#### Database structure
