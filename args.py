import argparse

def get_args_from_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', required=True,
                        help='path to input image')

    parser.add_argument('-o', '--output', required=False,
                        help='output image name')

    parser.add_argument('-p', '--preview', required=False, default=False,
                        action=argparse.BooleanOptionalAction,
                        help='show preview')

    parser.add_argument('-r', '--reverse', required=False, default=False,
                        action=argparse.BooleanOptionalAction,
                        help='reverse image orientation')

    return vars(parser.parse_args())
