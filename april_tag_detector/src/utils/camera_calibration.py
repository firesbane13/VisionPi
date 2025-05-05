def calibrate_camera(camera_matrix, dist_coeffs, image_size):
    # This function calibrates the camera using the provided camera matrix and distortion coefficients.
    # It returns the optimal camera matrix and the region of interest.
    new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, image_size, 1, image_size)
    return new_camera_matrix, roi

def undistort_image(image, camera_matrix, dist_coeffs):
    # This function undistorts an image using the camera matrix and distortion coefficients.
    undistorted_image = cv2.undistort(image, camera_matrix, dist_coeffs)
    return undistorted_image

def load_calibration_data(file_path):
    # This function loads camera calibration data from a file.
    with open(file_path, 'rb') as f:
        calibration_data = pickle.load(f)
    return calibration_data['camera_matrix'], calibration_data['dist_coeffs']