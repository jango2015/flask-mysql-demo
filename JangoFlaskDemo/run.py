import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate =Migrate(app,db)
manager = Manager(app)

def make_dbInfo_context():
    return  dict(app=app,db=db)
manager.add_command('db',MigrateCommand)
manager.add_command('dbinfo',Shell(make_context=make_dbInfo_context))

@manager.command
def test():
    import  unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.command
def wether():
     from app.services.weather import get_weather
     city_weather = get_weather('nanjing')
     print(city_weather)

if __name__ == '__main__':
    # app.run()
    manager.run()
