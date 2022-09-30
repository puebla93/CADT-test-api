"""CADT test API.
See https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24
See https://gist.github.com/kylehounslow/767fb72fde2ebdd010a0bf4242371594
"""

from flask import Flask

app = Flask("CADT test API")

@app.route("/", methods=["GET"])
def root() -> str:
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
