from gino import Gino

db = Gino()

class Document(db.Model):
    __tablename__='documents'

    id = db.Column('id', db.Integer, primary_key=True)
    rubrics = db.Column('rubrics', db.String)
    text = db.Column('text', db.String)
    created_date = db.Column('created_date', db.DateTime)



