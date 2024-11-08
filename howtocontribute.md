# How do I participate?
That is what this guide will tell you!

## First you need to install [Python.](https://www.python.org/downloads/) 
After Python is installed, you will need to install the dependencies in the dependencies.md file using pip, its just like NPM in COMP206.

I also recommend the Python extension on Visual Studio Code.

## Then message Eric or Julian in the CPA Discord
We will invite you to our private testing server where you can use the bot privately. We will answer and questions and act as your senior developers, just like in an actual development job. 

## Clone the repository from github
I personally recommend you use Visual Studio Code as github is essentially embedded in VSCode. 

You can clone it one of two ways:

1. Click "clone repository" on the home page of VSCode and put the link to this repo in the dropdown menu that appears at the top of the screen.

2. Open then terminal and type the following command `git clone https://github.com/astrosaturn/CPADiscordBot`

After you have cloned it you now have the bot on your computer!

## I'm all set up to start, what now?

Now you need to make a .env file. Just make a new file in the ./CPADiscordBot directory called ".env"

.env files are special files that are used by developers to hide important information, such as the bot's token (which you can find pinned in general in the development server). This is so people cant open our public repo and yank the token and start using it for nefarious purposes.

Once you make the .env file, put in `DISCORD_TOKEN = {token}` into the file, replacing {token} with the token from the server, and then run the bot!

To run the bot you may either:

A. Open main.py and click the play button at the top right of VSCode

B. Open the terminal and type `python main.py`

If the bot successfully starts, you will get a message telling you that the script has successfully logged on to Gravey!

## I've written some code, how do I add it to the repository?
We ask that you make a pull request so we can review the code and then bring it into the main repository.

How to make a pull request:

Open the terminal in Visual Studio Code and do the following:

Make sure you arent on the main branch, we dont want to make a pull request on the main branch.
`git checkout -b your-feature-branch`

Then commit your changes.
`git add .`
`git commit -m "Put a descriptive sentence about your changes here"`

And finally push the changes to your new remote repository.
`git push origin your-feature-branch`

Either Eric or Julian will review your pull request, and we will give you our thoughts on it, any improvements to be made, then we will pull it into the repo!

## That should be it! 
If you have any questions, feel free to ask either me (Eric) or Julian, or just chatgpt it because that works too.
