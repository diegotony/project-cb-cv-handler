import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import blueprint
from app.main import create_app, db
from app.main.models import user
from app.main.models import interaction

app = create_app(os.getenv('BOILERPLATE_ENV') or 'prod')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


if __name__ == '__main__':
    manager.run()
    app.run()
