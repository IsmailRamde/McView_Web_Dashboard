<<<<<<< HEAD
# Dash McView

This is an interactive Python Dash developed to meet McPhy's current needs.
Dash abstracts all the technologies and protocols required to create an interactive web application and provides a simple and efficient way to bind a user interface to Python code. For more information, see the [documentation](https://plot.ly/dash).

## Getting Started

### Running the app locally

First create a virtual environment with conda or venv inside a temp folder, then activate it.

```
virtualenv venv

# Windows
venv\Scripts\activate
# Or Linux
source venv/bin/activate

```
Download the folder on your computer or
Clone the git repo, then install the requirements with pip

```
In your terminal type :
- git clone [the link of the project on github]
- cd [position yourself in the folder]
- pip install -r requirements.txt or :
  * pip install dash
  *pip install jypyter-dash
  *pip install pandas

```

Run the app

```

python app.py

After execution of the script app.py we obtain :
$ python app.py
...Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

open this link: http://127.0.0.1:8050/ to see the application

```

## About the app

This Dash application displays in real time the evolution of various data from McPhy hydrogen stations (temperature, pressure, flow), data from the engines, energy consumption and a satellite representation of all stations with their status. There are filters at the top of the application to update the graphs below. By selecting or hovering over the data in one graph, the other graphs will be updated ("cross-filtering").

## Built With

- [Dash](https://dash.plot.ly/) - Main server and interactive components
- [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots


## Access the detailed project documentation

### html
You can access the html page directly as follows:
```
docs → _build → html → then open the file index.html
```

vous avez la possibilité de le faire à partir du terminal :
```
pip install -U Sphinx
sudo apt-get install python3-sphinx
pip install sphinx-rtd-theme
make html
firefox build/html/index.html
```
Do not hesitate to consult the complete documentation of sphinx by following this link : https://he-arc.github.io/livre-python/sphinx/index.html#enumerate 

### pdf
```
docs → _build → latex → then open the file mcviewwebdashboard.pdf
```


## Screenshots

The following are screenshots for the app in this repo:

![animated1](/home/ismael/Bureau/plotly/McView_WebDashboard/assets/cap1.png)

![screenshot](/home/ismael/Bureau/plotly/McView_WebDashboard/assets/cap3.png)

![screenshot](/home/ismael/Bureau/plotly/McView_WebDashboard/assets/cap2.png)

=======
# Dash McView

This is an interactive Python Dash developed to meet McPhy's current needs.
Dash abstracts all the technologies and protocols required to create an interactive web application and provides a simple and efficient way to bind a user interface to Python code. For more information, see the [documentation](https://plot.ly/dash).

## Getting Started

### Running the app locally

First create a virtual environment with conda or venv inside a temp folder, then activate it.

```
virtualenv venv

# Windows
venv\Scripts\activate
# Or Linux
source venv/bin/activate

```
Download the folder on your computer or
Clone the git repo, then install the requirements with pip

```
In your terminal type :
- git clone [the link of the project on github]
- cd [position yourself in the folder]
- pip install -r requirements.txt or :
  * pip install dash
  *pip install jypyter-dash
  *pip install pandas

```

Run the app

```

python app.py

After execution of the script app.py we obtain :
$ python app.py
...Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)

open this link: http://127.0.0.1:8050/ to see the application

```

## About the app

This Dash application displays in real time the evolution of various data from McPhy hydrogen stations (temperature, pressure, flow), data from the engines, energy consumption and a satellite representation of all stations with their status. There are filters at the top of the application to update the graphs below. By selecting or hovering over the data in one graph, the other graphs will be updated ("cross-filtering").

## Built With

- [Dash](https://dash.plot.ly/) - Main server and interactive components
- [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots


## Access the detailed project documentation

### html
You can access the html page directly as follows:
```
docs → _build → html → then open the file index.html
```

vous avez la possibilité de le faire à partir du terminal :
```
pip install -U Sphinx
sudo apt-get install python3-sphinx
pip install sphinx-rtd-theme
make html
firefox build/html/index.html
```
Do not hesitate to consult the complete documentation of sphinx by following this link : https://he-arc.github.io/livre-python/sphinx/index.html#enumerate 

### pdf
```
docs → _build → latex → then open the file mcviewwebdashboard.pdf
```


## Screenshots

The following are screenshots for the app in this repo:

![animated1](/home/ismael/Bureau/plotly/McView_WebDashboard/assets/cap1.png)

![screenshot](/home/ismael/Bureau/plotly/McView_WebDashboard/assets/cap3.png)

![screenshot](/home/ismael/Bureau/plotly/McView_WebDashboard/assets/cap2.png)

>>>>>>> a5ceafc3d0edd9e29a7b746aa6888a004a60c22e
