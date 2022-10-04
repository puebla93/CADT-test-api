import pytest
import random

from util import *


def test_emboss_filter(mocker):
    mocker_numpy_array = mocker.patch("numpy.array")
    numpy_array_returned_value = "fake numpy.array returned value"
    mocker_numpy_array.return_value = numpy_array_returned_value

    mocker_cv2_filter2D = mocker.patch("cv2.filter2D")
    cv2_filter2D_returned_value = "fake cv2.filter2D returned value"
    mocker_cv2_filter2D.return_value = cv2_filter2D_returned_value

    result = emboss_filter(img=[])

    assert result == cv2_filter2D_returned_value
    mocker_numpy_array.assert_called_once_with([[0,-1,-1],[1,0,-1],[1,1,0]])
    mocker_cv2_filter2D.assert_called_once_with(src=[], kernel=numpy_array_returned_value, ddepth=-1)


def test_gaussian_blur_filter(mocker):
    mocker_cv2_GaussianBlur = mocker.patch("cv2.GaussianBlur")
    cv2_GaussianBlur_returned_value = "fake cv2.GaussianBlur returned value"
    mocker_cv2_GaussianBlur.return_value = cv2_GaussianBlur_returned_value

    result = gaussian_blur_filter(img=[])

    assert result == cv2_GaussianBlur_returned_value
    mocker_cv2_GaussianBlur.assert_called_once_with([], (35, 35), 0)


def test_canny_edge_filter(mocker):
    mocker_cv2_Canny = mocker.patch("cv2.Canny")
    cv2_Canny_returned_value = "fake cv2.Canny returned value"
    mocker_cv2_Canny.return_value = cv2_Canny_returned_value

    result = canny_edge_filter(img=[])

    assert result == cv2_Canny_returned_value
    mocker_cv2_Canny.assert_called_once_with([], 100, 200)


def test_gray_scale_filter(mocker):
    from cv2 import COLOR_BGR2GRAY

    mocker_cv2_cvtColor = mocker.patch("cv2.cvtColor")
    cv2_cvtColor_returned_value = "fake cv2.cvtColor returned value"
    mocker_cv2_cvtColor.return_value = cv2_cvtColor_returned_value

    result = gray_scale_filter(img=[])

    assert result == cv2_cvtColor_returned_value
    mocker_cv2_cvtColor.assert_called_once_with([], COLOR_BGR2GRAY)


def test_sepia_filter(mocker):
    mocker_numpy_array = mocker.patch("numpy.array")
    numpy_array_returned_value = "fake numpy.array returned value"
    mocker_numpy_array.return_value = numpy_array_returned_value

    mocker_cv2_filter2D = mocker.patch("cv2.filter2D")
    cv2_filter2D_returned_value = "fake cv2.filter2D returned value"
    mocker_cv2_filter2D.return_value = cv2_filter2D_returned_value

    result = sepia_filter(img=[])

    assert result == cv2_filter2D_returned_value
    mocker_numpy_array.assert_called_once_with([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
    mocker_cv2_filter2D.assert_called_once_with(src=[], kernel=numpy_array_returned_value, ddepth=-1)


def test_apply_filter_invalid_filter_func():
    with pytest.raises(ValueError) as cm:
        apply_filter(img=[], filter_func="")

    assert "Invalid fiter function" == str(cm.value)


def test_apply_filter(mocker):
    filter_func_names = {
        "emboss": "emboss_filter",
        "gaussianBlur": "gaussian_blur_filter",
        "cannyEdge": "canny_edge_filter",
        "grayScale": "gray_scale_filter",
        "sepia": "sepia_filter"
    }
    filter_func = random.choice(list(filter_func_names.keys()))

    mocker_requests_get = mocker.patch(f"util.{filter_func_names[filter_func]}")
    returned_value = "fake returned value"
    mocker_requests_get.return_value = returned_value

    result = apply_filter(img=[], filter_func=filter_func)

    assert result == returned_value
    mocker_requests_get.assert_called_once_with([])
