from flask import Flask, request, jsonify, render_template, send_file
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import cv2
import numpy as np
from io import BytesIO

app = Flask(__name__, template_folder='.')
model = YOLO("yolov8n.pt")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/detect-image", methods=["POST"])
def detect_image():
    try:
        file = request.files.get("file")
        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        image = Image.open(BytesIO(file.read())).convert("RGB")
        image_np = np.array(image)
        results = model(image_np)[0]

        visual = results.plot()
        _, img_encoded = cv2.imencode(".jpg", visual)
        return send_file(BytesIO(img_encoded.tobytes()), mimetype="image/jpeg")

    except UnidentifiedImageError:
        return jsonify({"error": "Invalid image format"}), 400
    except Exception as e:
        print("❌ Detection failed:", e)
        return jsonify({"error": "Detection failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
