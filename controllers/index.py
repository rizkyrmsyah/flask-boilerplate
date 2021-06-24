
import flask

class IndexController(object):

    def index(self):
        return "Flask " + flask.__version__ + " Boilerplate"