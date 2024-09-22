from flask import Flask, render_template, request
from ultralytics import YOLO

app = Flask(__name__)

model = YOLO(r"C:\Users\Detection\yolov8s.pt")
names = model.names

def detect_objects(image_path):
    results = model.predict(source=image_path)
    class_counts = {}
    for r in results:
        for c in r.boxes.cls:
            class_name = names[int(c)]
            class_counts[class_name] = class_counts.get(class_name, 0) + 1
    return class_counts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', error="No file part")
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error="No selected file")
    if file:
        image_path = "uploaded_image.jpg"
        file.save(image_path)
        class_counts = detect_objects(image_path)
        return render_template('index.html', counts=class_counts)

if __name__ == '__main__':
    app.run(debug=True)
