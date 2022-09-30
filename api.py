"""API module
"""

import cv2
import jsonpickle
import numpy as np
from flask import Blueprint, Response, request


api_bp = Blueprint("api", __name__)


def apply_filter(img: np.array) -> np.array:
    return img


@api_bp.route("/apply_filter/", methods=["POST"])
def apply_filter_handler() -> Response:
    current_request = request
    # convert string of image data to uint8
    nparr = np.fromstring(current_request.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    filtered_img = apply_filter(img)
    _, img_encoded = cv2.imencode('.png', filtered_img)

    # build a response dict to send back to client
    response = {
        "message": f"image received. size={img.shape[1]}x{img.shape[0]}",
        "filtered_img": img_encoded.tostring()
    }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
