import numpy as np
from image_processing import processing

def test_apply_gray_filter():
    dummy_image = np.ones((10, 10, 3), dtype=np.uint8) * 255
    gray_image = processing.apply_gray_filter(dummy_image)
    assert gray_image.shape == (10, 10)
