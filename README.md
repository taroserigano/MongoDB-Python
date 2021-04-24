# MongoDB-Python

CS 340 README 
Taro Serigano
3/27/2021

OBJECTIVES

This school project is building the architecture that lets you build and manage MongoDB databases that is connected to the application. We will also implement Create, Read, Delete and Update functionality known as CRUD in order to keep the data in the database organized and provide the best performance of the database system.


Motivation
This is a short description of the motivation behind the creation and maintenance of the project. This should explain why the project exists.

The CRUD operation technology is a very common and pretty much a “standard” in today’s IT industry. Creating such technology and maintain the database system is a crucial skill to anybody who works for the IT industry and that is why we have to earn these skills.


Getting Started
This is an example of how you may give instructions on setting up your project locally: “To get a local copy up and running, follow these simple example steps.”


Installation
List the tools you need to use the software and how to install them.

You would need following items installed in order to engage in this project: 
1.	MongoDB
2.	Mongo Shell
3.	Jupyter Notebook 
4.	Python IDE (PyCharm is recommended)


Usage
Use this space to show useful examples of how your project works and how it can be used. Be sure to include examples of your code, tests, and screenshots.

Code Example
Show what the library does as concisely as possible. Developers should be able to figure out how your project solves their problem by looking at the code example. Make sure that your code is short and concise.

 


In order for you to access the database, replace the “user_name” and “pass_word” with your own. Once the access is gained, you may perform the “read” with search of your criteria. When you entered the criteria, Data = self.database.animals.find(criteria, {“_id”:False}) will  store the result into the “data”, whill will be returned. If no criteria was selected, the code will simply output all the data stored in the database. 












Tests
Describe and show how to run the tests with code examples.


 


Test execution gets performed in “main.py”. We will also import another py file, “CRUD.py”.

Here, we simply created 3 rows of data. The code then perform for-loop and collect all the data and then perform the “read” operation and filter out only the “dog” type. The result then will be printed out as the below screenshot:

 


Screenshots
Provide screenshots that demonstrate your work.



REFLECTION

•	How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?


I use object-oriented programming principles and extensively comment my code to create such maintainable-readable-adaptable programs. When it comes to the CRUD-based model, writing it this way means that I can quickly adapt it to function in a variety of different situations. In order to give some flexibility and make it more versatile, I think I could give something like databaseSelect() process.
•	How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

As CS student, breaking down a problem into smaller pieces and solving each part separately while keeping the big picture in mind is important. I believe it is important to test the integration of the smaller components as soon as possible in order to ensure that I identify and address problems as quickly as possible. My method was similar to that of prior projects and course works given in previously taken classes. I looked at each requirement and classified it as "independent"or"dependent," meaning whether or not it is dependent on me meeting another requirement first. After that, I begin writing code for the independent specifications.
•	What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

CS students address issues by devising technical solutions that are both safe and effective. These approaches improve both efficiency and overall our life styles by reducing the time it takes to complete tasks, giving plenty of time for pursuing word and resting. Thus, this kind of technology could boosts the competitiveness of a business like Grazioso Salvare by drastically reducing the time it takes to find the resources you needed.





Contact

Should you have the need to contact me, please contact me via the following info:
Your name: Taro Serigano
Email: taro.serigano167@snhu.edu
