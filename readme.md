# RESTful API Test Task
## Technology stack:

- FastAPI
- SQLite
- SQLAlchemy
- JWT, Oauth 2
- bcrypt (for password hashing)


## Functionality:

- User registration/authorization. During authorization, the user on the client receives a JWT from which you can get the user id.
- An authorized user has access to CRUD endpoints 
- CRUD Documetation (Swagger)
- Postman collection with autotests


<hr/>

## How to run
### Download
```
git pull https://github.com/vitaliykalachev/webtronics_tests.git
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run server
```
uvicorn app.main:app --reload
```
### Run Postman API tests
- import file ```RESTful_FastAPI_Posman_Collection.postman_collection.json``` into Postman
- run collection

### Documentation
###### All CRUD methods (Swagger UI)
``` 
https://localhost:8000/docs 
```

### Author
##### [Vitaliy Kalachev](https://vitaliykalachev.github.io) 
