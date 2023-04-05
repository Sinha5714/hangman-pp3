
# Hangman 

- Hangman as the name suggest is a game for saving a man from "Hang Till Death" situation.
- Its also a great way to learn new words and game helps to improve vocabulary.
- Game is very simple:-
   - Player get 6 chances to save the man
   - Guess the correct words before chances are over and save the man.

[Link to the website](https://hangman-pp.herokuapp.com/)

![An image previewing all devices](/assets/screenshots/preview.png)

## Contents
[UX](#ux)
 - [User Stories](#user-stories)
 - [Site Owner Goals](#site-owner-goals)
 - [Potential Features](#potential-features)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features to be implemented](#features-to-be-implemented)
- [Testing](#testing)
  - [Tested Devices with Browsers](#tested-devices-with-browsers)
  - [Validator Testing](#validator-testing)
  - [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
  - [Content](#content)
  - [Code](#code)
- [Thank You](#thank-you)

## UX
### User Stories
- Play Hangman game
- Signup to play game as a first time user
- Login to play game as existing user
- Able to restart the game
- Able to use in different media 
### Site Owner Goals
- Website for a Hangman game
- Rules for the game
- Instruction for Signup
- Login data check
- Validation for login and signup
- Log signup data
- Save signup details in googlespread worksheet
- Extract login details and check
- Display of hangman
- Chances left for user
- Random words for the game
- Hint letters for the user
- Add their name to the game
- Deployment of the game
### Potential Features
- 
 

## Features
### Existing Features

#### Home page display
- The main page will be displayed once the website is open.
- It consists of a heading, a small description of the game and three buttons.
- Each button has seperate function:
    - Play button : Opens the Username entry page
    - How to Play button : Opens the rules page of the quiz
    - High Scores button : Opens the page for high score table
    
  ![An image of home display](/assets/screenshots/gameload.png)

#### Rules for the Game
  - This page opens once the "How To Play" button is clicked on main-page.
  - This page consists of rules about how to play the game and a "Home" button.
  - Once the Home button is clicked, user goes back to the main-page.

![An image of rules page](assets/screenshots/rules.png)

#### User Signup Area
- This page opens when "Play" button is clicked in the main page.
- This page consists of a heading, an input field for user to enter the name and a "Start Game" button.
- Once the "Start Game" button is clicked user can start playing the quiz.

![An image of Username Entry Page](/assets/screenshots/username.png)

#### User Login Area
- This page opens when "High Scores" button is clicked in main page.
- This page consists of a heading, a table with Table heading of "USERNAME" and "SCORES" and a Home button.
- Once the "Home" button is clicked, user will go back to main-page.

![An image of High Score Area](assets/screenshots/login.png)

#### Game display Area
- This page opens when "Start Game" button is clicked in Username Entry Page.
- This page consists of the following:
    - A heading
    - A welcome message with Username value in it
    - An area for question image
    - Four option buttons
    - Restart button
    - Next button
    - Score area
    - Timer 
- Once the page is loaded, the timer starts with a coundown of 15 seconds for user to choose an option.
- The score is 10 for per correct answer and will be displayed in the score area.
- Next button is to go to the next question.
- Restart button is provided for user to restart the game in the same quiz page. 


![An image of quiz area](assets/screenshots/gamedisplay.png)

#### Restart Game 
- This page opens automatically after the 10 quiz questions have been played.
- This page consists of :
    - A heading
    - A congratulation message: 
        - Number of total correct question attempted
        - Score obtained by the user
    - Save High Score button
    - Home button
- Once "Save High Score" button is clicked, username and scores will be added to the high score table and "High Score Page" will be opened.

![An image of end page](assets/screenshots/restart.png)

### Features to be implemented
- More question images
- Sound for the game
- Event listners for all buttons to call functions
- An online multiplayer quiz competition

## Testing
- I tested that this page works in different browsers - Chrome and Safari

### Manual Testing
- 

### Tested Devices with Browsers
- iPhone 12
    - Safari
- Samsung S22 Ultra
    - Chrome
- Macbook Pro 2019 16-inch
    - Chrome
    - Safari

### Validator Testing


### Unfixed Bugs
- No unfixed bugs.

## Deployment

### Deploying the website in Heroko:
- The website was deployed to heroko using following steps:
  - Login or create an account at Heroku

![Login page](/assets/heroku/heroku_login.png)

- Creating an app
  - Create new app in the top right of the screen and add an app name.
  - Select region
  - Then click "create app".

![create app](/assets/heroku/createapp.png)

- Open settings Tab
  - Click on config var
     - Store CREDS file from gitpod in key and add the values
     - Store PORT in key and value

![Config var](/assets/heroku/config.png)

  - Add Buildpacks
     - Add python buildpack first
     - Add Nodejs buildpack after that

![buildpacks](/assets/heroku/buildpacks.png)

 - Open Deploy Tab
   - Choose deployment method
     - Connect GITHUB
     - Login if prompted

![connect github](/assets/heroku/method.png)

   - Connect to Github
     - Choose repositories you want to connect
     - Click "Connect"

![connect](/assets/heroku/repo-connect.png)

  - Automatic and Manual deploy
     - Choose a method to deploy
     - After Deploy is clicked it will install various file

![deploy](/assets/heroku/deploy.png)

  - Final Deployment
     - A view button will display
     - Once clicked the website will open

![view](/assets/heroku/view.png)


### Cloning the repository in GitHub
1. Visit the GitHub page of the website’s repository
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
#### The following ideas were borrowed from [Love Sanswiches](https://github.com/Sinha5714/Love_Sandwiches)

-  validate_user_details function
-  How to import gspread
-  How to import Credentials from google.oauth

#### The following code idea was taken from google search and various youtube videos

- play_hangman function; (https://www.youtube.com/shorts/GYCCN0IP8u0)


#### Following code idea was provided by my Mentor

- saveHighScore(); (https://stackoverflow.com/questions/1129216/sort-array-of-objects-by-string-property-value)

### Thank You
- to my mentor Mo Shami for supporting me with his feedback through the entire project
- to Code Institute and Slack community for helping me when I was getting stuck with some challenges.