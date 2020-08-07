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


'''
print(courses.find({'author':'Akash'}).count())
courses.delete_one({
    'author': 'Akash'
})


print(courses.find({'author':'Akash'}).count())

'''

print(courses.find({'author':'Arihant'}).count())
courses.delete_many({
    'author': 'Arihant'
})


print(courses.find({'author':'Arihant'}).count())
