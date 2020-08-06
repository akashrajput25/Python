from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.test_database
courses = db.course

course ={
    'author' : 'Akash' ,
    'course' : 'MongoDb',
    'price' : '100$',
    'rating' : 5
}

result = courses.insert_one(course)

if result.acknowledged:
    print('course added . course id is', str(result.inserted_id))
