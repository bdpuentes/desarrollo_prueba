from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from datetime import datetime
from controller.price_controller import app

if __name__ == '__main__':
    app.run(debug=True , port=1010)
