from flask import Flask
#import tensorflow as tf
app = Flask(__name__)

import subprocess
import sys



@app.route('/')

def index():
    #print("load started")
    #new_model = tf.keras.models.load_model('saved_model.h5')

    # try:
    #     import tensorflow as tf 
    # except ImportError:
    #     subprocess.check_call([sys.executable, "-m", "pip", "install", 'tensorflow'])
    # finally:
    #     import tensorflow as tf
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'scipy'])

    import scipy as tf
        

    v = tf.__version__ 

    return f'Hello WOrld  dee {v} '


if __name__ == '__main__':
    app.run(debug =  True)