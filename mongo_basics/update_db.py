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

courses.update({
    'course' : 'Java'
},
{
    '$set' : {
        'course' : 'Advanced Java'
    }
},multi = True)


courses = courses.find({'course' : 'Advanced Java'})
for course in courses:
    pprint.pprint(course)
