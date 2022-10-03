"""API module
"""

import cv2
import jsonpickle
import numpy as np
from flask import Blueprint, Response, request

from util import apply_filter

api_bp = Blueprint("api", __name__)


@api_bp.route("/apply_filter/", methods=["POST"])
def apply_filter_handler() -> Response:
    b_image: bytes = request.files["image"].read()
    img_type: str = request.files["image"].mimetype
    filter_func: str = request.form["filterFunc"]

    # convert string of image data to uint8
    nparr = np.fromstring(b_image, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    filtered_img = apply_filter(img, filter_func)

    ext = f".{img_type.split('/')[1]}"
    _, img_encoded = cv2.imencode(ext, filtered_img)

    # build a response dict to send back to client
    response = {
        "msg": "success",
        "size": [img.shape[1], img.shape[0]],
        "type": img_type,
        "filtered_img": img_encoded.tostring()
    }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")
