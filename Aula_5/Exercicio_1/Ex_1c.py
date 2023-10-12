#!/usr/bin/env python3
# Shebang line

import cv2

def main():

    image_filename = '/home/ricardo/Documentos/PSR_2023-2024/my_student_psr_23-24/Aula_5/Exercicio_1/atlascar2_multichannel_thresholded.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()
