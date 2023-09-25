# Token-Auth-with-FastAPI

**GITHUB REPOSITORY**: "[https://github.com/Conradgabe/Token-Auth-with-FastAPI](https://github.com/Conradgabe/Token-Auth-with-FastAPI)"

**HOSTED ENDPOINT**: "[https://tkauth.onrender.com/](https://tkauth.onrender.com/)"

**DOCUMENTATION URL**: "[https://github.com/Conradgabe/Token-Auth-with-FastAPI/blob/main/DOCUMENTATION.md](https://github.com/Conradgabe/Token-Auth-with-FastAPI/blob/main/DOCUMENTATION.md)"

# Installation and Setup

## Prequisites
Make sure you have the following prequisites installed on your development environment:

- FastAPI:
```
pip install "fastapi[all]"
```
- Web server:  Fastapi makes use of uvicorn to run a development server locally.
```
pip install uvicorn[standard]
```
- Database: FastAPI supports both relational and Non-relationship Databases such as MongoDB, MySQL, Postgres, SQLAlchemy and SQLite. SQLAlchemy is used in this project to set up the database.
```
pip install sqlalchemy
```
- Git: Git is a version control System used for manageing the project's source code.

  # Cloning and Preparing the Application
  Follow these steps to clone and prepare the application
  - Open your terminal and follow the following instructions:
  ### 1. Clone the Repository
  ```
  git clone https://github.com/Conradgabe/Token-Auth-with-FastAPI.git
  ```
  ### 2. Navigate to your Project Directory
  change your working directory to the cloned project folder
  ```
  cd Token-Auth-with-FastAPI/
  ```
  ### 3. Install Dependencies
  ```
  pip install -r requirements.txt
  ```
  ### 4. Run Development server
  ```
  uvicorn main:app --reload
  ```
  and wait a few seconds for it to run
  
### In your browser navigate to: 
```
http://127.0.0.1:8000/docs
```
This will take you to the api documentation where you can test and use the api locally
