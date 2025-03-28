# How do I participate?
That is what this guide will tell you!

## First you need to install [Python.](https://www.python.org/downloads/) 3.12.6
After Python is installed, you will need to install the dependencies in the dependencies.md file using pip, its just like NPM in COMP206.

I also recommend the Python extension on Visual Studio Code.

## Then message Eric or Julian in the CPA Discord
We will invite you to our private testing server where you can use the bot privately. 
We will answer and questions and act as your senior developers, just like in an actual development job. 

## Clone the repository from github
I personally recommend you use Visual Studio Code as github is essentially embedded in VSCode. 

You can clone it one of two ways:

1. Click "clone repository" on the home page of VSCode and put the link to this repo in the dropdown menu that appears at the top of the screen.

2. Open then terminal and type the following command `git clone https://github.com/astrosaturn/CPADiscordBot`

After you have cloned it you now have the bot on your computer!

## I'm all set up to start, what now?

First run the terminal, and run `pip install poetry`. 

If pip *doesn't work*:

- Rerun the Python installer
- Click `modify`
- Click `next`
- Check `Add to enviornmental variables`

Then click install, restart VSCode, and rerun the command.

Once the command works, run `poetry install`.
Then all the dependiencies should install automatically.

Now you need to make a .env file. Just copy the .envexample file and rename it to just `.env`.

.env files are special files that are used by developers to hide important information, such as the bot's token (which you can find pinned in general in the development server). This is so people cant open our public repo and yank the token and start using it for nefarious purposes.

To run the bot you must run the command `poetry run python main.py`.

If the bot successfully starts, you will get a message telling you that the script has successfully logged on to Gravey!

## I've written some code, how do I add it to the repository?
We ask that you make a pull request so we can review the code and then bring it into the main repository.

How to make a pull request:

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Or

In the version control tab, press the plus to stage your changes, add a message, then next to the commit button press the dropdown arrow and press `Commit & Create Pull Request`

Either Eric or Julian will review your pull request, and we will give you our thoughts on it, any improvements to be made, then we will pull it into the repo!

## That should be it! 
If you have any questions, feel free to ask either me (Eric) or Julian, or just chatgpt it because that works too.
