import numpy as np
import cv2 as cv
import os

class Mirror:
    def __init__(self, image_path:str) -> None:
        self._image = cv.imread(image_path)
        self._copy = self._image.copy()

    def process(self, is_reverse:bool):
        '''# process: 
        creates a mirrored image by creating a copy of the original, them rotating
        by 180 degrees and flipping it. It finalizes returning the concatenation of
        both images

        # Args:

        is_reverse: the default order is mirrored image and then the original one.
        set this variable to True if you want to invert the sequence.'''
        rotated = self.rotate(angle=180)
        mirrored = cv.flip(rotated, 1)

        concatenate_order = (mirrored, self._image) if not is_reverse \
            else (self._image, mirrored)

        result_image = np.concatenate(concatenate_order)
        return result_image

    def preview(self, image, preview_aspect=(250, 250)):
        '''# preview:

        Displays a preview window of a given image.

        ## Args

        * image: the image to preview
        * preview_aspect: preview aspect ration'''
        preview = image.copy()
        preview = cv.resize(preview, preview_aspect,
                                interpolation=cv.INTER_LINEAR)
        cv.imshow('preview', preview)
        cv.waitKey(0)

    def rotate(self, angle:int, rotPoint=None):
        '''# rotate

        rotate a image in a given angle through a given point

        ## Args

        * angle: angle to rotate the image.

        * rotPoint: point rotate the image.'''
        (height, width) = self._copy.shape[:2]

        if rotPoint is None:
            rotPoint = (width//2, height//2)

        rotation_matrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
        dimensions = (width, height)
        return cv.warpAffine(self._copy, rotation_matrix, dimensions)

    def save(self, output_name, result):
        out_dir = 'output'
        if not os.path.exists(out_dir): os.mkdir(out_dir)
        cv.imwrite(os.path.join(out_dir, output_name), result)
        print(f'file saved at: {os.path.join(os.getcwd(), out_dir, output_name)}')
