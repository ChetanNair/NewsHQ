# News HQ
## Overview
NewsHQ is a website that scrapes top news websites and displays the top three articles on a single page. 

# Getting Started
## Dependencies
django, django-on-heroku, heroku, newspaper


## Testing Server Execution
```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

## Tools
Created using Python, Django, HTML, CSS, Bootstrap.

## Detailed Explanation
The user can input the URL to a news website that they would like to see displayed on one of the slides. When "Load Articles" is clicked, the websites are scraped and the top three articles are retrieved. These are stored in a database (SQLite for testing and Postgres for deployment). These articles are served up from the database. The articles cycle through on a regular basis and are updated daily depending on requests to the website from users. The website is deployed using Heroku.

## Try it out!
Deployed using Heroku at https://newshq.herokuapp.com

## Author

Chetan Nair - chetan.r.nair@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
