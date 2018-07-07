from keras.models import Sequential
from keras.layers import Dense, Activation


def make():
    model = Sequential([
        Dense(32, input_shape=(513, 2, 2)),
        Activation('relu')
        Dense(10),
        Activation('softmax'),
    ])
    model.compile(optimizer='rmsprop', loss='mse')
    return model


def load(path):
    pass


def save(path):
    pass


def train(network, audio):
    pass
