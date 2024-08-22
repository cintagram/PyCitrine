import xml.etree.ElementTree as ET

class DynamicData:
    @staticmethod
    def ExtractDynamicFields(citrine_data):
        """Extract dynamic fields from Citrine data."""
        from xml.etree import ElementTree as ET
        
        tree = ET.ElementTree(ET.fromstring(citrine_data))
        dynamic_elements = tree.findall('.//Dynamic')
        
        dynamic_fields = []
        for elem in dynamic_elements:
            dynamic_fields.append({
                'name': elem.attrib.get('name'),
                'type': elem.attrib.get('type'),
                'default': elem.attrib.get('default'),
                'value': elem.text
            })
        
        return dynamic_fields

    @staticmethod
    def Locate(citrine_data, name):
        """Locate and return the value of a specific dynamic field by name."""
        tree = ET.ElementTree(ET.fromstring(citrine_data))
        root = tree.getroot()
        
        # Search for Dynamic elements by name
        for dynamic in root.findall(".//Dynamic"):
            if dynamic.get('name') == name:
                return ''.join(dynamic.itertext()).strip()
        
        raise ValueError(f"Dynamic field '{name}' not found.")