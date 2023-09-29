from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Statements(db.Model):
    __tablename__ = 'STATEMENTS'
    sqlite_autoincrement = True
    id = db.Column('ID', db.Integer, primary_key=True)
    statement = db.Column('STATEMENT', db.Text)
    description = db.Column('DESCRIPTION', db.Text)
    # email = db.Column('email', db.Text)

    def to_dict(self):
        return dict(
            id=self.id,
            statement=self.statement,
            #phone=self.phone,
            description=self.description
        )
    
