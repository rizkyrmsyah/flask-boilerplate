from flask import Blueprint
from flask import jsonify
from config import configuration
import json

from controllers import IndexController

blueprint = Blueprint("index", __name__)
indexController = IndexController()

class Index:
    @blueprint.route("/", methods = ["GET"])
    def index():
        res = indexController.index()
        return jsonify(res)