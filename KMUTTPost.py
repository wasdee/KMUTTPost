from flask import Flask, jsonify
from check import isThereMyMailAtKMUTTOffice
app = Flask(__name__)

numericDict = {
    "postfix": "New Mail @KMUTT POST?",
    "data": {
        "value": "yes"
    }
}

@app.route('/')
def hello_world():
    a = numericDict.copy()
    try:
        if isThereMyMailAtKMUTTOffice():
            a["data"]["value"] = "Go and Grab it!"
        else:
            a["data"]["value"] = "Nothing There"
    except:
        a["data"]["value"] = "selenium connect fail"
    finally:
        return jsonify(**a)

def test():
    print("KMUTT POST")

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=80)
    # app.run()

