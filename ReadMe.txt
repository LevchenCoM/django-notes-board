https://github.com/LevchenCoM/django-notes-board

Hello! My name is Mykola and this is a short description of the project.

I. First of all - How to run project on your local computer. To run project, please, follow this steps:

  1. Create new virtualenv for this project;
  2. Install all libraries from requirements.txt;
  3. Run your new virtualenv, go to project folder and write this command in your terminal:
          For Windows: python manage.py migrate
          For Linux:   python3 manage.py migrate
  4. Then write this command for run django server
          For Windows: python manage.py runserver
          For Linux:   python3 manage.py runserver       
  4. Congratulations! Now your server is run! Go to "http://127.0.0.1:8000/".

II. Now let's talk about the possibilities of the application.

    1. To see all notes go to home directory ("http://127.0.0.1:8000/");
    2. First of all, you need to register ("/register/"), or login (go to "/login" and use login: admin, pass: admin);
    3. Use navigation menu on the top for add new note to the board:
          Add note - adds new note to the site.
    4. On note page, you can edit your media - change title, descriptione or status. Go to "All notes" using navigation menu, then click on "Edit" button.

Thank you! Hope you will like my project!
Mykola.
