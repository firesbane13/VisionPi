import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        # Paths to YOLOv4 files in the src/cfg directory
        model_path = "src/cfg/yolov4.weights"
        config_path = "src/cfg/yolov4.cfg"
        class_names_path = "src/cfg/coco.names"

        # Load the pre-trained YOLOv4 model
        self.net = cv2.dnn.readNetFromDarknet(config_path, model_path)
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        # Load class names
        with open(class_names_path, 'r') as f:
            self.class_names = f.read().strip().split('\n')

    def detect_objects(self, frame):
        # Prepare the frame for object detection
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)

        # Get output layer names
        layer_names = self.net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        # Perform forward pass
        detections = self.net.forward(output_layers)

        # Parse detections
        height, width = frame.shape[:2]
        objects = []
        for output in detections:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:  # Confidence threshold
                    box = detection[0:4] * np.array([width, height, width, height])
                    (center_x, center_y, box_width, box_height) = box.astype("int")

                    x = int(center_x - (box_width / 2))
                    y = int(center_y - (box_height / 2))

                    objects.append({
                        "class_id": class_id,
                        "class_name": self.class_names[class_id],
                        "confidence": float(confidence),
                        "box": (x, y, int(box_width), int(box_height)),
                        "center": (center_x, center_y)
                    })

        return objects