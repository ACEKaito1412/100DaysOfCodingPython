import cv2 as cv
import numpy as np
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import uuid, os

UPLOAD_FOLDER = "static/temp"
TEST_PATH = "static/test_.png"

def save_document(file) -> list[str, str]:
    try:
        filename = f"{uuid.uuid4()}_{secure_filename(file.filename)}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        return file_path, ""
    except Exception as e:
        return "", str(e)

def get_colors(img, size: int):
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    resize_img = cv.resize(img_rgb, (500, 500))

    pixels = resize_img.reshape(-1, 3)
    pixels = np.float32(pixels)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, _, centers = cv.kmeans(pixels, size, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    dominant_colors = [tuple(color) for color in centers.astype(np.uint8)]

    return dominant_colors

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():

    if request.method == "POST":
        file = request.files['file']

        path, error = save_document(file=file)

        img = cv.imread(path)

        colors = get_colors(img, 6)

        img_2 = cv.imread(TEST_PATH)
        src_col = get_colors(img_2, 6)

        return render_template('index.html', colors=colors, img_path = path, src_n = TEST_PATH, src_col = src_col)
    
    img = cv.imread(TEST_PATH)
    src_col = get_colors(img, 6)

    return render_template('index.html', colors=[], src_n = TEST_PATH, src_col = src_col)


if __name__ == "__main__":
    app.run(debug=True)