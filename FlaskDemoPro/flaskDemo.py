from flask import Flask
from flask import render_template
from service.Service import DbService
app = Flask(__name__)


@app.route('/')
def hello_world():
    # DbService.insert()
    models = DbService.getall()
    print(models)
    return render_template("index.html", lists =  models)
    # return 'Hello World!'


if __name__ == '__main__':
    app.run()
