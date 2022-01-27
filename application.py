from main import application
from models.ML_Model import ML_Model
import os

model = ML_Model()
if __name__ == '__main__':
    port = int(os.environ.get('PORT', default=3333))
    application.run(host='0.0.0.0', port=port)
