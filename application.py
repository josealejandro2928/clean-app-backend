from main import application
from models.ML_Model import ML_Model
import os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', default=3333))
    model = ML_Model()
    # from waitress import serve
    # import logging
    # logger = logging.getLogger('waitress')
    # logger.setLevel(logging.INFO)
    # serve(app, host="0.0.0.0", port=port)
    application.run(host='0.0.0.0', port=port)