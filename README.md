
# Hangman 

- Hangman as the name suggest is a game for saving a man from "Hang Till Death" situation.
- Its also a great way to learn new words and game helps to improve vocabulary.
- Game is very simple:-
   - Player get 6 chances to save the man
   - Guess the correct words before chances are over and save the man.

[Link to the website](https://hangman-pp.herokuapp.com/)

![An image previewing all devices](/assets/screenshots/preview.png)

## Contents
- [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
- [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
- [Teachnical Design](#technical-design)
    - [Flowchart](#flowchart)
- [Technology Used](#technology-used)
    - [Language used](#language-used)
    -[Python Libraries used](#python-libraries-used)
    - [Other websites/tools used](#other-websitestools-used)
    - [3rd Party Python Libraries used](#3rd-party-python-libraries-used)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Tested Devices with Browsers](#tested-devices-with-browsers)
    - [Validator Testing](#validator-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
- [Deployment](#deployment)
    - [Deploying in Heroku](#deploying-the-website-in-heroko)
    - [Cloning of Repo](#cloning-the-repository-in-github)
- [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
- [Thank You](#thank-you)

## Project Goals
### User Stories

- Play Hangman game
- Be able to sign up as new user
- Be able to login as existing user
- Be able to read the rules
- Be able to restart the game
- Be able to use in different media 

### Site Owner Goals

- Create a game which is easy and clear to user
- Ensure that new user is able to signup
- Ensure that existing user can login
- Ensure errors are handled and displayed to user
- Ensure that user is able to understand the game
- Ensure that user can read the rules of the game
- Ensure that user can restart the game

## User Experience
### Target Audience

- There is no specific audience for the game. 
- But it displays a dead man cartoon image so adults can decide if it's ok for their children to play or not
- I would recommend that its also a game to improve vocabulary so children above 8 years can play

### User Requirements and Expectations

- A simple and fun game
- Straightforward Navigation
- Game personalisation by entering players' names
- Log-in works as expected and incorrect details do not allow the user access to their account.

### User Manual
<details><summary>Click here to view instructions</summary>

#### Load Game

- On loading the game, users are presented with heading of the game which  displays design of hangman and the title.
- Under the heading, a question is prompted if the user is existing user or not.
- Operation: Are you an existing user: Y/N
- If user inputs do not correspond with available option then they will be promt to try again

#### Sign Up

- If user is a new player, they will be required to sign up
- The instructions will be displayed how to sign up
- User will be required to enter a new name and password
- Once sign up is successful, user will be ask to login to play the game
- Operation: Sign Up Here
    - Enter New Username
    - Enter New Password

#### Login

- If user is an existing user, they will be asked to enter username and password
- If it matches will the data, the user will be logged in.
- A welcome message on the screen will be displayed for the users with their name
- The input goes through a validation process. If the user input is not correct they have an option to try again .
- If user does not exist, they will be prompted again with:
    Are you an existing user: Y/N
- Operation: Login to play Hangman
    - Username
    - Password

#### Users greeting

- Once users have been logged in, the program will display a greeting message with the user name

#### Rules

- Once users have been logged in, they will be asked if they want to see the rules
- Operation: Do you want to see the rules: Y/N

#### Start Game

- If user decide to see the rules, after displaying rules the game will start automatically
- If user decide not to see the rules, the game will start automatically without displaying rules

#### Game

- Once the game has started it will display initial stage of hangman, attempts left and blank lines which depicts secret word
- Operation: Enter a guess letter:
    - User need to enter a letter to start the game
    - Once a letter is entered the hints letters will be displayed
    - If input is more than a letter or not an alphabet, it will display an error
    - Once secret word is guessed, player will win
    - If attempts are over before word is guessed, player lose

#### Restart Game
- Once user wins or lose, a restart game question will be prompted
- Operation: Do you want to play again: Y/N
    - If user input is "Y", the game will restart
    - If user input is "N", the game will quit and user will be logged out
    - If user input is invalid, an error will be thrown and question will be prompted again

</details>

## User Stories

### Users

1. I want to be able to have an option as existing user or new user
2. I want to able to signup as new user
3. I want to be able to log-in if I return to the game
4. I want to be able to read the rules of the game
5. I want to be able to restart game when I'm logged in

### Site Owner

6. I want users to have a positive experience whilst playing the game
7. I want user names and password to be saved to Google Spreadsheet
8. I want the user to get errors displayed in case of wrong input
9. I want data entry to be validated, to guide the user on how to correctly format the input
10. I want user to see their name once they login

## Technical Design

## FlowChart

- [Lucidchart](https://www.lucidchart.com) was used to build flowchart

<details>
    <summary>Flowchart</summary>
    <p>Hangman Game Flowchart</p>
    <img src = "assets/screenshots/lucid.jpeg" alt = "A screenshot of flowchart">
</details>

## Technology Used
### Language Used

  - Python

### Python Libraries used

- os - used to clear terminal
- random - used to choose random words
- time - used to displayed delayed areas in the terminal

### Other websites/tools used

- [Lucidchart](https://www.lucidchart.com) was used to build flowchart
- [GitHub](https://github.com/) was used for saving and storing files.
- [GitPod](https://www.gitpod.io/) was the IDE used for writing code.
- [Heroku](https://www.heroku.com/) was used as the deploying platform for this site.

### 3rd Party Python Libraries used

- [Google sheets API](https://github.com/burnash/gspread) was used to store and check the user input and authorize the user identity
- [Google OAuth](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to connect the project with the google account.
- [Colorama](https://pypi.org/project/colorama/) was used for better visual display

## Features

### Home page display

- Once the user run the program this area is displayed
- The area consist of a display showing the heading
- It also prompts the users to provide input if they are an existing user
- User stories covered: 1
<details>
    <summary>Home Page screenshot</summary>
    <img src="assets/screenshots/gameload.png" alt="Game load page">
</details>  

### User Signup Area

- This area display an instruction for signup for new users
- This area is displayed when player is not an existing user
- Once new username and password is entered, it prompts Signup confirmed..
- The input data is updated in google spreadsheet
- User stories covered: 2, 8, 9

<details>
    <summary>Sign Up Area screenshot</summary>
    <img src="assets/screenshots/signup.png" alt="Sign up area">
    <img src="assets/screenshots/worksheet.png" alt="Worksheet"> 
</details> 

### User Login Area

- This area is displayed if user is an existing user
- Users need to login their details to play the game
- User stories covered: 3, 8, 9

<details>
    <summary>Login Area screenshot</summary>
    <img src="assets/screenshots/login.png" alt="Login area">
</details> 

### User Greeting
- After user is logged in successfully, a welcome message is displayed
- User stories covered: 6, 10

<details>
    <summary>Welcome message Screenshot</summary>
    <img src="assets/screenshots/ustory3.png" alt="Welcome message">
</details>

### Rules for the Game

- This area shows the rule of the game
- User can decide to see the rules or directly start the game
- After rules is displayed game starts automatically
- User stories covered: 4

<details>
    <summary>Rules Area screenshot</summary>
    <img src="assets/screenshots/rules.png" alt="Rules area">
</details> 

### Game display Area

- This area is displayed once the user read the rules or decide to skip the rules
- Initial Display
  - Hangman initial stage
  - Attempts left
  - Six " _ " depicting secret word
- Once player guess a letter, the hint letters are displayed
- This was done to make the game little exicting
- User stories covered : 6, 8

<details>
    <summary>Game Area screenshot</summary>
    <img src="assets/screenshots/gamedisplay.png" alt="Game area">
</details> 

### Restart Game

- Once the play has played the game, they recieve a promt if they want to play again or not
- This is provided for both kind of players: Losers or Winners
- If they decide to play again, the game will restart
- If not the game will end and user will be logged out
- User stories covered : 5, 9

<details>
    <summary>Restart Game screenshot</summary>
    <img src="assets/screenshots/restart.png" alt="Restart Game">
</details> 


## Testing
- Manual testing of user stories
- Testing on Browsers
- Tested Devices with Browsers
- Validator Testing

### Manual Testing
<details><summary>See user stories testing</summary>

1. I want to be able to have an option as existing user or new user

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Are you an existing user | Type Y/N | Y: Open login area / N: SignUp Area | Works as expected
<details>
    <summary>Screenshots</summary>
    <p>Sign Up</p>
    <img src="assets/screenshots/ustory1-signup.png" alt="Sign up area">
    <p>Log In</p>
    <img src="assets/screenshots/ustory1-login.png" alt="Login area">
</details> 

2. I want to able to signup as new user

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Sign Up Here | Enter New Username/ Enter New Password | Sign Up Complete : Login Page opens | Works as expected
<details>
    <summary>Screenshots</summary>
    <p>Sign Up Area</p>
    <img src="assets/screenshots/signup.png" alt="Sign up area">
    <p>Login area opens after sign up is confirmed</p>
    <img src="assets/screenshots/userstory2.png" alt="Login area">
</details> 

3. I want to be able to log-in if I return to the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login To Play Hangman | Username/ Password | Login Successful : Open rules | Works as expected

<details>
    <summary>Screenshots</summary>
    <p>Log In Area</p>
    <img src="assets/screenshots/ustory1-login.png" alt="Login area">   
    <p>Open rules is prompted after login is successful</p>
    <img src="assets/screenshots/ustory3.png" alt="Open rules">
</details> 

4. I want to be able to read the rules of the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Open Rules  | Type Y/N| Y: Open rules/ N: Starts Game | Works as expected

<details>
    <summary>Screenshots</summary>   
    <p>Open rules is prompted</p>
    <img src="assets/screenshots/ustory3.png" alt="Open rules">
    <p>If user input is "Y"</p>
    <img src="assets/screenshots/rules.png" alt="Rules of the game">
    <p>If user input is "N"</p>
    <img src="assets/screenshots/gamestart.png" alt="Game started">
</details> 

5. I want to be able to restart game when I'm logged in

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Restart Game  | Type Y/N| Y: Game restarts/ N: Game ends, User logged out | Works as expected

<details>
    <summary>Screenshots</summary>   
    <p>Restart is prompted</p>
    <img src="assets/screenshots/restartq.png" alt="Restart Question">
    <p>If user input is "Y"</p>
    <img src="assets/screenshots/restart.png" alt="Game restarts">
    <p>If user input is "N"</p>
    <img src ="assets/screenshots/ustory5.png" alt="Game ends">   
</details>

6. I want users to have a positive experience whilst playing the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | Simple navigation and game play  | Colored messages and straightforward instructions | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/ustory1-signup.png" alt="Sign up area">
    <img src="assets/screenshots/userstory2.png" alt="Login area">
    <img src="assets/screenshots/ustory3.png" alt="Open rules"> 
    <img src="assets/screenshots/restartq.png" alt="Restart Question">
</details>

7. I want user name and password to be saved to Google Spreadsheet

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Sign-Up | Users input their name and password which has not been previously registered  | Username and password are saved to Google Spreadsheet| Works as expected |

<details>
    <summary>Screenshots</summary>
    <p>Google Spread Worksheet</p>
    <img src="assets/screenshots/worksheet.png" alt="Worksheet">      
</details> 

8. I want the user to get errors displayed in case of wrong input

 **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | User inputs invalid input when questions are prompted. User inputs invalid value during log-in or sign-up | Feedback message displayed to the user | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/us9.png" alt="User Exist area">
    <img src="assets/screenshots/errorsignup.png" alt="Sign up area">
    <img src="assets/screenshots/errorlogin.png" alt="Login area">
    <img src="assets/screenshots/errorrules.png" alt="Open rules"> 
    <img src="assets/screenshots/errorrestart.png" alt="Restart Question">
</details>

9. I want data entry to be validated, to guide the user on how to correctly format the input

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | User inputs invalid data | Feedback message with instructions diplayed to the user | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/us9.png" alt="User Exist area">
    <img src="assets/screenshots/signU9.png" alt="Sign up area">
    <img src="assets/screenshots/loginUS9.png" alt="Login area">
    <img src="assets/screenshots/errorrules.png" alt="Open rules"> 
    <img src="assets/screenshots/errorrestart.png" alt="Restart Question">
</details>

10. I want user to see their name once they login

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome (Username) | After successful login | Users are asked to input their username and password, and once validated, a greeting message with their name is displayed. | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/ustory3.png" alt="Welcome message">
</details>

</details>

### Testing on Browsers
- I tested that this game works in different browsers - Chrome and Safari and was able to deploy successfully

### Tested Devices with Browsers
- iPhone 12
    - Safari
- Samsung S22 Ultra
    - Chrome
- Macbook Pro 2019 16-inch
    - Chrome
    - Safari

### Validator Testing
#### PEP8 Python Validator
[PEP8 Python Validator](https://pep8ci.herokuapp.com/) was used to validate the code.

This validator was provided by Code Institute.

No errors were found.

<details>
    <summary>gsheet.py</summary>
    <p>Result: gsheet.py</p>
    <img src = "assets/screenshots/gsheet.png" alt = "A screenshot of gsheet.py result">
</details>

<details>
    <summary>run.py</summary>
    <p>Result: run.py</p>
    <img src = "assets/screenshots/run-valid.png" alt = "A screenshot of run.py result">
</details>

### Bugs and Fixes
- No unfixed bugs.
- Following bugs were fixed
| **Bug** | **Fix** |
| ------- | ------- |
| When user login password input was wrong it was not giving an option to go back | Add signup_check function which will prompt again if user exist or not|
|When user do not exist was prompted during login, user didn'T have option to go back| Add signup_check function which will prompt again if user exist or not|


## Deployment

### Deploying the website in Heroko:
- The website was deployed to Heroko using following steps:
#### Login or create an account at Heroku
- Make an account in Heroko and login

<details>
    <summary>Heroko Login Page</summary>
    <img src="assets/heroku/heroku_login.png" alt="Heroko login page">
</details>

#### Creating an app
  - Create new app in the top right of the screen and add an app name.
  - Select region
  - Then click "create app".

<details>
    <summary>Create App</summary>
    <img src="assets/heroku/createapp.png" alt="Heroko create app screenshot">
</details>

#### Open settings Tab
  ##### Click on config var
  - Store CREDS file from gitpod in key and add the values
  - Store PORT in key and value

<details>
    <summary>Config var</summary>
    <img src="assets/heroku/config.png" alt="Config var screenshot">
</details>

  ##### Add Buildpacks
  - Add python buildpack first
  - Add Nodejs buildpack after that

<details>
    <summary>Buildpacks</summary>
    <img src="assets/heroku/buildpacks.png" alt="Buildpacks screenshot">
</details>

 #### Open Deploy Tab
   ##### Choose deployment method
  - Connect GITHUB
  - Login if prompted

<details>
    <summary>Deployment method</summary>
    <img src="assets/heroku/method.png" alt="Deployment method screenshot">
</details>

   ##### Connect to Github
  - Choose repositories you want to connect
  - Click "Connect"

<details>
    <summary> Repo Connect</summary>
    <img src="assets/heroku/repo-connect.png" alt="Repo connect screenshot">
</details>

  ##### Automatic and Manual deploy
  - Choose a method to deploy
  - After Deploy is clicked it will install various file

<details>
    <summary> Deploy methods</summary>
    <img src="assets/heroku/deploy.png" alt="deploy method screenshot">
</details>

  ##### Final Deployment
  - A view button will display
  - Once clicked the website will open

<details>
    <summary> Deploy</summary>
    <img src="assets/heroku/view.png" alt="view screenshot">
</details>


### Cloning the repository in GitHub
1. Visit the GitHub page of the website's repository
2. Click the “Clone” button on top of the page
3. Click on “HTTPS”
4. Click on the copy button next to the link to copy it
5. Open your IDE
6. Type ```git clone <copied URL>``` into the terminal

## Credits

### Content
- The text content was provided by the site owner.
- Idea of Hangman game has been taken from hangman game played around the world

### Code
#### The following ideas were borrowed from [Love Sandwiches](https://github.com/Sinha5714/Love_Sandwiches)

-  validate_user_details function
-  How to import gspread
-  How to import Credentials from google.oauth

#### The following code idea was taken from google search and various youtube videos

- play_hangman function; (https://www.youtube.com/shorts/GYCCN0IP8u0)
- How to clear terminal


### Thank You
- to my mentor Mo Shami for supporting me with his feedback through the entire project
- special thanks to my husband Remo Liebetrau to help me finding out the issues in the game
- to Code Institute and Slack community for helping me when I was getting stuck with some challenges.