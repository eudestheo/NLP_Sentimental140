def split_data_randomly(sentences, labels, sample_size=0.1, training_size=0.9, random_seed=42):
    """
    Randomly split data into training and testing sets after taking 10% as a random sample.

    Parameters:
    - sentences (list): List of sentences.
    - labels (list): List of labels corresponding to the sentences.
    - sample_size (float, optional): Fraction of data to be used for sampling (default: 0.1).
    - training_size (float): Fraction of data to be used for training (default: 0.9).
    - random_seed (int): Random seed for reproducibility (default: 42).

    Returns:
    - tuple: A tuple containing the following:
        - train_sentences: Training sentences.
        - val_sentences: Testing sentences.
        - train_labels: Training labels.
        - val_labels: Testing labels.
    """
    random.seed(random_seed)
    
    # Randomly select 10% of data as a random sample
    num_samples = int(len(sentences) * sample_size)
    sentences_labels_zip = list(zip(sentences, labels))
    sentences_labels_zip = random.sample(sentences_labels_zip, num_samples)
    sentences, labels = zip(*sentences_labels_zip)

    
    # Split the remaining data into training and testing sets
    training_size = int(len(sentences)*0.9)
    
    train_sentences = sentences[:training_size]
    val_sentences = sentences[training_size:]
    
    train_labels = labels[:training_size]
    val_labels = labels[training_size:]

    return train_sentences, val_sentences, train_labels, val_labels