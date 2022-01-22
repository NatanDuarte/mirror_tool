from args import get_args_from_parser
from mirror import Mirror
import cv2 as cv

if __name__ == '__main__':
    args = get_args_from_parser()

    mirror = Mirror(args['input'])
    result_image = mirror.process(args['reverse'])

    if args['preview']:
        mirror.preview(result_image)

    mirror.save(args['output'], result_image)

    cv.destroyAllWindows()