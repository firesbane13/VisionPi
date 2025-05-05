class ColorIdentifier:
    def __init__(self):
        pass

    def identify_color(self, image, contours):
        colors = []
        for contour in contours:
            mask = self.create_mask(image, contour)
            mean_color = cv2.mean(image, mask=mask)[:3]
            color_name = self.get_color_name(mean_color)
            colors.append(color_name)
        return colors

    def create_mask(self, image, contour):
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        cv2.drawContours(mask, [contour], -1, 255, -1)
        return mask

    def get_color_name(self, mean_color):
        b, g, r = mean_color
        if r > g and r > b:
            return "Red"
        elif g > r and g > b:
            return "Green"
        elif b > r and b > g:
            return "Blue"
        else:
            return "Unknown"