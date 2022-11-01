<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Login_microservice" />

  &#xa0;

  <!-- <a href="https://login_microservice.netlify.app">Demo</a> -->
</div>

<h1 align="center">Login_microservice</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/JA-Dempsey/login_microservice?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/JA-Dempsey/login_microservice?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/JA-Dempsey/login_microservice?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/JA-Dempsey/login_microservice?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/JA-Dempsey/login_microservice?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/JA-Dempsey/login_microservice?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/JA-Dempsey/login_microservice?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Login_microservice 🚀 Under construction...  🚧
</h4> 

<hr> -->
## About ##

A very basic microservice-type program to practice the use of a microservice in another program. This 
program will simply count the number of current users given the name of users being logged in. It does
not record passwords, nor should be used with any information that needs to be secure.

## Features ##

:heavy_check_mark: Given names of people logging in and out can track the number
of current logged-in users.


## Technologies ##

The following tools were used in this project:

- Flask

## :white_check_mark: Requirements ##

Included in the requirements txt:
- Install Flask (recommend a virtual environment)


```bash
# Clone this project
$ git clone https://github.com/JA-Dempsey/login_microservice

# Install dependencies
$ pip install flask

# Run the project
$ python app.py

# The server will initialize in the <http://localhost:5000>
```

## Usage ##

The microservice allows for two POST request and a GET request. The info page (localhost:5000/info) shows
the three requests that can be sent to the microservice.

For the POST requests, they must be sent with a JSON within the body (specified as json/application).
For the purposes of this program it is recommended to use {name: <insert_name>} as the basic JSON construct
to send to the server.

An example of this can be as follows:
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"test\"}" 127.0.0.1:5000/login
curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"test\"}" 127.0.0.1:5000/logout

The \ are required in Windows for the command to work to escape the inner "" in the JSON input wanted.
Each will acknowledge that the user was added as a response.

The get request will return the number of current users logged in.

As an exampe:

curl -X GET  127.0.0.1:5000/current
Returns the current count

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.


Made by <a href="https://github.com/JA-Dempsey" target="_blank">Andrew Dempsey</a>

&#xa0;

<a href="#top">Back to top</a>
