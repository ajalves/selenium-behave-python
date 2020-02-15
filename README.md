# Selenium with Behave Framework

## Selenium

More information can be found [here](https://www.seleniumhq.org/)

## Behave

BDD (Behaviour-Driven Development) framework.
It's documentation can be found [here](https://behave.readthedocs.io/en/latest/)

## Framework Architecture

Framework is build using Page-Object-Model (POM). 
Each Webpage is modelled as an object

`environment.py` contains [environmental controls](https://behave.readthedocs.io/en/latest/tutorial.html#environmental-controls) for the behave framework.

Framework is built with 4 major folders context, features, steps and pages

#### context

Settings and driver instantiation.

#### features

Contains `.feature` files, conforming to [gherkin syntax](https://behave.readthedocs.io/en/latest/philosophy.html#the-gherkin-language).

#### steps

Where the files to implement the steps in the `.feature` files are located.

#### pages

Contains all page objects, as well as locators for finding elements on the webpages.


## Getting Started

Clone the repo, navigate to your local repository and run 

`pip3 install -r requirements.txt`

setup webdrivers:
You must have chrome downloaded and installed, and will also need to get a version of chromedriver.
Best to use package managers (brew, choco).

For Mac users, simply run:

`brew cask install chromedriver`

Windows;

`choco install chromedriver`

Ubuntu/Debian:

`apt install chromium-chromedriver`

Ensure that the chromedriver has been added to your path by your package manager.

After Chromedriver is installed, you should be ready to run the tests, simply executing command behave on the terminal

`behave`

should trigger the tests.