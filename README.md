# Django Basics Demo  
This is a blog project, written in Django and wrapped in a Docker container, created for Women Coding Community mentoring sessions.

## References
- Django Documentation - [Getting Started](https://docs.djangoproject.com/en/5.1/intro/)
- [Example database design](https://miro.com/app/board/uXjVLDp3NSc=/?share_link_id=491242328578)
- [Example API design](https://github.com/dkellycollins/lulu-cao-collab)

## Steps 
### Set Up Environment
  - Copy and paste the Dockerfile 
  - Use the VS Code Docker extension to run a container for the project
  - `pipenv shell`
  - `pipenv install django`
### Scaffold a Project and an App
  - `django-admin startproject blog_project`
  - Move generated code to the root folder
  - `pipenv run python manage.py startapp blog_app`
  - `pipenv run python manage.py runserver`
### Set Up a View and a URL
  - Add code to `blog_app/views.py`
  - Add code to `blog_app/urls.py`
  - Add code to `blog_project/urls.py`
  - View the app at `http://127.0.0.1:8000/blog_app/`
### Set Up a Model
  - Use Dbeaver to connect to `django-basics-demo/db.sqlite3`
  - Add code to `blog_app/models.py`
  - `pipenv run python manage.py makemigrations`
  - `pipenv run python manage.py migrate`
### Set Up an Admin Site
  - `pipenv run python manage.py createsuperuser`
  - Add code to `blog_app/admin.py`
  - View the admin site at `http://127.0.0.1:8000/admin/`
### Debugging
  - `pipenv run python manage.py check`
  - [`pipenv run python manage.py shell`](https://docs.djangoproject.com/en/5.1/intro/tutorial02/#playing-with-the-api)
### Version Control 
  - Copy and paste the `.gitignore`