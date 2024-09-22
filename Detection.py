from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\Desktop\Detection\yolov8s.pt")
results = model.predict(source=r"C:\Users\Downloads\istockphoto-491574872-612x612.jpg", save=True, project="runs/detect", name="inference", exist_ok=True) # source already setup
names = model.names

# Initialize a dictionary to store counts of each class
class_counts = {}

for r in results:
    for c in r.boxes.cls:
        class_name = names[int(c)]
        # Increment count for each class
        class_counts[class_name] = class_counts.get(class_name, 0) + 1

# Print the counts of each class
for class_name, count in class_counts.items():
    print(f"{class_name}s = {count}")
