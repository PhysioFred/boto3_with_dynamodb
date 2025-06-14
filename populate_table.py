import boto3
import uuid

#DRY Code
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Murdah")

#Modularity

#Add new attributes
def add_student(name, grade, house, detention_count):
    student_id = str(uuid.uuid4())
    table.put_item(Item={
        "student_id": student_id,
        "name": name,
        "grade": grade,
        "house": house,
        "detention_court": detention_count
    })
    print(f"Added student: {student_id} ,{name}")

add_student("Ivan Milat", 11, "Red", 3)
add_student("Ted Bundy", 12, "Blue", 1)