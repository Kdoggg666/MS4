# Deployment

## Setup AWS S3

1. Create an account and login at [Amazon Web Services](https://aws.amazon.com/)
2. Search for s3 and setup your bucket, for more information on how to do this see this [S3 bucket tutorial](https://www.youtube.com/watch?v=v33Kl-Kx30o) or [Amazon S3 Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)
3. Setup a policy for your bucket that allows public access. for more information on how to do this see [Policies for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html)
4. Save your secret key variables that will be given to you after completing the previous steps in AWS. 
5. In your workspace run ```pip3 install boto3``` and ```pip3 install django-storages``` in the terminal to install the neccessary packages to connect to the s3 bucket.
6. In settings.py add "storages" to installed apps and add the Amazon Web Services s3 bucket settings to the static files settings.
7. Create a new file called "custom_storages.py" and setup the static files locations using s3boto3's storage classes as needed.
8. Add these changes to your github repositary by commiting and pushing them.

## Deploy to Heroku

GBGzoo was deployed to Heroku using the following steps:

1. Create an account and login to Heroku.
2. Click Create a new app.
3. Chose a name for your app and make sure its available.
4. Click Create app.
5. Click Resources.
6. Search for postgres in the search box and click on heroku postgres.
7. Select the free/hobby dev option and click provision. 
8. Make sure to save your new postgres DB URL as you will need this to connect to your database locally.
9. In your workspace terminal run ```python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json``` to backup your local database to a db.json file.
10. Install dj_database_url and psychopg2 by using the following commands in the terminal: ```pip3 install dj_database_url``` and ```pip3 install psycopg2```.
11. Add your new database url settings to settings.py being careful not to commit any changes that may leave your database url exposed in version control.
12. Migrate your db settings using the following command ```python3 manage.py migrate```.
13. Load your fixtures that you exported previously into your postgres db with the following command ```python3 manage.py loaddata db.json```.
14. Create a new superuser with the following command ```python3 manage.py createsuperuser```.
15. Install the gunicorn web server with the following command ```pip3 install gunicorn```.
16. Save a list of all required installed plugins by using ```pip3 freeze > requirements.txt```.
17. Create a Procfile to tell heroku what kind of app you are deploying by using ``echo web: gunicorn your_app_name.wsgi:application > Procfile``.
18. Go to your heroku dashboard and click on your app then click the deploy tab.
19. Connect your github repo in the deployment method section and click connect.
20. Enable automatic deployment under the automatic deploys section. 
21. Click the settings tab.
22. Click the reveal config vars.
23. Add your environment variables such as AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET and USE_AWS.

[Heroku Deployment Docs](https://devcenter.heroku.com/categories/deployment)

### Fork GbgZoo
1. Create a Github account or login [here](www.github.com)
2. On GitHub, go to [Kdoggg666/MS4](https://github.com/Kdoggg666/MS4/)
3. Look for the fork button, top right under your profile picture and click it

### Clone Kenan's Cook Book
1. Create a Github account or login [here](www.github.com)
2. Fork the project as detailed in the steps above
3. Click the code button    
4. Select to clone with HTTPS/SSH/GithubCli and click the copy icon on the right  
5. In your editor software eg. GitBash, GitPod, VSCode open the terminal    
6. Navigate to the destination which you want to be the destination for the clone
7. Type gitclone if you selected HTTPS or SSH and paste the copied code. If you used GithubCLi just paste the code you copied
8. Press Enter to create your clone