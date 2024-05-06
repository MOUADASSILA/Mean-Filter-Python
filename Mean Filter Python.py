#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:10:17 2024

@author: mac
"""

from PIL import Image

def apply_mean_filter(image, kernel_size):
    img = image.convert("RGB")
    pixels = img.load()

    width, height = img.size

    output_image = Image.new("RGB", (width, height))
    output_pixels = output_image.load()
    k_half = kernel_size // 2

    for i in range(k_half, width - k_half):
        for j in range(k_half, height - k_half):
            sum_r = sum_g = sum_b = 0
            for ki in range(-k_half, k_half + 1):
                for kj in range(-k_half, k_half + 1):
                    r, g, b = pixels[i - ki, j + kj]
                    sum_r += r
                    sum_g += g
                    sum_b += b
            num_pixels = kernel_size * kernel_size
            output_pixels[i, j] = (sum_r // num_pixels, sum_g // num_pixels, sum_b // num_pixels)

    return output_image

# Correct placement of the main execution code
if __name__ == "__main__":
    image_path = "/Users/mac/Downloads/original.png"
    original_image = Image.open(image_path)
    kernel_size = 6
    filtered_image = apply_mean_filter(original_image, kernel_size)
    filtered_image.show()