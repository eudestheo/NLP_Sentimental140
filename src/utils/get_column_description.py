def get_column_description(df, column_name):
    """
    Get the description of a specific column from the parsed column documentation.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the columns.
    - column_name (str): The name of the column for which you want to retrieve the description.

    Returns:
    - str: The description of the specified column. If no description is available, it returns "No documentation available."
    """
    if column_name in column_documentation:
        return column_documentation[column_name]
    else:
        return "No documentation available."
