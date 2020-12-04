from flask import Flask, request     # please put three lines in order
import sys                                  # 1. line
sys.path.insert(1, '/app')                  # 2. line
from prediction import predict              # 3. line

app = Flask(__name__)


@app.route('/')
def root():
    return "alive"


@app.route('/predict', methods=['GET', 'POST'])
def predict_route():
    if request.method == 'POST':
        print("this is POST")
    else:
        return """Welcome house price prediction API by Christophe GIETS, Naomi THIRU, Orhan NURKAN and Sara SILVENTE
                check /instructions link for how to use this API"""


if __name__ == '__main__':
    app.run(debug=True)
