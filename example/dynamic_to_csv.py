from pycitrine.dynamic_csv_converter import DynamicCSVConverter

# Example data with placeholders
citrine_data = """
<DataFormat>
  <Prompts>
    <Dynamic name="UserGreeting" type="str" default="Hello">Hello <@UserName/>, welcome to our service.</Dynamic>
    <Dynamic name="UserName" type="str" default="Guest">Alice, Bob</Dynamic>
    <Dynamic name="UnreadMessages" type="int" default="0">5</Dynamic>
  </Prompts>
</DataFormat>
"""

values_dict = {
    'UserName': 'Alice, Bob',  # Note the comma in the value
    'UnreadMessages': '5'
}

# Convert dynamic data from Citrine format to CSV
csv_file_path = 'dynamic_fields.csv'
DynamicCSVConverter.DynamicToCSV(citrine_data, csv_file_path, values_dict)
print("Converted dynamic fields to CSV.")