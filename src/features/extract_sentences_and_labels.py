def extract_sentences_and_labels(df):
    """
    Extract sentences and labels from a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing sentences and labels.

    Returns:
    - list: A list of sentences.
    - list: A list of labels.
    """
    sentences = list(df['sentences'])
    labels = list(df['labels'])
    return sentences, labels