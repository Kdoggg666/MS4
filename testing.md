# Manual Testing for GbgZoo
## Testing Responsiveness
#### Am I Responsive
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629808952/images/albums/MS4/responsive/amiresponsive_umdpws.png" width="450"/>

### iPhone
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629808952/images/albums/MS4/responsive/iphonex_nml2lt.png" width="250"/>

### iPad
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629808952/images/albums/MS4/responsive/ipad_b6pon8.png" width="350"/>  

### PixelXL
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629808952/images/albums/MS4/responsive/pixelXL_imdj3v.png" width="350"/> 

## Testing user stories as a shopper:
## User Story 1
- I want to quickly find a new pet reptile or amphibian.

### Action
Navigate to animals page by clicking the button on the home page or in the Nav bar.

### Expectation
The animals page displays a list of all animlas paginated in groups of 6.

### Result
The page loads correctly, the nav link works and results are displayed paginated in groups of 6. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629647955/images/albums/MS4/features%20images/all_animals_page_utboxb.png" width="650"/>

## User Story 2
- I want to be able to easily sort and search for a specific animal.

### Action
Navigate to animals page by clicking the button on the home page or in the Nav bar then click one of the filter butttons or type an animal name in the search bar.

### Expectation
The animals page displays a list of all animlas that match the filter button or search term. 

### Result
The page loads correctly, The animals page displays a list of all animlas that match the filter button or search term. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629809544/images/albums/MS4/testing/search_python_c4gqb0.png" width="650"/>

## User Story 3
- I want to easily find care information about my animals.

### Action
Navigate to care guides page by clicking the button on the home page or in the Nav bar.

### Expectation
The care guides page will display a list of all animlas paginated in groups of 6. Clicking on an animal will take you to a care guide for that animal. If there is no care guide a toast message will notify you that there is no care guide yet for the animal.

### Result
The care guides page displays a list of all animlas paginated in groups of 6. Clicking on an animal takes you to a care guide for that animal. If there is no care guide a toast message notifies you that there is no care guide yet for the animal.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629809828/images/albums/MS4/testing/care_working_tiousy.png" width="650"/>  

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629809829/images/albums/MS4/testing/no_care_guide_jlhaoy.png" width="650"/>

## User Story 4
- I want to be able to login to the site.

### Action
Clicking the login button on the nav bar.

### Expectation
Clicking the login button on the nav bar will take you to the login page and you will be able to successfully login.
### Result
Clicking the login button on the nav bar takes you to the login page and you successfully login. A toast message is shown to inform you of successful login.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629810141/images/albums/MS4/testing/login_success_ikbnxw.png" width="650"/>

## User Story 5
- I want to be able to create a profile.

### Action
Click the register button on the nav bar.

### Expectation
Clicking the register button will allow me to make an account and profile on the website. On the My profile page I want to be able to add/edit my delivery details. 

### Result
Clicking the register button allows me to make an account and profile on the website. On the My profile page I am able to add/edit my delivery details. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641108/images/albums/MS4/features%20images/sign_up_hff1le.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629641385/images/albums/MS4/features%20images/profile_wg5eau.png" width="650"/>

## User Story 6
- I want to be able to add a review for an animal.

### Action
Click "Review this Animal" on the animal details page.

### Expectation
Clicking "Review this Animal" will take me to a form where I can review the specific animal. 

### Result
Clicking "Review this Animal" takes me to the animal review form where I review the specific animal. After the form is submitted my review is publically available for other users to see. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629810698/images/albums/MS4/testing/add_review_form_bcqivn.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629810698/images/albums/MS4/testing/rating_added_mexyi1.png" width="650"/>

## User Story 7
- I want to be able to Edit and Delete my reviews.

### Action
Clicking the Edit or Delete button on a review.

### Expectation
Clicking the Edit or Delete button on a review will allow me to edit/delete my review.

### Result
Clicking the Edit button takes me to a form where I can edit my review. Clicking delete opens a confirmation dialog box and asks me to confirm. Once deleted the review is gone and once edited the review is changed and the last edited field is updated. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811180/images/albums/MS4/testing/review_update_lo4q6k.png" width="650"/>
  
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811180/images/albums/MS4/testing/review_delete_zxgrh5.png" width="650"/>
  
<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811179/images/albums/MS4/testing/review_delete_success_ersh7q.png" width="650"/>

## User Story 8
- I want to be able to add animals to a shopping cart which keeps a running total of all the animals in my cart.

### Action
Adding an animal to cart with the add to cart button, quantity selection optional. 

### Expectation
When I click "ADD TO CART" the animal with the quantity I have selected will added to my cart and the running total will be updated accordingly. 

### Result
Clicking "ADD TO CART" on the animal with the quantity I want added the animal to my cart and the running total was updated accordingly.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811473/images/albums/MS4/testing/add_to_cart_fhbu46.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811479/images/albums/MS4/testing/cart_full_ejtrap.png" width="650"/>

## User Story 9
- I want to see my previous orders and user information on my profile page.

### Action
Click "My Profile" on the nav bar.

### Expectation
Clicking "My Profile" will take me to my profile page where my information and previous orders will be displayed.

### Result
Clicking "My Profile" takes me to my profile page where my information and previous orders are displayed.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811805/images/albums/MS4/testing/my_profile_l0c3bs.png" width="650"/>

## User Story 9
- I want to be able to easily purchase my animal using secure checkout functionality using my credit/debit card.

### Action
Clicking secure checkout on the shopping cart page. 

### Expectation
I will be taken to a checkout form that will have my details autocompleted if previously saved, I will have the option to save them if not. I will be able to put in my credit card details and complete the purchase. 

### Result
Upon clicking secure checkout I am taken to a checkout form that has my details autocompleted. I am able to put in my credit card details(Stripe test card number in this case) and complete the purchase. The purchase is completed successfully and I am given the success toast message with my confirmation. I am sent a confirmation email with the order details.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629640844/images/albums/MS4/features%20images/checkout_confiim_yrsap6.png" width="650"/>

## User Story 10
- I want to be able to select the quantity of animals when adding them to my cart.

### Action
Clicking the + button to incriment the quantity of animal before clicking add to cart.

### Expectation
Upon adding animal(s) to my cart, the shopping cart will be updated with the correct ammount of animals.

### Result
Upon adding animal(s) to my cart, the shopping cart is updated with the correct ammount of animals.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629811473/images/albums/MS4/testing/add_to_cart_fhbu46.png" width="650"/>

## User Story 11
- I want to be able to recover my password if I have lost it.

### Action
Clicking forgot my password on login form. 

### Expectation
I will be able to reset my password if its lost. I will recieve an email with a link to reset my password and be able to change it.

### Result
I recieve an email with a link to reset my password and was able to change it.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629812372/images/albums/MS4/testing/password_reset_iohtfn.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629812372/images/albums/MS4/testing/change_password_qu7usf.png" width="650"/>

## Testing user stories as the site Administrator:
## User Story 1
- I want to be able to add new animals.

### Action
Clicking add animal on the site admin tab on the nav bar.

### Expectation
I will be taken to a form where I can add the animal, after I have submited the animal will be available on the site. 

### Result
I am taken to the add animal form where I added the animal, after I submited the animal was available on the site. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629812818/images/albums/MS4/testing/add_animal_yqtyfp.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629812820/images/albums/MS4/testing/ball_python_u77xr9.png" width="650"/>

## User Story 2
- I want to edit existing animals.

### Action
Clicking edit animal on the animal details page

### Expectation
I will be taken to a form where I can edit the animal, after I have submited the edited animal will be available on the site. 

### Result
I am taken to the edit animal form where I then edited the animal, after I submited the animal was available on the site. 

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629812994/images/albums/MS4/testing/edit_ballpythonbutton_c9rf3w.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629812995/images/albums/MS4/testing/edit_form_jmpoyl.png" width="650"/>

## User Story 3
- I want to be able to add new care guides.

### Action
Click "Add care guide" on animals that do not have a care guide.

### Expectation
I will be able to add a care guide for an animal which will then be available on the site after submitting.

### Result
I am able to add a care guide for an animal which is now available on the site after submitting.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813235/images/albums/MS4/testing/add_care_guide_zk1hfz.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813234/images/albums/MS4/testing/add_care_form_opdjek.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813327/images/albums/MS4/testing/success_care_guide_ok32hi.png" width="650"/>

## User Story 4
- I want to edit existing care guides.

### Action
Clicking "Edit Care Guide" on the animal care details page.

### Expectation
I will be able to edit a care guide for an animal which will then be available in its edited version on the site after submitting.

### Result
I am able to edit a care guide for an animal which is now available in its edited version on the site after submitting.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813528/images/albums/MS4/testing/edit_care_guide_button_ccplo0.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813528/images/albums/MS4/testing/edit_care_guide_lvwvno.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813527/images/albums/MS4/testing/edit_care_success_whjabl.png" width="650"/>

## User Story 5
- I want to be able to remove reviews if need be.

### Action
Clicking delete on a review.

### Expectation
I will be prompted with a confirmation modal to ensure I want to delete the review. Once deleted the review will no longer be available on the site.

### Result
I am prompted with a confirmation modal to ensure I want to delete the review. Once deleted the review was no longer available on the site.

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813804/images/albums/MS4/testing/delete_review_button_fohgey.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813804/images/albums/MS4/testing/delete_review_modal_fbh0dh.png" width="650"/>

<img src="https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813804/images/albums/MS4/testing/review_delete_success_c85dzi.png" width="650"/>

## Code Validation
### HTML
GbgZoo validated HTML with only 2 warnings about type="text/javascript" not being needed.  
[W3C Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fgbgzoo.herokuapp.com%2F)
![HTML Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629813998/images/albums/MS4/validation/html_kkxcfl.png)


### CSS
My CSS file validated without any errors on the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator)
![CSS Validation](https://res.cloudinary.com/dyxe4g62g/image/upload/v1629814177/images/albums/MS4/validation/css_hawlck.png)


### PEP8 Compliance
My Site passed PEP8 compliance at [PEP8 Checker](http://pep8online.com/checkresult)
![PEP8 Validation]()

### JSHint Validation
As the only javascript in this project is from bootstrap, stripe and the boutique ado walkthrough project I didnt think validation was neccessary. 
 
## Known Bugs
I unfortunately ran out of time to fix the remaining bugs, however they do not break any functionality or cause a bad user experience in my opinion.  
- The star rating average which displays stars based on the reviews by customers shows the average stars of all reviews and not specific to the animal in question. I ran out of time and could not fix this by the submission deadline.
- There is a bug with my DB settings where it will not see the if statement relating to which DB to use. Everytime I open my workspace I need to run the command "unset DATABASES_URL" even though there is no enviroment variable in my development environment.
- 
- 