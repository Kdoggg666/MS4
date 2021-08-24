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