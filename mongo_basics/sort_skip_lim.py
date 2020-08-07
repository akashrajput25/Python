from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.test_database
courses = db.course

arr_courses =[
    {
        'author' : 'Akash' ,
        'course' : 'MongoDb',
        'price' : '100',
        'rating' : 5
    },
    {
        'author' : 'Sritam' ,
        'course' : 'Python',
        'price' : '200',
        'rating' : 5
    },
    {
        'author' : 'Arihant' ,
        'course' : 'Java',
        'price' : '150',
        'rating' : 4
    }
]

'''courses = courses.find().sort('author' , -1 )   #descending order
courses = courses.find().sort('author' , 1 )   #ascending order
for course in courses:
    pprint.pprint(course)
'''

'''
courses = courses.find().sort([('author' , 1) , ('course' , -1)])   #sorting multiple values 
for course in courses:
    pprint.pprint(course)

'''

'''
courses = courses.find().sort([('author' , 1) , ('course' , -1)]).limit(1)   #limiting to show only one value in database
for course in courses:
    pprint.pprint(course)

'''

courses = courses.find().skip(1)   #skipping the first database value
for course in courses:
    pprint.pprint(course)