# Test Project

## Problem Description

Create an app in Django project that will upload a PDF file and store uploaded the file in some physical location and all metadata of the file in the model

- The file should be transferred in Base64 format from front-end
- back-end should generate a file from Base64 and store it in some folder and all metadata of the file in the model.
- create a page where we can see a list of all uploaded files(Back-end should return file object in Base64 format)
- by clicking any file browser should open that file in new window. Make sure you do not expose file location e.g in browser window user should not see 'http://127.0.0.1:8000/media/abc/file_name.pdf' instead of any other URL    

Note: Do not store Base64 data in any model

## Instructions to Run

- Create and activate a virtualenv with Python 3.8.0
- Clone this repo
- cd into the repo
- Add a `.env` file following the example at `.env.example`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

## Endpoints

- Upload files: http://127.0.0.1:8000/file/
- View list of files: http://127.0.0.1:8000/


**Used Django with JQuery, Bootstrap and SQLite**
