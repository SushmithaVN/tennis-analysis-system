from ultralytics import YOLO

model = YOLO('yolov8x')  # load a pretrained YOLOv8x model

result = model.track('input_videos/input_video.mp4', conf=0.2, save=True)  # predict on an input video and show/save the results
# print(result)  # print the result object to see details about the predictions
# print("Boxes:")
# for box in result[0].boxes:
#     print(box)  # print each bounding box object
