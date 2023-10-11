def text_classification_model(VOCAB_SIZE, EMBEDDING_DIM, MAXLEN, EMBEDDINGS_MATRIX):
    """
    Create a text classification model using Keras.

    Parameters:
    - VOCAB_SIZE (int): Size of the vocabulary.
    - EMBEDDING_DIM (int): Dimension of the word embeddings.
    - MAXLEN (int): Maximum sequence length.
    - EMBEDDINGS_MATRIX (numpy.ndarray): Embeddings matrix for the vocabulary.

    Returns:
    - tf.keras.models.Model: A text classification model.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(VOCAB_SIZE + 1, EMBEDDING_DIM, input_length=MAXLEN, weights=[EMBEDDINGS_MATRIX], trainable=False),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Conv1D(64, 5, activation='relu'),
        tf.keras.layers.MaxPooling1D(pool_size=4),
        tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    return model