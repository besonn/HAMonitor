from faker import Faker
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from com.application import create_app
from com.model import *

app = create_app(__name__)

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

fk = Faker(locale='zh_CN')


def add_fake():
    for i in range(0, 10):
        p = Person(name=fk.name(), phone=fk.phone_number(), email=fk.email())
        db.session.add(p)

    db.session.commit()
    print('添加了10个联系人')


@manager.shell
def myshell():
    return dict(
        app=app,
        db=db,
        Person=Person,
        fk=fk,
        add_fake=add_fake
    )


if __name__ == '__main__':
    manager.run()
