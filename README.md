# Vehicle Task Manager

## Overview

The Vehicle Task Manager is a PyQt5-based application that allows users to manage car details and maintenance tasks associated with each car. It provides a graphical user interface (GUI) where users can add, remove, and view car details and maintenance tasks. The application uses a SQLite database to store the data.




### Prerequisites
Python 3.x

PyQt5 library

SQLite






### Usage


To start the Vehicle task manager, follow the steps below:

Run the following command:

``` python3 main.py ```


## Car Management

The application allows you to add, remove, and modify car details in the database. Follow the steps below to manage car details:


*To add a new car:*


Enter the car details in the input fields provided (Car ID, Year, Make, Model).
Click the Add Car button to save the car details.



*To remove a car:*

Highlight the entire row in the car table by clicking the small bar on the left side of the row.
Click the Remove Car button. Removing a car will also delete all tasks asociated with that car



*To modify a car detail:*

Highlight the cell you want to modify by double-clicking on it.
Enter new text directly in the highlighted cell.
Press the Enter key to save the changes.




##Task Management


You can add, remove, and modify maintenance tasks associated with each car. Follow the steps below to manage tasks:

*To add a new task:*

Enter the task details in the input fields provided (Task Name, Car ID).
Click the Add Task button to save the task details.


*To remove a task:*

Highlight the entire row in the task table by clicking the small bar on the left side of the row.
Click the Remove Task button.


*To modify a task detail:*

Highlight the cell you want to modify by clicking on it.
Enter new text directly in the highlighted cell.
Press the Enter key to save the changes.

## Screenshot




![image](https://github.com/DancesWithDobes/vehicle_task_manager/assets/69741804/105a9c46-114a-4a7c-89ee-a4ceb9476092)


# Note:

To delete a car or task, ensure that the corresponding row is highlighted in the table. You can click the small bar on the left side of the row to select it.
Cells in the tables can be modified by simply highlighting the value, entering new text, and pressing the Enter key to save the changes.


*Database Setup*

The application requires the schema.sql file to set up the database structure and the vehicle_maintenance.db file to store the data. Both files should be located in the same directory as the main.py file.


