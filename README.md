

This code appears to be a script that is used to scrape data from a website and send a message to a Discord channel via a webhook if the data has changed.

The website appears to contain a table with information about class schedules for various groups, and the script uses the requests library to make HTTP requests to the website and the BeautifulSoup library to parse the HTML content of the resulting web pages. It then extracts the data from the table and stores it in a text file.

The script has several functions:

getGr: Makes a request to the website and parses the HTML content to extract a list of group names.

checkChanges: Compares the data from the website with the data stored in a text file and returns True if the data is the same or False if it is different.

getData: Makes a request to the website with a specific group name and parses the HTML content to extract the data from the table on the page.

main: The main function that coordinates the execution of the other functions. It gets the current time, calls getGr to get the list of group names, iterates over the list of group names, and makes a request to the website for each group name. It then calls getData to extract the data from the table on the website, and checkChanges to compare the data with the data stored in the text file. If the data is different, the function sends a message to the Discord channel via the webhook.
The project is built using python and the following library:

- discord-webhook

- lxml

- bs4

- requests

- numpy

- schedule

- time

- datetime
