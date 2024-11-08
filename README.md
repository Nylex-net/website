# website
New redesign of the company website.  Code related to docking this application was adapted from londonappdeveloper at https://londonappdeveloper.com/deploying-django-with-docker-compose/.

The original website used Joomla.  Joomla is a CMS that's meant to help manage the site using a PHP server and mysql. However, it used a very old version of Joomla that went out of support. Plus the website was beginning to look outdated, and I worried that its performance would dissolve over time.
I spent some time learning how to configure Joomla on a Hyper-V running Ubuntu. But in the process of doing so, I decided I needed some extra flexability in how I design and configure this new website.

For the new Nylex website, I chose to use Django. If you're unfamiliar with Django, it is a python framework used to build and customize your own applications. When building the new website, I used the following languages and tools:
- Python
- Basic Web languages:
    - HTML
    - CSS
    - Javascript
- Django
- PostgreSQL
- Bootstrap 5
- nginx
- alpine
- Docker
- MS Entra ID (For secure Microsoft Login into admin portal).

I wanted to design this new application with the intention that it's secure, easy to manage and customize, and it runs fairly quickly. To accomplish this, I decided these were the best tools to use.

The main website data is in the folder titled "site."  The other folder was a test folder to get myself used to Django's framework.
