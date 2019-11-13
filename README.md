# MainApp Python

Django app that integrate Graphql api and another REST resources in order to manage main requirements for an startup app.


#Instalation

- Create  a virtual environment.
- Install requirements needed:
```
python install -r requirements.txt
```
- Configure database using environments files environment.(prod|dev) direct values in main_app/settings.py
```
EMAIL_HOST_USER=user
EMAIL_HOST_PASSWORD=password
CORS_ORIGIN_WHITELIST_ENV=http://localhost:8080
SPA_URL=http://localhost:8080
DB_DATABASE_ENV=main_app
DB_USER_ENV=user
DB_PASSWORD_ENV=dbpassword
ENV_SUB_PATH=api/

```
- This environments variblables define mail specifications for user registration proccess configured using djonser.


# Some urls and availables functions
```
python manage.py show_urls   #show urls availables
```
```

/admin/ django.contrib.admin.sites.index        admin:index
/auth/jwt/create/       rest_framework_simplejwt.views.TokenObtainPairView      jwt-create #for rest functions
/auth/jwt/refresh/      rest_framework_simplejwt.views.TokenRefreshView jwt-refresh #for rest functions
/auth/jwt/verify/       rest_framework_simplejwt.views.TokenVerifyView  jwt-verify #for rest functions
/graphql/       #Default graphql endpoint exposed
```

### Graphql usage

- Get authentication token:
```
  mutation tokenAuth($username: String!, $password: String!){
          tokenAuth(username: $username, password: $password) {
          token
      }
  }
```
- Get refresh token:
```
mutation{
  refreshToken(token: token_value){
    token
    payload
  }
}
```
- Update user profile:
```
mutation{
  refreshToken(token: ______){
    token
    payload
  }
}
mutation{
  updateProfile(
  avatar: ______,
  city: ______,
  company: ______,
  country: ______,
  lastName: ______,
  name: ______,
  zipcode: ______
  ){
    profile
  }
}

```
- Get the rest of the graphql available functions in  the schema generated after run the project with:
``` 
python manage.py graphql_schema
```
