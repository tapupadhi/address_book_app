# address_book_app
This is an address book application where API users can create, update and delete addresses.

# Prerequisite:
Make sure python is installed in your machine.

# Database used:
SQLite


# Steps to run this Project:
  1. clone the project: "git clone git@github.com:tapupadhi/address_book_app.git"
  2. navigate inside to your cloned directory
  3. create virtual environment and configured your python interpreter
    **Steps to create virtual environment:**
      go to folder containing project
      python3 -m venv evn_name
      source evn_name/bin/activate
      now you will be able to see (env_name) infront of the each terminal line
  4. Now you can install required libraries in virtual environment: "pip3 install -r requirement.txt"
  5. once all set run this command:  "uvicorn application:app --reload"
  6. now you can see the inbuilt swaager in web browser: "http://127.0.0.1:8000/docs"
