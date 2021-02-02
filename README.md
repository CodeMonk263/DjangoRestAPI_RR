# DjangoRestAPI_RR
API hosted live [here](http://codemonk263.pythonanywhere.com/posts/)

## Features
1. Login
2. Registration
3. CRUD operations on posts
4. JWT Authentication

## Endpoints
1. [Admin Panel](http://codemonk263.pythonanywhere.com/admin/)
2. [Posts](http://codemonk263.pythonanywhere.com/posts)
3. [Login](http://codemonk263.pythonanywhere.com/login/)
4. [Register](http://codemonk263.pythonanywhere.com/register)
5. [JWT Token Refresh](http://codemonk263.pythonanywhere.com/refresh/)

## Few other pointers
1. Data cannot be accessed with JWT token which can be obtained at the time of registration and also when logging in.
2. To edit/delete a post, go to BASE_URL/<id_num>.
3. Postman works best for API testing.
4. For accessing/creating posts via JWT token, the header should be {"Authentication" : "JWT <token_code>"}.
5. Access all posts via GET request to [here](http://codemonk263.pythonanywhere.com/posts/) and for creating a new post POST request to [here](http://codemonk263.pythonanywhere.com/posts/) with the json data as {"title":"whatever title", "body":"whatever body"} and also the header as mentioned before.
6. For registration, the POST request to [here](http://codemonk263.pythonanywhere.com/register) should have json of the form - {"username":"whatever username", "password":"whatever password", "password2":"same as whatever password"}.

## Author
Shaurya Vijayvargiya
