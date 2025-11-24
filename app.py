from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from chicken_disease.utils.common import decodeImage
from src.chicken_disease.pipeline.predict import PredictPipeline

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictPipeline(self.filename)

clApp = ClientApp()   # <-- Global object created here

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training Completed!"

@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json["image"]

    # Use the global clApp instance
    decodeImage(image, fileName=clApp.filename)

    prediction = clApp.classifier.predict()
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

    
