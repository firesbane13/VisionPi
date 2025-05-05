import cv2
from detection.apriltag_detector import AprilTagDetector
from detection.object_detector import ObjectDetector
from detection.color_identifier import ColorIdentifier
from utils.camera_calibration import calibrate_camera

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    # Calibrate camera
    camera_matrix, dist_coeffs = calibrate_camera()

    # Initialize detectors
    apriltag_detector = AprilTagDetector(camera_matrix, dist_coeffs)
    object_detector = ObjectDetector(camera_matrix, dist_coeffs)
    color_identifier = ColorIdentifier()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect AprilTags
        apriltags = apriltag_detector.detect_tags(frame)
        for tag in apriltags:
            angles, distance = apriltag_detector.calculate_pose(tag)
            print(f"AprilTag ID: {tag['id']}, Angles: {angles}, Distance: {distance}")

        # Detect other objects
        objects = object_detector.detect_objects(frame)
        for obj in objects:
            angles, distance = object_detector.get_object_info(obj)
            color = color_identifier.identify_color(frame, obj)
            print(f"Object: {obj['type']}, Angles: {angles}, Distance: {distance}, Color: {color}")

        # Display the frame
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()