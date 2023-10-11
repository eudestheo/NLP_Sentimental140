def parse_column_documentation(file_path):
    """
    Parse column documentation from a text file and store it in a dictionary.

    Parameters:
    - file_path (str): The file path to the text file containing column documentation.

    Returns:
    - dict: A dictionary where keys are column names and values are their respective descriptions.
    """
    column_docs = {}
    with open(file_path, 'r') as doc_file:
        for line in doc_file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                column_name = parts[0].strip()
                column_description = parts[1].strip()
                column_docs[column_name] = column_description
    return column_docs
