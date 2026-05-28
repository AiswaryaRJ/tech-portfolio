detection_batch = [
    {"object_id": 101, "label": "Crack", "confidence" : 0.94, "location" : [12.5, 45,2]},
    {"object_id": 102, "label": "Pothole", "confidence" : 0.42, "location" : [14.1, 44.8]},
    {"object_id": 103, "label": "Crack", "confidence" : 0.88, "location" : [11.9, 46.0]}
]

for detection in detection_batch:
    if detection["confidence"]>0.75:
        print(f" high confidence: {detection['label']} ({detection['object_id']* 100}%)")
