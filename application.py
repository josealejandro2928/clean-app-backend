from main import application
from models.load_models import load_models
import os

print("\n***************LOADING MODELS******************\n")
load_models()
print("\n***************MODELS LOADED******************\n")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', default=3333))
    application.run(host='0.0.0.0', port=port)
