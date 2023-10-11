def load_glove_embeddings(GLOVE_FILE, word_index, VOCAB_SIZE, EMBEDDING_DIM):
    """
    Load pre-trained GloVe word embeddings and create an embeddings matrix.

    Parameters:
    - GLOVE_FILE (str): Path to the GloVe word vectors file.
    - word_index (dict): Dictionary mapping words to their indices in the vocabulary.
    - VOCAB_SIZE (int): Size of the vocabulary.
    - EMBEDDING_DIM (int): Dimension of the word embeddings.

    Returns:
    - tuple: A tuple containing two elements:
        - GLOVE_EMBEDDINGS (dict): A dictionary containing GloVe word embeddings.
        - EMBEDDINGS_MATRIX: An embeddings matrix containing word embeddings for the vocabulary.
    """
    # Initialize an empty embeddings index dictionary
    GLOVE_EMBEDDINGS = {}

    # Read the GloVe file and fill glove_embeddings with its contents
    with open(GLOVE_FILE) as f:
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            GLOVE_EMBEDDINGS[word] = coefs

    # Initialize an empty numpy array with the appropriate size
    EMBEDDINGS_MATRIX = np.zeros((VOCAB_SIZE + 1, EMBEDDING_DIM))

    # Iterate all words in the vocabulary and save GloVe embeddings in the matrix
    for word, i in word_index.items():
        embedding_vector = GLOVE_EMBEDDINGS.get(word)
        if embedding_vector is not None:
            EMBEDDINGS_MATRIX[i] = embedding_vector

    return GLOVE_EMBEDDINGS, EMBEDDINGS_MATRIX