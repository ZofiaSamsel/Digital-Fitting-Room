from utils.app import FashionPose
import cv2
import numpy as np


class FashionPoseImage(FashionPose):

    def __init__(self, image, outfit='Def'):
        super().__init__()
        self.image = image
        self.outfit = outfit
        self.outfit_type = outfit


    def estimate_pose(self, image):
        self.img_height, self.img_width, _ = 480, 600,3
        # Extract background
        input_image = cv2.imread(image)

        input_image.flags.writeable = False
        pose_landmarks = self.pose_estimation.process(input_image).pose_landmarks

        self.detected = pose_landmarks.landmark
        if not self.detected:
            return
        self.skeleton_keypoints = np.array([[int(min([landmark.x * self.img_width, self.img_width - 1])),
                                             int(min([landmark.y * self.img_height, self.img_height - 1]))]
                                            for landmark in pose_landmarks.landmark], dtype=np.float32)