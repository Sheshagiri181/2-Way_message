from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('----------------/')
filter={}

result = client['--------']['------'].find(filter=filter)
marks_result = client['--------']['--------'].find(filter=filter)
print("connected to database")
# -----------------------------Student-------------------------------------- 
@app.route('/student', methods=['GET'])
def get_students():
    students = []
    for student in result:
        student['_id'] = str(student['_id'])
        students.append(student)
    return jsonify(students)    

@app.route('/student/<Id>', methods=['GET'])
def get_student(Id):
    student = client['aagama_pr_1']['student'].find_one({"Id": Id})
    if student:
        student['_id'] = str(student['_id'])
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404 

@app.route('/student', methods=['POST'])
def add_student():
    new_student = request.get_json()
    result = client['aagama_pr_1']['student'].insert_one(new_student)
    new_student['_id'] = str(result.inserted_id)
    return jsonify(new_student), 201    

@app.route('/student/<Id>', methods=['PUT'])
def update_student(Id):
    updated_student = request.get_json()
    result = client['aagama_pr_1']['student'].update_one({"Id": Id}, {'$set': updated_student})
    if result.modified_count > 0:
        updated_student['_id'] = Id
        return jsonify(updated_student)
    else:
        return jsonify({'error': 'Student not found or no changes made'}), 404

@app.route('/student/<Id>', methods=['DELETE']) 
def delete_student(Id):
    result = client['aagama_pr_1']['student'].delete_one({"Id": Id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Student not found'}), 404

# -----------------------------Marks--------------------------------------
@app.route('/marks', methods=['GET'])
def get_marks():
    marks = []
    for mark in marks_result:
        mark['_id'] = str(mark['_id'])
        marks.append(mark)
    return jsonify(marks)       

@app.route('/marks/<Id>', methods=['GET'])  
def get_mark(Id):
    mark = client['aagama_pr_1']['marks'].find_one({"Id": Id})
    if mark:
        mark['_id'] = str(mark['_id'])
        return jsonify(mark)
    else:
        return jsonify({'error': 'Mark not found'}), 404

@app.route('/marks', methods=['POST'])      
def add_mark():
    new_mark = request.get_json()
    result = client['aagama_pr_1']['marks'].insert_one(new_mark)
    new_mark['_id'] = str(result.inserted_id)
    return jsonify(new_mark), 201

@app.route('/marks/<Id>', methods=['PUT'])  
def update_mark(Id):
    updated_mark = request.get_json()
    result = client['aagama_pr_1']['marks'].update_one({"Id": Id}, {'$set': updated_mark})
    if result.modified_count > 0:
        updated_mark['_id'] = Id
        return jsonify(updated_mark)
    else:
        return jsonify({'error': 'Mark not found or no changes made'}), 404

@app.route('/marks/<Id>', methods=['DELETE'])
def delete_mark(Id):
    result = client['aagama_pr_1']['marks'].delete_one({"Id": Id})
    if result.deleted_count > 0:
        return jsonify({'message': 'Mark deleted successfully'})
    else:
        return jsonify({'error': 'Mark not found'}), 404

# -----------------------------Student & marks--------------------------------------
@app.route('/student/full/<Id>', methods=['GET'])
def get_full_student_info(Id):
    student = client['aagama_pr_1']['student'].find_one({"Id": Id})
    if student:
        student['_id'] = str(student['_id'])
        marks = client['aagama_pr_1']['marks'].find_one({"Id": Id})
        if marks:
            marks['_id'] = str(marks['_id'])
            student['marks'] = marks
        return jsonify(student)
    else:
        return jsonify({'error': 'Student not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
