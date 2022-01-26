import json
from flask import Flask, jsonify, render_template
from routes.image.image_service import image_service
from routes.user.user_service import user_service
from flask_cors import CORS

jinja_options = Flask.jinja_options
jinja_options.update(dict(
    block_start_string='$$',
    block_end_string='$$',
    variable_start_string='$',
    variable_end_string='$',
    comment_start_string='$#',
    comment_end_string='#$',
))

app = Flask(__name__, template_folder="static", static_folder="static")
CORS(app)

############ REGISTERING THE SERVICES (Using Blueprint) ###################################
app.register_blueprint(image_service, url_prefix='/image')
app.register_blueprint(user_service, url_prefix='/user')


@app.route('/')
def index():
    return render_template('templates/index.html')
