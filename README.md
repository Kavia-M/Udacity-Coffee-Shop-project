# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. The featues of the application are

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## Implementation
Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)

### Authors
- Kavia M from Natwest - an Udacity student

### Acknowledgements
Sincere Thanks to,
- Sahadevan, my colleague who also do this nanodegree, for helping me resolving the errors
- Natwest Groups, for providing me an opportunity to take the nanodegree
- Coach for the course Identity Access Management
- Awanish Kumar Sigh, Natwest mentor for the nanodegree
- Udacity Team, for continous support and mentorship

### Reference
1.  [My Own Trivia project file, referred for api.py for end points](https://github.com/Kavia-M/Trivia-files/blob/main/__init__.py)
2. [The reference code provided in Udacity github repository. This is the code taught in Course lessons. I referred this for auth.py code in backend authentication](https://github.com/udacity/cd0039-Identity-and-Access-Management/blob/master/lesson-2-Identity-and-Authentication/BasicFlaskAuth/app.py)
3. [Udacity course video - referred for check_permissions() function in auth.py This video is in Full Stack Web developer nanodegree -> Course 3 Identity Access Management -> Lesson 4 Access and Authorization -> Concept 4 Using RBAC in Flask](https://www.youtube.com/watch?v=oJTIraxK4UQ&t=1s)
4. [The reference code provided by Udacity in Course 2 API Development and Documentation. I referred this for delete drinks end point in api.py](https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/6_Final_Starter/backend/flaskr/__init__.py)

## Other links referred 
- [Error handler decorator in api.py](https://stackoverflow.com/questions/53285452/internal-server-error-rather-than-raised-autherror-response-from-auth0)
- [Exeption handling in api.py](https://www.geeksforgeeks.org/how-to-print-exception-stack-trace-in-python/)
- [To know about JWT payload and claims](https://jwt.io/introduction#:~:text=of%20the%20JWT.-,Payload,%2C%20public%2C%20and%20private%20claims.)
- [**To handle OSSL error in frontend**](https://stackoverflow.com/questions/69665222/node-js-17-0-1-gatsby-error-digital-envelope-routinesunsupported-err-os)
- [To resolve errors when calling insert and update](https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes)
- [To make the recipe in request in JSON format for post and patch end points](https://bobbyhadz.com/blog/python-replace-single-with-double-quotes-in-list#:~:text=Use%20the%20str.,replaced%20with%20a%20double%20quote)




[def]: https://www.youtube.com/watch?v=oJTIraxK4UQ&t=1s