from flask import Flask, request, jsonify
from models import db, Meeting, Lesson, Test, Opinion, Student, Course, Teacher
from config import Config
from datetime import datetime
from flask_cors import CORS, cross_origin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_object(Config)
db.init_app(app)

@app.route('/meetings', methods=['POST'])
def add_meeting():
    data = request.get_json()
    try:
        new_meeting = Meeting(
            title=data['title'],
            description=data.get('description'),
            status=data['status'],
            link=data.get('link'),
            start_date=datetime.strptime(data['start_date'], '%Y-%m-%d %H:%M:%S'),
            end_date=datetime.strptime(data['end_date'], '%Y-%m-%d %H:%M:%S'),
            student_id=uuid.UUID(data['student_id']),
            teacher_id=uuid.UUID(data['teacher_id'])
        )
        db.session.add(new_meeting)
        db.session.commit()
        return jsonify({'message': 'Meeting added', 'meeting': new_meeting.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/courses/<uuid:course_id>/lessons', methods=['GET'])
def get_lessons_by_course(course_id):
    lessons = Lesson.query.filter_by(course_id=course_id).all()
    return jsonify([l.to_dict() for l in lessons]), 200

@app.route('/courses/<uuid:course_id>/tests', methods=['GET'])
def get_tests_by_course(course_id):
    tests = Test.query.filter_by(course_id=course_id).all()
    return jsonify([t.to_dict() for t in tests]), 200

@app.route('/courses/<uuid:course_id>/opinions', methods=['POST'])
def add_opinion(course_id):
    data = request.get_json()
    try:
        new_opinion = Opinion(
            title=data['title'],
            content=data.get('content', ''),
            score=data['score'],
            course_id=course_id
        )
        db.session.add(new_opinion)
        db.session.commit()
        return jsonify({'message': 'Opinion added', 'opinion': new_opinion.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/courses/<uuid:course_id>/opinions', methods=['GET'])
def get_opinions_by_course(course_id):
    opinions = Opinion.query.filter_by(course_id=course_id).all()
    return jsonify([op.to_dict() for op in opinions]), 200

@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        return jsonify([course.to_dict() for course in courses]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/students/register', methods=['POST'])
def register_student():
    data = request.get_json()
    if Student.query.filter((Student.email == data['email']) | (Student.username == data['username'])).first():
        return jsonify({'error': 'Email or username already exists'}), 400

    new_student = Student(
        name=data['name'],
        username=data['username'],
        email=data['email'],
        level=data.get('level', 'basic')
    )
    new_student.set_password(data['password'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student registered', 'student': new_student.to_dict()}), 201

@app.route('/students/login', methods=['POST'])
def login_student():
    data = request.get_json()
    student = Student.query.filter_by(username=data['username']).first()
    if student and student.check_password(data['password']):
        return jsonify({'message': 'Login successful', 'student': student.to_dict()})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/students/forgot', methods=['POST'])
def forgot_password():
    data = request.get_json()
    student = Student.query.filter_by(email=data['email']).first()
    if not student:
        return jsonify({'error': 'Email not found'}), 404

    student.set_password(data['new_password'])
    db.session.commit()
    return jsonify({'message': 'Password updated successfully'})

@app.route('/teachers/register', methods=['POST'])
def register_teacher():
    data = request.get_json()
    if Teacher.query.filter((Teacher.email == data['email']) | (Teacher.username == data['username'])).first():
        return jsonify({'error': 'Email or username already exists'}), 400

    new_teacher = Teacher(
        name=data['name'],
        username=data['username'],
        email=data['email'],
        specialty=data.get('specialty', 'other'),
        description=data.get('description', ''),
        experience=data.get('experience', 0)
    )
    new_teacher.password = generate_password_hash(data['password'])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({'message': 'Teacher registered', 'teacher_id': new_teacher.to_dict()}), 201

@app.route('/teachers/login', methods=['POST'])
def login_teacher():
    data = request.get_json()
    teacher = Teacher.query.filter_by(username=data['username']).first()
    if teacher and check_password_hash(teacher.password, data['password']):
        return jsonify({'message': 'Login successful', 'teacher': teacher.to_dict()})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/teachers/forgot', methods=['POST'])
def forgot_teacher_password():
    data = request.get_json()
    teacher = Teacher.query.filter_by(email=data['email']).first()
    if not teacher:
        return jsonify({'error': 'Email not found'}), 404

    teacher.password = generate_password_hash(data['new_password'])
    db.session.commit()
    return jsonify({'message': 'Password updated successfully'})

@app.route('/students/<uuid:student_id>/courses', methods=['GET'])
def get_courses_for_student(student_id):
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify([
        {
            'course_id': str(course.id),
            'title': course.title,
            'level': course.level,
            'price': course.price
        } for course in student.courses
    ]), 200

@app.route('/students/<uuid:student_id>/meetings', methods=['GET'])
def get_meetings_for_user(student_id):
    meetings = Meeting.query.filter_by(student_id=student_id).all()

    return jsonify([{
        'meeting_id': str(m.meeting_id),
        'title': m.title,
        'status': m.status,
        'start_date': m.start_date.isoformat(),
        'end_date': m.end_date.isoformat()
    } for m in meetings]), 200

@app.route('/courses/<uuid:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    data = request.get_json()
    for field in ['title', 'subject', 'description', 'level', 'duration', 'price', 'score']:
        if field in data:
            setattr(course, field, data[field])

    db.session.commit()
    return jsonify({'message': 'Course updated'})

@app.route('/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Course(
        title=data['title'],
        subject=data.get('subject', ''),
        description=data.get('description', ''),
        level=data.get('level', 'basic'),
        duration=data.get('duration', 0),
        price=data.get('price', 0),
        score=data.get('score', 0),
        teacher_id=data['teacher_id']
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created', 'course_id': new_course.to_dict()})

@app.route('/courses/<uuid:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted'})

@app.route('/meetings/<uuid:meeting_id>', methods=['PUT'])
def update_meeting(meeting_id):
    meeting = Meeting.query.get(meeting_id)
    if not meeting:
        return jsonify({'error': 'Meeting not found'}), 404

    data = request.get_json()
    for field in ['title', 'description', 'status', 'link', 'start_date', 'end_date']:
        if field in data:
            setattr(meeting, field, data[field])

    db.session.commit()
    return jsonify({'message': 'Meeting updated'})

@app.route('/meetings/<uuid:meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    meeting = Meeting.query.get(meeting_id)
    if not meeting:
        return jsonify({'error': 'Meeting not found'}), 404

    db.session.delete(meeting)
    db.session.commit()
    return jsonify({'message': 'Meeting deleted'})

@app.route('/teachers/<uuid:teacher_id>/courses/count', methods=['GET'])
def get_number_of_bought_courses(teacher_id):
    count = Course.query.filter_by(teacher_id=teacher_id).count()
    return jsonify({'count': count})

@app.route('/courses/<uuid:course_id>/students', methods=['GET'])
def get_students_for_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify([{
        'student_id': str(s.student_id),
        'name': s.name,
        'email': s.email
    } for s in course.students])

@app.route('/courses/<uuid:course_id>/students/<uuid:student_id>', methods=['POST'])
def add_student_to_course(course_id, student_id):
    course = Course.query.get(course_id)
    student = Student.query.get(student_id)
    if not course or not student:
        return jsonify({'error': 'Student or Course not found'}), 404

    course.students.append(student)
    db.session.commit()
    return jsonify({'message': 'Student added to course'})

@app.route('/courses/<uuid:course_id>/students/<uuid:student_id>', methods=['DELETE'])
def delete_student_from_course(course_id, student_id):
    course = Course.query.get(course_id)
    student = Student.query.get(student_id)
    if not course or not student:
        return jsonify({'error': 'Student or Course not found'}), 404

    if student in course.students:
        course.students.remove(student)
        db.session.commit()
        return jsonify({'message': 'Student removed from course'})
    return jsonify({'error': 'Student not enrolled in course'}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
