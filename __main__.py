from args import get_args_from_parser
from mirror import Mirror
import cv2 as cv

if __name__ == '__main__':
    args = get_args_from_parser()

    input_file_path = args['input']
    mirror = Mirror(input_file_path)

    use_reverse = args['reverse']
    result_image = mirror.process(use_reverse)

    is_preview = args['preview']
    if is_preview:
        mirror.preview(result_image)

    output_filename = args['output']
    mirror.save(output_filename, result_image)

    cv.destroyAllWindows()