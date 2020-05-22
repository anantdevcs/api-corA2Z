from flask import Flask
#import tensorflow as tf
app = Flask(__name__)

import subprocess
import sys



@app.route('/')

def index():
    #print("load started")
    #new_model = tf.keras.models.load_model('saved_model.h5')

    try:
        import pandas as pd
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
    finally:
        import pandas as pd

        

    v = pd.__version__

    return f'Hello WOrld  dee {v} '


if __name__ == '__main__':
    app.run(debug =  True)