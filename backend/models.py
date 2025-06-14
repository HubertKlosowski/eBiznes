from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
import uuid


db = SQLAlchemy()

class Meeting(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('scheduled', 'completed', 'cancelled', name='meeting_status'), nullable=False)
    link = db.Column(db.String(100))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey('students.id'))
    teacher_id = db.Column(UUID(as_uuid=True), db.ForeignKey('teachers.id'))

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'link': self.link,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'student_id': str(self.student_id),
            'teacher_id': str(self.teacher_id)
        }

class Lesson(db.Model):
    __tablename__ = 'lessons'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100))
    content = db.Column(db.JSON)
    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey('courses.id'))

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content,
            'course_id': str(self.course_id)
        }

class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100))
    content = db.Column(db.JSON)
    grade = db.Column(db.Float)
    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey('courses.id'))

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content,
            'grade': self.grade,
            'course_id': str(self.course_id)
        }

class Opinion(db.Model):
    __tablename__ = 'opinions'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    score = db.Column(db.Integer)
    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey('courses.id'))

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'content': self.content,
            'score': self.score,
            'course_id': str(self.course_id)
        }

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    avatar = db.Column(db.LargeBinary)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    level = db.Column(db.Enum('podstawowka', 'liceum', 'technikum', 'studia', name='student_level'))

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'level': self.level
        }

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    avatar = db.Column(db.LargeBinary)  # BLOB = binary data
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    specialty = db.Column(db.Enum('Matematyka', 'Fizyka', 'Biologia', 'Chemia', name='teacher_specialty'))
    description = db.Column(db.Text)
    experience = db.Column(db.Integer)
    courses = db.relationship('Course', backref='teacher', cascade='all, delete', passive_deletes=True)

    def to_dict(self):
        return {
            'id': str(self.id),
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'specialty': self.specialty,
            'description': self.description,
            'experience': self.experience
        }

    def set_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


student_course = db.Table('student_course',
                          db.Column('student_id', UUID(as_uuid=True), db.ForeignKey('students.id')),
                          db.Column('course_id', UUID(as_uuid=True), db.ForeignKey('courses.id'))
                          )

class Course(db.Model):
    __tablename__ = 'courses'

    students = db.relationship('Student', secondary=student_course, backref='courses')
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    level = db.Column(db.String(100), nullable=True)
    duration = db.Column(db.Integer)
    price = db.Column(db.Float)
    score = db.Column(db.Float)
    teacher_id = db.Column(UUID(as_uuid=True), db.ForeignKey('teachers.id'))

    def to_dict(self):
        return {
            'id': str(self.id),
            'subject': self.subject,
            'title': self.title,
            'description': self.description,
            'level': self.level,
            'duration': self.duration,
            'price': self.price,
            'score': self.score,
            'teacher_id': str(self.teacher_id)
        }
