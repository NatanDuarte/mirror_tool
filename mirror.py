import numpy as np
import cv2 as cv
import os

class Mirror:
    def __init__(self, image_path:str) -> None:
        self._image = cv.imread(image_path)
        self._copy = self._image.copy()
        if not os.path.exists('output'): os.mkdir('output')

    def process(self, is_reverse:bool):
        rotated = self.rotate(angle=180)
        mirrored = cv.flip(rotated, 1)

        concatenate_order = (mirrored, self._image) if not is_reverse \
            else (self._image, mirrored)

        result_image = np.concatenate(concatenate_order)
        return result_image

    def preview(self, image):
        image_view = image.copy()
        preview_aspect = (350, 350)
        image_view = cv.resize(image_view, preview_aspect,
                                interpolation=cv.INTER_LINEAR)
        cv.imshow('preview', image_view)
        cv.waitKey(0)

    def rotate(self, angle, rotPoint=None):
        (height, width) = self._copy.shape[:2]

        if rotPoint is None:
            rotPoint = (width//2, height//2)

        rotation_matrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(self._copy, rotation_matrix, dimensions)

    def save(self, output_path, result):
        cv.imwrite(output_path, result)
        print(f'file saved at: {os.path.abspath(output_path)}')
