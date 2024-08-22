import csv
from pycitrine.dynamic import DynamicData

class DynamicCSVConverter:
    @staticmethod
    def DynamicToCSV(citrine_data, csv_file, values_dict=None):
        """Convert dynamic data from Citrine format to CSV, resolving placeholders and escaping commas."""
        if values_dict is None:
            values_dict = {}
        
        # Extract dynamic fields from Citrine data
        dynamic_fields = DynamicData.ExtractDynamicFields(citrine_data)
        
        # Open CSV file for writing
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Type', 'Value'])
            
            for field in dynamic_fields:
                name = field.get('name')
                type_ = field.get('type')
                default = field.get('default')
                value_template = field.get('value')
                
                # Resolve placeholders
                value = DynamicCSVConverter._resolve_placeholders(value_template, values_dict, default)
                
                # Escape commas in the value
                if ',' in value:
                    value = f'"{value}"'
                
                writer.writerow([name, type_, value])
    
    @staticmethod
    def _resolve_placeholders(value_template, values_dict, default):
        """Resolve placeholders in value template using provided values or default."""
        import re
        
        # Function to replace placeholders
        def replace_placeholder(match):
            key = match.group(1)
            return values_dict.get(key, f"<@{key}/>")

        # Replace placeholders in the value template
        resolved_value = re.sub(r'<@(\w+)>/', replace_placeholder, value_template)
        
        # Return resolved value or default if no value is provided
        if '<@' in resolved_value and default is not None:
            resolved_value = default
        elif '<@' in resolved_value:
            raise ValueError(f"Missing values for placeholders: {resolved_value}")
        
        return resolved_value