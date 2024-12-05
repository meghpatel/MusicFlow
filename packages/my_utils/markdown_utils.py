import pandas as pd

def generate_markdown_table(data, min_index=0):
    # Check if the input is a Series or a DataFrame
    if isinstance(data, pd.Series):
        markdown = "| Value | Count |\n"
        markdown += "|-------|-------|\n"
        for index, value in data.items():
            # Convert index and value to strings, replacing problematic characters for Markdown
            index_str = str(index).replace("|", "\\|")
            value_str = str(value).replace("|", "\\|")
            markdown += f"| {index_str} | {value_str} |\n"
        return markdown

    elif isinstance(data, pd.DataFrame):
        # Helper function to map data types to more readable formats
        def map_data_type(dtype, sample_value):
            # Check for datetime
            if pd.api.types.is_datetime64_any_dtype(dtype) or (
                isinstance(sample_value, str) and pd.to_datetime(sample_value, errors='coerce') is not pd.NaT
            ):
                return "Datetime"
            # Check for Boolean (Python Boolean or string representation)
            elif isinstance(sample_value, bool) or (isinstance(sample_value, str) and sample_value.lower() in ["true", "false"]):
                return "Boolean"
            elif pd.api.types.is_string_dtype(dtype):
                return "String"
            elif pd.api.types.is_numeric_dtype(dtype):
                if pd.api.types.is_integer_dtype(dtype):
                    return "Integer"
                elif pd.api.types.is_float_dtype(dtype):
                    return "Float"
            elif (isinstance(sample_value, list)) or type(sample_value) == pd.Series:
                return "List"
            else:
                return str(dtype)  # Fallback to original dtype if no match

        # Generate the table header for DataFrame
        markdown = "| Column Name | Data Type | Description | Example Value |\n"
        markdown += "|-------------|-----------|-------------|---------------|\n"

        # Iterate over DataFrame columns to generate each row
        for column in data.columns:
            sample_value = data[column].iloc[min_index] if not data[column].empty else "N/A"
            data_type = map_data_type(data[column].dtype, sample_value)
            # Convert example_value to string to avoid formatting issues
            example_value = str(sample_value).replace("\n", " ").replace("|", "\\|")
            # Create a new row for each column
            markdown += f"| `{column}` | {data_type} |  | {example_value} |\n"

        return markdown

    else:
        raise TypeError("Input must be a pandas DataFrame or Series")

def generate_file_markdown_intro(file_name, title, df):
    mdown_text = f"""
    # {title} Data Definition

    This data dictionary describes the fields in the {file_name} data. There are {df.shape[0]} rows and {df.shape[1]} columns. 

    ## {title} Data

    """
    return mdown_text

def write_markdown_file(mdown_text, file_path):
    with open(file_path, 'w') as f:
        f.write(mdown_text)
    print(f"Markdown file saved to {file_path}")