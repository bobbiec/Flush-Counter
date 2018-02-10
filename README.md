# Flush Counter
Counting toilet flushes can make more of a difference than you think.

Deployed on [Heroku](http://flush-counter.herokuapp.com).

### Details
This project is Python/Flask, with Plot.ly and R/Shiny for visualization.
Accelerometer_App is a demo app in Processing/Android to demonstrate that
toilet flushing can be detected via accelerometer. Reading


### Getting Started
To install, use pipenv
```
pip install pipenv
pipenv install
pipenv shell
```

To run, use
```
export FLASK_APP=app.py
flask run

# Or alternately
python app.py

# Or alternately
heroku local
```