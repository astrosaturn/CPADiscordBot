# How do I participate?
That is what this guide will tell you!

## First you need to install [Python.](https://www.python.org/downloads/) 
After Python is installed, you will need to install the dependencies in the dependencies.md file using pip, its just like NPM in COMP206.

## Then message Eric or Julian in the CPA Discord
We will invite you to our private testing server where you can use the bot privately. We will answer and questions and act as your senior developers, just like in an actual development job. 

## Finally, clone the repository from github
I personally recommend you use Visual Studio Code as github is essentially embedded in VSCode. 

You can clone it one of two ways:

1. Click "clone repository" on the home page of VSCode and put the link to this repo in the dropdown menu that appears at the top of the screen.

2. Open then terminal and type the following command `git clone https://github.com/astrosaturn/CPADiscordBot`

After you have cloned it you now have the bot on your computer!

## I'm all set up to start, what now?

Now you need to make a .env file. Just make a new file in the /CPADiscordBot called ".env"

.env files are special files that are used by developers to hide important information, such as the bot's token (which you can find pinned in general in the development server). This is so people cant open our public repo and yank the token and start using it for nefarious purposes.

Once you make the .env file, put in `DISCORD_TOKEN = {token}` into the file, replacing {token} with the token from the server, and then run the bot!

To run the bot you may either:

A. Open main.py and click the play button at the top right of VSCode

B. Open the terminal and type `python main.py`

If the bot successfully starts, you will get a message telling you that the script has successfully logged on to Gravey!

## I've written some code, how do I add it to the repository?
There are two ways to do this, firstly and the simplest:

In VSCode look to the left side of your screen, there should be an icon that shows 3 dots connected together. That is the version control tab. Click it.

After that, you will see a list of all your changes, to commit them press the plus icon to stage them, type a message in the bot and then press "Commit". After that press sync and your changes will be pushed to the repo!

Or in the terminal:

`git add .` to add all your changes

`git commit` to commit your changes

Then type your commit message into the text file that opens, make it meaningful so everyone on the project knows what you did and the purpose of your commit. Then save the file and close it.

And finally, `git push` to push your changes to the repo. 

Congratulations! You have now pushed to the repo!

Make sure before you start working, run git pull or press sync in the version control tab to pull everyone else's changes into your workspace.

## That should be it! 
If you have any questions, feel free to ask either me (Eric) or Julian, or just chatgpt it because that works too.
