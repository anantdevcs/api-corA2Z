from flask import Flask
import tensorflow as tf
app = Flask(__name__)

@app.route('/')

def index():
    print("load started")
    new_model = tf.keras.models.load_model('saved_model.h5')

    return f'Hello WOrld {new_model.summary()}  dee '


if __name__ == '__main__':
    app.run(debug =  True)