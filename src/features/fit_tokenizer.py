def fit_tokenizer(train_sentences, val_sentences, train_labels, val_labels, 
                  max_len=16, padding_type='post', truncating_type='post', oov_token='<OOV_TOKEN>'):
    """
    Fit a tokenizer and preprocess text data, including tokenization and padding.

    Parameters:
    - train_sentences (list): List of training sentences.
    - val_sentences (list): List of validation sentences.
    - train_labels (list or np.ndarray): List or numpy array of training labels.
    - val_labels (list or np.ndarray): List or numpy array of validation labels.
    - max_len (int): Maximum sequence length.
    - padding_type (str): Type of padding ('pre' or 'post', default: 'post').
    - truncating_type (str): Type of truncating ('pre' or 'post', default: 'post').
    - oov_token (str): Token to represent out-of-vocabulary words (default: '<OOV_TOKEN>').

    Returns:
    - tuple: A tuple containing the following:
        - np.ndarray: Padded training sequences.
        - np.ndarray: Padded validation sequences.
        - np.ndarray: Numpy array of training labels.
        - np.ndarray: Numpy array of validation labels.
        - dict: Word index dictionary.
        - Tokenizer: Tokenizer object.
    """
    tokenizer = Tokenizer(oov_token=oov_token)
    
    # Generate the word index dictionary
    tokenizer.fit_on_texts(train_sentences)
    word_index = tokenizer.word_index
    
    # Generate and pad the training sequences
    train_sequences = tokenizer.texts_to_sequences(train_sentences)
    train_padded = pad_sequences(train_sequences, maxlen=max_len, padding=padding_type, truncating=truncating_type)
    
    # Generate and pad the validation sequences
    val_sequences = tokenizer.texts_to_sequences(val_sentences)
    val_padded = pad_sequences(val_sequences, maxlen=max_len, padding=padding_type, truncating=truncating_type)
    
    # Convert the labels lists into numpy arrays
    train_labels = np.array(train_labels)
    val_labels = np.array(val_labels)
    
    return train_padded, val_padded, train_labels, val_labels, word_index, tokenizer