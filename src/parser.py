import os
import pandas as pd
from llama_index.core.schema import TextNode


class Reader:

    def __init__(self):
        pass

    def _get_data(self, folder_path:str, sheet_name_is_influencial:bool):
        nodes = []
        files = os.listdir(folder_path)
        # Loop through each file in the folder
        for file_name in files:
            if file_name.endswith('.xlsx'):  # Check if the file is an Excel file
                file_path = os.path.join(folder_path, file_name)                
                # Read all sheets from the Excel file
                excel_data = pd.read_excel(file_path, sheet_name=None)
                
                # Loop through each sheet in the Excel file
                for sheet_name, df in excel_data.items():
                    for column in df.columns:
                        if sheet_name_is_influencial:
                            node = TextNode(
                                    text=column +" " +sheet_name
                                )
                        else:
                            node = TextNode(
                                    text=column
                                )
                        node.metadata = {'filepath':file_path,
                                'sheetname': sheet_name}
                        nodes.append(node)
        return nodes

