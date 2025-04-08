
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['DELETE'])
def delete_route():
    return "DELETE method accepted"

if __name__ == "__main__":
    app.run()
