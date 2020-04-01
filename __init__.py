from morphology_methods import *
import argparse


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-path", "--path_image", type=str,
                    default='image.png',
                    help="The path of the input image")
    ap.add_argument("-M_type", "--Morphology_method", type=str,
                    default='d',
                    help="[d = Dilation, e = Erosion, o = opening, c = closing, g = Morphological Gradient"
                         "t = Top Hat, b = Black Hat]")
    ap.add_argument("-K_type", "--Kernel_type", type=str,
                    default='r',
                    help="[r = RECT, e = ELLIPSE, c = CROSS]")
    ap.add_argument("-K_size", "--kernel_size", type=int,
                    default=3,
                    help="the size of the kernel")
    args = vars(ap.parse_args())

    img = cv2.imread(args["path_image"], 0)
    cv2.imshow('input', img)
    cv2.waitKey(0)

    kernel = chose_kernel(args["Kernel_type"], args["kernel_size"])
    out = chose_morphology_method(img, kernel, args["Morphology_method"])
    cv2.imshow('output', out)
    cv2.waitKey(0)

