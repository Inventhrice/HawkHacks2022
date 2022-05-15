# HawkHacks2022 - To-Do List with Django

This is a web application developed with Python, Django and Bootstrap.  
It provides the basic CRUD functions.

## To Start

To play with this app, you should firstly install Django: `pip install django`

> For more details, check this [How to install Django](https://docs.djangoproject.com/en/4.0/topics/install/)

Then **pull** the main branch of our project through Github.

**Open the project folder** in your terminal.

Use this command `python manage.py runserver`
to **run the app at port 8000** in your local machine.(You can also specify another port if there are conflications: `python manage.py runserver 8888` )

Then open this url(<http://127.0.0.1:8000/>) in your **browser**.

We are done. Welcome to your to-do list!

## CRUD Operations

### Add tasks

---

![image](/res/add.png)  
Type in the input box and press enter or click the 'Add' button.

### Update

---

![image](/res/update.png)
Click the 'Update' button and it will redirect to this page.  
Click 'Save' to summit your changes.

### Delete

---

![image](/res/delete.png)  
Click the 'Delete' button and it will redirect to this page.  
Click 'Yes' to confirm the deletion; otherwise, click 'No' to cancel it.

### Checkbox

---

![image](/res/checkbox.png)  
Simply click to strike or unstrike the task.
At present, the changed task state will not be saved into database.

> **If you refresh the page, all the tasks will be unchecked.**

To change the task state in datebase, you need to **click 'Update'**, check the complete box and **'Save'**. We will fix this later.

## Future improvements

1. Save the state change via checkbox into database
2. Time and Date attribute of the Task model: so we can implement a Reminder function for this app
3. Calendar view: give a overview of all tasks schduled in a specific time period
4. Tag and Priority level attribute: group and classify the tasks and choose which oned to be displayed on the webpage
5. Sort functions: sort by time, date, priority or tags
6. others

**Anyone is welcomed to fork and contribute**
