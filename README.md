# Final Project Assignment

### Requirements
For your final project, you will write various Python programs that accesses a MySQL database. Your project should include the following:

1. A SQL script that contains
    - a physical implementation for your database (database, tables, constraints, indexes)
    - statements that inserts sample data into your database
    - statements that create a user and grants appropriate access to the user.  This user will access the database in your Python programs.



3. Python programs that do the following:
    - display all of the relevant data, excluding data that isn’t relevant to a user such as autonumber keys
    - allow the user to filter the display on some criteria
    - allow users to add data to the database and prevent SQL injection attacks
    - allow users to edit or delete data in the database and prevent SQL injection attacks


### Grading
This project is worth **70 points**.
|Criteria|points|
| -- | -- |
| A SQL script is included that creates the database and tables| 5 |
|Attributes have reasonable data types|7 |
|Primary key constraints are included for all tables|7 |
|Foreign key constraints are included for all relationships|8 |
|Indexes are created for fields frequently queried but not for fields that are primary keys or foreign keys|7 |
|The script inserts sample data into tables|5 |
|Python program(s) that display all of the relevant data, excluding data that isn’t relevant to a user, such as auto number keys|8 |
|Python program(s) that filter data based on some criteria|8 |
|Python program(s) that allow users to add data to the database and prevent SQL injection attacks|5 |
|Python program(s) that allow users to edit or delete data in the database and prevent SQL injection attacks|5 |
|Assignment is submitted on time and via GitHub|5 |

### Assignment Submission

Push all files required to create your database and python files to your **GitHub repository**.

```
git add .
git commit -m "completed final project"
git push
```
**Submit the assignment in Blackboard**, including a link to your GitHub repository in the comment section of the assignment.

**This assignment is due no later than 11:59 PM on Tuesday, December 15th.**
