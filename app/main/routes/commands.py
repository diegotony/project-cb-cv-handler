from flask import Flask
from flask import jsonify
from flask import request
from commands import commands
app = Flask(__name__)


@app.route('/command', methods=['POST'])
def handler_command():
    try:
        if request.form:
            data = request.form
            print(data)
            data = commands(data['command'])
            return data
        else:
            return "no hay datos"
    except Exception as e:
        print("tmal")
        return "tmalx"



if __name__ == '__main__':
    app.run(debug=True)
