from main import app
from models.ML_Model import ML_Model
import  os
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3333))
    model = ML_Model()
    app.run(host='0.0.0.0', port=port)
    
