import json
from flask import Flask, jsonify, render_template
from routes.analyze.analyze_service import analyze_service
from routes.user.user_service import user_service
from flask_cors import CORS

jinja_options = Flask.jinja_options
jinja_options.update(dict(
    block_start_string="%/",
    block_end_string="\%",
    variable_start_string="[%",
    variable_end_string="%]",
    comment_start_string='%$#',
    comment_end_string='#$%',
))

application = Flask(__name__, template_folder="static", static_folder="static")
CORS(application)

############ REST API PART #######################################
############ REGISTERING THE SERVICES (Using Blueprint) ###################################
application.register_blueprint(analyze_service, url_prefix='/analyze')
application.register_blueprint(user_service, url_prefix='/user')


############ WEB PART #######################################
@application.route('/')
def index():
    return render_template('templates/waste-classifier.html')


@application.route('/about-us')
def about_us():
    return render_template('templates/about-us.html')

############ WEB PART #######################################
