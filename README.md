# COSI103-PA3

***** PA03 Introduction *****

Transaction.py is an Object-Relational Mapping (ORM) module that interacts with the tracker.db database.

The ORM will map SQL rows with the schema
(id, date, description, amount, category_id)
to Python Dictionaries as follows:
{id:1, date:'2022-03-28', description:'Grocery shopping', amount: 100.00, category_id:1}
In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database named tracker.db
The class Transaction provides various methods for accessing and manipulating data, including getting ,adding and modifying categories, adding and deleting transactions, and summarizing transactions by date, month, year, or category etc.

In addition, the ORM includes a method run_query() that connects to the database, executes a query with parameters, fetches the rows, and closes the connection. The method catches and ignores any errors that may occur during the database interaction.


***** Pylint Script *****
```
pylint transaction.py
```

***** How to run tracker *****
```
python3 tracker.py
```
If the user enter 0, the program will quit
If the user eneter 1, the program will show all categories
For example
```
Enter an option: 1
Categories:
1. food
2. snake
3. fruit
```
If the user eneter 2, the program will add a category
For example
```
Enter an option: 2 food
Enter an option: 2 snake
Enter an option: 2 fruit
```
If the user eneter 3, the program will modify category
```
Enter an option: 3 food veg

Enter an option: 1
Categories:
1. veg
2. snake
3. fruit
```
If the user eneter 4, the program will show transactions
```
Enter an option: 4
(1, 'Snack', 5.99, '2021-03-26', 1)
(2, 'Food', 7.99, '2021-03-26', 2)
(3, 'Snack', 9.99, '2022-03-27', 1)
(4, 'Food', 10.99, '2022-03-27', 2)
(5, 'Food', 7.99, '2022-04-10', 2)
(6, 'Snack', 9.99, '2022-04-11', 1)
(7, 'Food', 7.99, '2023-03-01', 2)
(8, 'Snack', 9.99, '2023-03-02', 1)
(9, 'Food', 10.99, '2023-05-02', 2)
```


***** PA03 Assignment Introduction *****

PA03 - finance tracker - using SQL, pytest, and pylint

Motivation
Many software projects use SQLite to manage their data and this problem set will give you the experience of building such an app.  Another important process in software engineering is the design of automated tests.  This assignment will ask you to develop a suite of tests for your app. There are other database and testing frameworks, but they are all similar in principle and this assignment will expose you to the core concepts and skills you'll need.


Learning Objectives -
* to write SQL queries to perform the CRUD operations (Create, Read, Update, Delete) and aggregation(with SQLite3)
* to develop automated testing (with pytest)

Steps:
1) create a git repository to contain the pa03 code, which you then push to github
2) add all members of the team as collaborators
3) create a Python class Transaction in a new file transaction.py which will store financial transactions with the fields. 
It should have an __init__ method where you pass in the filename for the database to be used (e.g. tracker.db) 
and each transaction should have the following fields stored in a SQL table called transactions.

'item #',
'amount',
'category',
'date',
'description'

It should be similar to the Todolist ORM from Lesson 19 in class. It will allow the user to read and update the database as need.
The transaction class should not do any printing!! 

Create a file tracker.py which offers the user the following options and makes calls to the Transaction class to update the database.

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

The tracker.py program should not have any SQL calls and should be similar is structure to the todo2.py program from Lesson19

Testing with pytest -- 
create a file, test_transaction.py, and addtests to it for each method in the Transaction class. 
It is a good idea to add a test each time you implement a feature. 
You are testing the Transaction class, not the tracker.py user interface code.

Linting with pylint --
Use pylint with transactions.py and tracker.py and eliminate all of the style errors that it flags. Try to get 100% compliance.

Collaborating with github -- 
regularly commit your changes and push them to github, every team member should push some changes of their own. I suggest you have each person implement a few of the options in tracker.py and everyone collaborate on the operations needed for the ORM transaction.py

Creating a transcript - 
create a transcript of your session as you demonstrate each of the features you have implemented. 
create a README.md file which describes your app and contains 
* a script of you running pylint, and 
* then running pytest, and 
* then running tracker.py and demonstrating all of the features you added

Try to make sure that everyone gets to work on some substantial part of the project.
 
What to upload to mastery.cs.brandeis.edu (programs)
* a link to your github
* a reflection where you state what you did personally on the project 
(you should put your name in the comments of each method you personally write....). 
We can use the "blame" feature in the github repository to see what each person did, but its easier if you just tell us!
