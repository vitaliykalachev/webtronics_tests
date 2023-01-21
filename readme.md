# RESTful API Test Task
## Technology stack:

- FastAPI
- SQLite
- SQLAlchemy
- JWT, Oauth 2
- bcrypt (for password hashing)


## Functionality:

- User registration/authorization. 
- An authorized user has access to CRUD endpoints
- An authorized user can like or dislike other users posts but not his own
- CRUD API Documetation (Swagger)
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
- import file ```Posman_Collection.postman_collection.json``` into Postman
- run collection

### Documentation
###### All CRUD methods (Swagger UI)
``` 
https://localhost:8000/docs 
```

### Author
##### [Vitaliy Kalachev](https://vitaliykalachev.github.io) 

