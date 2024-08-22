from pycitrine.dynamic import DynamicData
from pycitrine.file_handler import FileHandler
from pycitrine.converter import DataConverter
from pycitrine.utils import Utils
from pycitrine.placeholders import PlaceholderHandler

# Define data with multiple placeholders in one dynamic field
citrine_data = """
<DataFormat>
  <Prompts>
    <Text>Welcome to our application!</Text>
    <Dynamic name="UserGreeting" type="str" default="Hello"><@GreetingMsg/> <@UserName/>, you have <@UnreadMessages/> unread messages.</Dynamic>
    <Dynamic name="GreetingMsg" type="str" default="Hi">Hi</Dynamic>
    <Dynamic name="UserName" type="str" default="Guest">Alice</Dynamic>
    <Dynamic name="UnreadMessages" type="int" default="0">5</Dynamic>
  </Prompts>
  
  <Metadata>
    <Author>Jane Doe</Author>
    <Version>1.0</Version>
    <LastUpdated>2024-08-22</LastUpdated>
  </Metadata>
</DataFormat>
"""

# Extract and resolve multiple placeholders
print("Original Data with Placeholders:")
print(citrine_data)

# Replace placeholders using dynamic values
replaced_data = PlaceholderHandler.ReplacePlaceholders(citrine_data, {
    "GreetingMsg": "Hello",
    "UserName": "Alice",
    "UnreadMessages": 5
})
print("\nData with Multiple Placeholders Replaced:")
print(replaced_data)

# Extract specific dynamic field
dynamic_value = DynamicData.Locate(replaced_data, "UserGreeting")
print("\nResolved Dynamic Field 'UserGreeting':")
print(dynamic_value)