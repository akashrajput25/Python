from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.test_database
courses = db.course

courses.create_index(
    [('study' , 1 )]
,unique = True)

arr_courses =[
    {
        'author' : 'SK Verma' ,
        'course' : 'MongoDb',
        'price' : '100',
        'rating' : 5
    },
    {
        'author' : 'Sritam K Das' ,
        'course' : 'Python',
        'price' : '200',
        'rating' : 5
    },
    {
        'author' : 'Orielly' ,
        'course' : 'Java',
        'price' : '150',
        'rating' : 4
    }
]

results = courses.insert_many(arr_courses)

for object_id in results.inserted_ids:
    print('course added and course id is', str(object_id))