# Timetable 📊

## 📰 Description 
A CLI tool that allow you to generate a timetable for your school or university such that : 
 - A subject can't be seen on two consecutive days
 - A subject have a minimum of 2 hours per week and a maximum of 6
 - The timetable is divided in slots of 1 hours
 - The subjects are distributed between monday morning and saturady morning
 - Morning classes begin at 8:30 and end at 12:30
 - Afternoon classes begin at 13:30 and end at 17:30

 ## 📦 Installation 

 ### 💻 Local installation

To install this project locally, you first have to clone this repo and install [poetry](https://python-poetry.org/) with pip : `pip install poetry`.
Then, go to the root directory and run the following commands : 
```bash
poetry install # install all the necessary dependencies
poetry build
poetry run python -m wcc_timetable_generator 
```

 ### 🌐 Installation with PIP
 ```bash
 pip install wcc-timetable-generator
 ```

## 🖱 Usage
If you installed it with pip, this is how to run the project : 
```bash
wcc-timetable-generator
```

## ✅ Roadmap
- [x] Add the algorithm 
- [x] Add GUI-like UI
- [x] Publish to PyPI
- [ ] Add an animated GIF as demo to `README.md`
- [ ] Write tests
- [x] Add quit button
- [x] Print error messages
