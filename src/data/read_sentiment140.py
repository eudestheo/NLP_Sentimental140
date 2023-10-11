def read_sentiment140_csv(file_path):
    """
    Read the Sentiment140 dataset from a CSV file and preprocess it.

    Parameters:
    - file_path (str): The path to the CSV file containing the dataset.

    Returns:
    - pd.DataFrame: A DataFrame containing the Sentiment140 dataset with labels modified.
    """
    df = pd.read_csv(file_path, delimiter=",", header=None, encoding='latin-1')

    # Create a DataFrame with modified labels
    df = df[[0, 5]].rename(columns={0: 'labels', 5: 'sentences'})
    df['labels'] = np.where(df['labels'] == 4, 1, df['labels'])

    return df