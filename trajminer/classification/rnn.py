from .base import Classifier


class RNNClassifier(Classifier):
    """Recurrent Neural Network Classifier.

    Neural network tailored for classifying trajectory data.

    Parameters
    ----------
    input_shape : tuple
        Input shape as a tuple (max_length, n_features).
        **max_length** is the length of the longest trajectory and
        **n_features** is the number of attributes.
    hidden_units : int
        Number of hidden units.
    output_size : int
        Number of output units, i.e., the number of classes.
    cell : string (default='LSTM')
        RNN cell type used. It can be either **LSTM** for
        Long short-term memory or **GRU** for Gated recurrent unit.
    dropout : float (default=0.5)
        Dropout rate of the network. If `None`, no dropout layer is added
        to the model.
    batch_size : int (default=32)
        Number of samples per gradient update.
    lrate : float (default=0.001)
        Learning rate of the network.
    epochs : int (default=1)
        Number of epochs to train the network.
    """

    def __init__(self, input_shape, hidden_units, output_size, cell='LSTM',
                 dropout=0.5, batch_size=32, lrate=0.001, epochs=1):
        from keras.models import Sequential
        from keras.layers import Dense, LSTM, GRU, Dropout
        from keras.initializers import he_uniform
        from keras.regularizers import l1
        from keras.optimizers import Adam

        self._batch_size = batch_size
        self._epochs = epochs
        self._classifier = Sequential()

        if cell == 'LSTM':
            self._classifier.add(LSTM(units=hidden_units,
                                 input_shape=input_shape,
                                 recurrent_regularizer=l1(0.02)))
        else:
            self._classifier.add(GRU(units=hidden_units,
                                 input_shape=input_shape,
                                 recurrent_regularizer=l1(0.02)))

        if dropout:
            self._classifier.add(Dropout(dropout))

        self._classifier.add(Dense(units=output_size,
                             kernel_initializer=he_uniform(seed=1),
                             activation='softmax'))

        opt = Adam(lr=lrate)
        self._classifier.compile(optimizer=opt,
                                 loss='categorical_crossentropy',
                                 metrics=['acc'])

    def fit(self, X, y, epochs=None, validation_data=None, callbacks=None):
        """Train the network for a number of epochs.

        Parameters
        ----------
        X : array-like, shape (n_samples, max_length, n_features)
            Input data for training.
        y : array-like, shape (n_samples, n_labels)
            Labels of training samples.
        epochs : int (default=None)
            Number of epochs to train the network. If `None`, the network will
            be trained for the number of epochs specified in the object's
            initialization.
        validation_data : tuple (default=None)
            Tuple (val_X, val_y) of validation data. **val_X** is an
            array-like object of shape (n_samples, max_length, n_features)
            and **val_y** is an array-like object of shape (n_samples,
            n_labels) with the corresponding labels.
        callbacks : array-like
            List of `keras.callbacks.Callback` instances.
        """
        self._classifier.fit(x=X, y=y,
                             batch_size=self._batch_size,
                             epochs=epochs if epochs else self._epochs,
                             verbose=1,
                             validation_data=validation_data,
                             callbacks=callbacks)

    def predict(self, X):
        return self._classifier.predict(x=X,
                                        batch_size=self._batch_size,
                                        verbose=1)

    def score(self, X, y):
        _, acc = self._classifier.evaluate(x=X, y=y,
                                           batch_size=self._batch_size,
                                           verbose=1)
        return acc
