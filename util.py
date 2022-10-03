"""Util module
"""

import numpy as np
import cv2


def emboss_filter(img: np.ndarray) -> np.ndarray:
    emboss_kernel = np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    emboss_img = cv2.filter2D(src=img, kernel=emboss_kernel, ddepth=-1)
    return emboss_img


def gaussian_blur_filter(img: np.ndarray) -> np.ndarray:
    gaussian_blur_img = cv2.GaussianBlur(img, (35, 35), 0)
    return gaussian_blur_img


def canny_edge_filter(img: np.ndarray) -> np.ndarray:
    canny_edge_img = cv2.Canny(img,100,200)
    return canny_edge_img


def gray_scale_filter(img: np.ndarray) -> np.ndarray:
    gray_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_scale_img


def apply_filter(img: np.ndarray, filter_func: str = "emboss") -> np.ndarray:
    if filter_func == "emboss":
        return emboss_filter(img)
    if filter_func == "gaussianBlur":
        return gaussian_blur_filter(img)
    if filter_func == "cannyEdge":
        return canny_edge_filter(img)
    if filter_func == "grayScale":
        return gray_scale_filter(img)
    raise ValueError("Invalid fiter function")
