#!/usr/bin/env python3
# Shebang line

import cv2
import argparse

def main():

    parser = argparse.ArgumentParser(description='Scrip used to test imagem')
    parser.add_argument('-if', '--image_filename', type = str, help ='Olá', required=True)
    args = vars(parser.parse_args())
    print(vars)
    exit(0)

    #image_filename = '/atlascar2_multichannel_thresholded.png'
    #image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    #cv2.imshow('window', image)  # Display the image
    #cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()
