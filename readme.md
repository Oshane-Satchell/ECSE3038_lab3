# Lab 3

**Lab Tester**

[https://ecse3038-lab3-tester.netlify.app/](https://ecse3038-lab3-tester.netlify.app/)

## Aim

This lab is meant to get students more accustomed to the technologies used in designing and implementing a RESTful API server.

## Requirements

You've been assign a project that will be used to manage a system that monitors the status of a set of electronically measured water tanks. The embedded circuit attached to each water tank will measure the height of the water in the tank and report on the tank's current stored volume as a percentage of its maximum capacity.

Your role is to design a RESTful API that allows each IoT enabled water tank to interface with your server so that the measure values can be represented visually on a web page. The web page will be designed by another member of your team.

Your API should also support the maintenance of a simple user profile.

Your server should be able to perform the actions of a simple HTTP web server. The server should be able to perform actions on a resource such as Create, Read, Update and Delete. This is to be done with the use of a MongoDB database.

Your server should be designed to host at least 6 specific HTTP routes. They are:

```jsx
GET /profile
POST /profile

GET /data
POST /data
PATCH /data/:id
DELETE /data/:id
```

### Required Attributes

Profile

- Username
- Favourite color
- Role

Tank

- Tank id (automatically implemented)
- Tank location description
- Percent full
- Latitude
- Longitude

### Profile routes

**GET /profile**

Your server application should allow a user to create only one user profile. The get request should only ever return a singular JSON object. Its structure is defined in *fig.1.*

**POST /profile**

Your server should allow for an incoming POST request that accepts a JSON body as described above. The structure of the JSON request should match the example illustrated by the "Example Request" in *fig.2.*  The server response should be structured as the the "Expected Response" in *fig.2.* The `last_updated` attribute should be generated by the server application and can be formatted any way you choose (it MUST include both date and time), as long as it reflects the time at the time of the request. The `last_updated` attribute should not be sent to the server application by the client.

The route should also return status code that indicates that an object was successfully created.

### Data Routes

**GET /data**

This route should return an array of 0 or more objects. If a POST request was successfully made to the /data route previously, the GET route should return the posted object in the array. The structure of the object can be seen in *fig.4.*

The route should also return status code that indicates that an object was successfully created.

**POST /data**

This route should accepts a JSON structured as depicted in *fig.5.* On success, the server should respond the the same JSON that was posted with the addition of an `_id` attribute. This `_id` is to be generated by the database. 

**PATCH /data/:id**

Your server should allow a user to alter the parts of one of the tanks after it has been posted. The server should allow the requester to make a JSON body with any combination of the four attributes and update them as necessary (The client should NOT be allowed to edit the `_id` attribute). An example request and expected result can be seen in *fig.6.*

**DELETE /data/:id**

Your server application should allow the requester to delete any previously POSTed object. The server application should not send back any message to the client once the objects has been deleted. There should, however, be a suitable response code that indicated that an empty response is expected.

## Submission

Your code should be uploaded to your GitHub account.

The repo should be called "ECSE3038_lab3".

**Your main python script must be called app.py.**

**The application must listen for incoming request on port 8000.**

You should include a .gitignore file that omits any file that isn’t the [app.py](http://app.py), a README.md and requirements.txt.

Due date is Sunday, February 10, 2023 at 4:00PM.

You're only required to provide a link to your GitHub repository. 

Any commits made to the repo after the due date will not be considered.

## Profile routes

```jsx
GET /profile

Before POST Request
Expected Response
{}

After Successful POST Request
Expected Response 
{
    "last_updated": "2/3/2022, 8:48:51 PM",
    "username": "coolname",
    "role": "Engineer",
    "color": "#3478ff"
}
```

*fig.1*

```jsx
POST /profile 

Example Request
{
    "username": "coolname",
    "role": "Engineer",
    "color": "#3478ff"
}

Expected Response 
{
    "last_updated": "2/3/2021, 8:48:51 PM",
    "username": "coolname",
    "role": "Engineer",
    "color": "#3478ff"
}
```

*fig.2*

*fig.3*

## Tank routes

```jsx
GET /data

Expected Response
[
    {
				"id": 1,
        "location": "Engineering department",
        "lat": 18.0051862,
        "long": -76.7505108,
        "percentage_full": 92
    },
		.
		.
		.
]
```

*fig.4*

```jsx
POST /data

Example Request
{
    "location": "Physics department",
    "lat": 18.004741066082236,
    "long": -76.74875280426826,
    "percentage_full": 56
}

Example Response
{
		"id": "2"
    "location": "Physics department",
    "lat": 18.004741066082236,
    "long": -76.74875280426826,
    "percentage_full": 56
}
# Lab 3

**Lab Tester**

[https://ecse3038-lab3-tester.netlify.app/](https://ecse3038-lab3-tester.netlify.app/)

## Aim

This lab is meant to get students more accustomed to the technologies used in designing and implementing a RESTful API server.

## Requirements

You've been assign a project that will be used to manage a system that monitors the status of a set of electronically measured water tanks. The embedded circuit attached to each water tank will measure the height of the water in the tank and report on the tank's current stored volume as a percentage of its maximum capacity.

Your role is to design a RESTful API that allows each IoT enabled water tank to interface with your server so that the measure values can be represented visually on a web page. The web page will be designed by another member of your team.

Your API should also support the maintenance of a simple user profile.

Your server should be able to perform the actions of a simple HTTP web server. The server should be able to perform actions on a resource such as Create, Read, Update and Delete. This is to be done with the use of a MongoDB database.

Your server should be designed to host at least 6 specific HTTP routes. They are:

```jsx
GET /profile
POST /profile

GET /data
POST /data
PATCH /data/:id
DELETE /data/:id
```

### Required Attributes

Profile

- Username
- Favourite color
- Role

Tank

- Tank id (automatically implemented)
- Tank location description
- Percent full
- Latitude
- Longitude

### Profile routes

**GET /profile**

Your server application should allow a user to create only one user profile. The get request should only ever return a singular JSON object. Its structure is defined in *fig.1.*

**POST /profile**

Your server should allow for an incoming POST request that accepts a JSON body as described above. The structure of the JSON request should match the example illustrated by the "Example Request" in *fig.2.*  The server response should be structured as the the "Expected Response" in *fig.2.* The `last_updated` attribute should be generated by the server application and can be formatted any way you choose (it MUST include both date and time), as long as it reflects the time at the time of the request. The `last_updated` attribute should not be sent to the server application by the client.

The route should also return status code that indicates that an object was successfully created.

### Data Routes

**GET /data**

This route should return an array of 0 or more objects. If a POST request was successfully made to the /data route previously, the GET route should return the posted object in the array. The structure of the object can be seen in *fig.4.*

The route should also return status code that indicates that an object was successfully created.

**POST /data**

This route should accepts a JSON structured as depicted in *fig.5.* On success, the server should respond the the same JSON that was posted with the addition of an `_id` attribute. This `_id` is to be generated by the database. 

**PATCH /data/:id**

Your server should allow a user to alter the parts of one of the tanks after it has been posted. The server should allow the requester to make a JSON body with any combination of the four attributes and update them as necessary (The client should NOT be allowed to edit the `_id` attribute). An example request and expected result can be seen in *fig.6.*

**DELETE /data/:id**

Your server application should allow the requester to delete any previously POSTed object. The server application should not send back any message to the client once the objects has been deleted. There should, however, be a suitable response code that indicated that an empty response is expected.

## Submission

Your code should be uploaded to your GitHub account.

The repo should be called "ECSE3038_lab3".

**Your main python script must be called app.py.**

**The application must listen for incoming request on port 8000.**

You should include a .gitignore file that omits any file that isn’t the [app.py](http://app.py), a README.md and requirements.txt.

Due date is Sunday, February 10, 2023 at 4:00PM.

You're only required to provide a link to your GitHub repository. 

Any commits made to the repo after the due date will not be considered.

## Profile routes

```jsx
GET /profile

Before POST Request
Expected Response
{}

After Successful POST Request
Expected Response 
{
    "last_updated": "2/3/2022, 8:48:51 PM",
    "username": "coolname",
    "role": "Engineer",
    "color": "#3478ff"
}
```

*fig.1*

```jsx
POST /profile 

Example Request
{
    "username": "coolname",
    "role": "Engineer",
    "color": "#3478ff"
}

Expected Response 
{
    "last_updated": "2/3/2021, 8:48:51 PM",
    "username": "coolname",
    "role": "Engineer",
    "color": "#3478ff"
}
```

*fig.2*

*fig.3*

## Tank routes

```jsx
GET /data

Expected Response
[
    {
				"id": 1,
        "location": "Engineering department",
        "lat": 18.0051862,
        "long": -76.7505108,
        "percentage_full": 92
    },
		.
		.
		.
]
```

*fig.4*

```jsx
POST /data

Example Request
{
    "location": "Physics department",
    "lat": 18.004741066082236,
    "long": -76.74875280426826,
    "percentage_full": 56
}

Example Response
{
		"id": "2"
    "location": "Physics department",
    "lat": 18.004741066082236,
    "long": -76.74875280426826,
    "percentage_full": 56
}
