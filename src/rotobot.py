import os
import threading

# import requests

from flask import Flask
from flask_cors import CORS

import constants
import web_utils
import log
import motor_control

app = Flask(__name__)
CORS(app, supports_credentials=True)

dir_path = os.path.dirname(os.path.realpath(__file__))


@app.route("/rotate_360")
def capture():
    """Rotates the turntable 360 degrees"""
    log.info("rotate_360: request received")

    threading.Thread(target=motor_control.rotate_360).start()
    return web_utils.respond_ok(app)


class webapp:
    def __init__(self):
        pass

    def thread(self):
        app.run(host="0.0.0.0", port=constants.SERVER_PORT, threaded=True)

    def start_thread(self):
        thread = threading.Thread(target=self.thread)
        thread.setDaemon(False)
        thread.start()  #


log.info("rotobot server starting...")

flask_app = webapp()
flask_app.start_thread()
