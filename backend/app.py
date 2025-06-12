from flask import Flask, request, jsonify
from models import db, Meeting, Lesson, Test, Opinion, Student, Course, Teacher, student_course
from config import Config
from datetime import datetime
from flask_cors import CORS
from werkzeug.security import generate_password_hash
from uuid import UUID
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

@app.route('/lessons', methods=['POST'])
def create_lesson():
    try:
        data = request.get_json()

        if not data or 'title' not in data or 'course_id' not in data:
            return jsonify({'error': 'Tytuł i id kursu są wymagane'}), 400

        course = Course.query.get(data['course_id'])
        if not course:
            return jsonify({'error': 'Nie ma kursu o podanym id'}), 404

        new_lesson = Lesson(
            title=data['title'],
            content=data.get('content', {}),
            course_id=data['course_id']
        )

        db.session.add(new_lesson)
        db.session.commit()

        return jsonify({
            'message': 'Lekcja dodana pomyślnie',
            'lesson': new_lesson.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/lessons/<uuid:lesson_id>', methods=['DELETE'])
def delete_lesson(lesson_id):
    try:
        lesson = Lesson.query.get(lesson_id)
        if not lesson:
            return jsonify({'error': ['Lekcja o podanym id nie istnieje']}), 404

        db.session.delete(lesson)
        db.session.commit()

        return jsonify({'message': ['Lekcja usunięta pomyślnie'], 'lesson': lesson.to_dict()}), 200

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500

@app.route('/courses/<uuid:course_id>/tests', methods=['GET'])
def get_tests_by_course(course_id):
    tests = Test.query.filter_by(course_id=course_id).all()
    return jsonify([t.to_dict() for t in tests]), 200

@app.route('/tests', methods=['POST'])
def create_test():
    try:
        data = request.get_json()

        if not data or 'title' not in data or 'course_id' not in data:
            return jsonify({'error': 'Tytuł i id kursu są wymagane'}), 400

        course = Course.query.get(data['course_id'])
        if not course:
            return jsonify({'error': 'Nie ma kursu o podanym id'}), 404

        new_test = Test(
            title=data['title'],
            content=data.get('content', {}),
            grade=data.get('grade'),
            course_id=data['course_id']
        )

        db.session.add(new_test)
        db.session.commit()

        return jsonify({
            'message': 'Test dodany pomyślnie',
            'test': new_test.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/tests/<uuid:test_id>', methods=['DELETE'])
def delete_test(test_id):
    try:
        test = Test.query.get(test_id)
        if not test:
            return jsonify({'error': ['Test o podanym id nie istnieje']}), 404

        db.session.delete(test)
        db.session.commit()

        return jsonify({'message': ['Test usunięty pomyślnie'], 'test': test.to_dict()}), 200

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({'error': str(e)}), 500

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

@app.route('/teachers', methods=['GET'])
def get_teachers():
    try:
        teachers = Teacher.query.all()
        return jsonify([teacher.to_dict() for teacher in teachers]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/teachers/<uuid:teacher_id>', methods=['GET'])
def get_teacher_by_id(teacher_id):
    try:
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            return jsonify({'error': 'Teacher not found'}), 404
        return jsonify(teacher.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/students/register', methods=['POST'])
def register_student():
    data = request.get_json()

    required_fields = ['name', 'username', 'email', 'password', 'level']
    missing = [field for field in required_fields if not data.get(field)]

    if missing:
        return jsonify({
            'error': [f"Pole '{field}' nie może być puste." for field in missing]
        }), 400

    if Student.query.filter((Student.email == data['email']) | (Student.username == data['username'])).first():
        return jsonify({
            'error': ['Użytkownik o podanym e-mailu lub nazwie użytkownika już istnieje.']
        }), 400

    try:
        new_student = Student(
            name=data['name'],
            username=data['username'],
            email=data['email'],
            level=data.get('level', 'basic')
        )
        new_student.set_password(data['password'])
        db.session.add(new_student)
        db.session.commit()
        return jsonify({
            'success': 'Konto zostało poprawnie utworzone!',
            'student': new_student.to_dict()
        }), 201

    except Exception as e:
        return jsonify({
            'error': [f'Wystąpił błąd przy tworzeniu konta: {str(e)}']
        }), 500


@app.route('/students/login', methods=['POST'])
def login_student():
    data = request.get_json()

    # Sprawdzenie pustych pól
    missing = [field for field in ['username', 'password'] if not data.get(field)]
    if missing:
        return jsonify({
            'error': [f"Pole '{field}' nie może być puste." for field in missing]
        }), 400

    student = Student.query.filter_by(username=data['username']).first()
    if student and student.check_password(data['password']):
        return jsonify({'message': 'Zalogowano pomyślnie', 'student': student.to_dict()}), 200

    return jsonify({'error': ['Nieprawidłowy login lub hasło.']}), 401


@app.route('/students/<uuid:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()

    if all(not data.get(field) for field in ['name', 'username', 'email', 'level']):
        return jsonify({'error': ['Wszystkie pola są puste. Nie można zaktualizować użytkownika.']}), 400

    student = Student.query.get(student_id)
    if not student:
        return jsonify({'error': ['Student nie został znaleziony.']}), 404

    if data.get('name'): student.name = data['name']
    if data.get('username'): student.username = data['username']
    if data.get('email'): student.email = data['email']
    if data.get('level'): student.level = data['level']

    db.session.commit()
    return jsonify({'message': 'Student zaktualizowany', 'student': student.to_dict()}), 200

@app.route('/students/<uuid:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({
                'error': ['Nie znaleziono studenta o podanym identyfikatorze.']
            }), 404

        db.session.delete(student)
        db.session.commit()

        return jsonify({
            'success': 'Student został pomyślnie usunięty.'
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': [f'Wystąpił błąd przy usuwaniu studenta: {str(e)}']
        }), 500

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

    required_fields = ['name', 'username', 'email', 'password', 'specialty', 'experience']
    missing = [field for field in required_fields if not data.get(field)]

    if missing:
        return jsonify({
            'error': [f"Pole '{field}' nie może być puste." for field in missing]
        }), 400

    if Teacher.query.filter((Teacher.email == data['email']) | (Teacher.username == data['username'])).first():
        return jsonify({
            'error': ['Użytkownik o podanym e-mailu lub nazwie użytkownika już istnieje.']
        }), 400

    try:
        new_teacher = Teacher(
            name=data['name'],
            username=data['username'],
            email=data['email'],
            specialty=data['specialty'],
            description=data.get('description', ''),
            experience=data['experience']
        )
        new_teacher.set_password(data['password'])
        db.session.add(new_teacher)
        db.session.commit()
        return jsonify({
            'success': 'Konto zostało poprawnie utworzone!',
            'teacher': new_teacher.to_dict()
        }), 201

    except Exception as e:
        return jsonify({
            'error': [f'Wystąpił błąd przy tworzeniu konta: {str(e)}']
        }), 500

@app.route('/teachers/<uuid:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
    data = request.get_json()

    if all(not data.get(field) and data.get(field) != 0 for field in ['name', 'username', 'email', 'specialty', 'experience', 'description']):
        return jsonify({'error': ['Wszystkie pola są puste. Nie można zaktualizować użytkownika.']}), 400

    teacher = Teacher.query.get(teacher_id)
    if not teacher:
        return jsonify({'error': ['Nauczyciel nie został znaleziony.']}), 404

    if data.get('name'): teacher.name = data['name']
    if data.get('username'): teacher.username = data['username']
    if data.get('email'): teacher.email = data['email']
    if data.get('specialty'): teacher.specialty = data['specialty']
    if data.get('description') is not None: teacher.description = data['description']
    if data.get('experience') is not None: teacher.experience = data['experience']

    db.session.commit()
    return jsonify({'message': 'Nauczyciel zaktualizowany', 'teacher': teacher.to_dict()}), 200

@app.route('/teachers/<uuid:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    try:
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            return jsonify({
                'error': ['Nie znaleziono nauczyciela o podanym identyfikatorze.']
            }), 404

        if teacher.courses:
            return jsonify({
                'error': ['Nie można usunąć nauczyciela, który ma przypisane kursy.']
            }), 400

        db.session.delete(teacher)
        db.session.commit()
        return jsonify({
            'success': 'Nauczyciel został pomyślnie usunięty.'
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': [f'Wystąpił błąd przy usuwaniu nauczyciela: {str(e)}']
        }), 500

@app.route('/teachers/login', methods=['POST'])
def login_teacher():
    data = request.get_json()

    # Sprawdzenie pustych pól
    missing = [field for field in ['username', 'password'] if not data.get(field)]
    if missing:
        return jsonify({
            'error': [f"Pole '{field}' nie może być puste." for field in missing]
        }), 400

    teacher = Teacher.query.filter_by(username=data['username']).first()
    if teacher and teacher.check_password(data['password']):
        return jsonify({'message': 'Zalogowano pomyślnie', 'teacher': teacher.to_dict()}), 200

    return jsonify({'error': ['Nieprawidłowy login lub hasło.']}), 401

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

    return jsonify([course.to_dict() for course in student.courses]), 200

@app.route('/teachers/<uuid:teacher_id>/courses', methods=['GET'])
def get_courses_for_teacher(teacher_id):
    courses = Course.query.filter_by(teacher_id=teacher_id).all()
    return jsonify([course.to_dict() for course in courses]), 200

@app.route('/students/<uuid:student_id>/meetings', methods=['GET'])
def get_meetings_for_user(student_id):
    meetings = Meeting.query.filter_by(student_id=student_id).all()

    return jsonify([m.to_dict() for m in meetings]), 200

@app.route('/teachers/<uuid:teacher_id>/meetings', methods=['GET'])
def get_meetings_for_teacher(teacher_id):
    meetings = Meeting.query.filter_by(teacher_id=teacher_id).all()
    return jsonify([m.to_dict() for m in meetings]), 200

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
    return jsonify({'message': 'Course created', 'course': new_course.to_dict()})

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
    teacher_courses = Course.query.filter_by(teacher_id=teacher_id).all()
    counts = []
    for course_id in set([c.id for c in teacher_courses]):
        results = db.session.query(student_course).filter_by(course_id=course_id).count()
        counts.append({'course_id': course_id, 'count': results})
    return jsonify(counts)

@app.route('/courses/<uuid:course_id>/students', methods=['GET'])
def get_students_for_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify([{
        'student_id': str(s.id),
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
