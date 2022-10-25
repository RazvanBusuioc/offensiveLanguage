from model import Model
from flask import Flask, request, Response
from flask.json import jsonify
from flask_cors import CORS

modelFBRO = Model("./BERT-CNN-FBRO_0.844_50.h5", 50)
modelTRANS = Model("./BERT-CNN-TRANSF_0.819_120.h5", 120)

predictions = {}
app = Flask(__name__)
CORS(app)

@app.route('/api/fbro/text',methods=['POST'])
def predfbro():
    data = request.get_json(force=True)
    prediction = modelFBRO.predict([str(data['text'])])
    output = prediction[0]
    return jsonify(output)

@app.route('/api/transf/text',methods=['POST'])
def predtransf():
    data = request.get_json(force=True)
    prediction = modelTRANS.predict([str(data['text'])])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    print("RUNNING APP")
    app.run("0.0.0.0", port = 7020, debug=True)
