import xml.etree.ElementTree as ET

class CtrFormatParser:
    @staticmethod
    def CtrToDict(ctr_data):
        """Convert Citrine format data to a dictionary."""
        root = ET.fromstring(ctr_data)

        def parse_element(elem):
            if elem is None:
                return None
            if elem.tag == 'CtrDict':
                return {child.find('CtrKey').text: parse_element(child.find('CtrValue')) for child in elem if child.find('CtrKey') is not None}
            elif elem.tag == 'CtrList':
                return [parse_element(child) for child in elem if child is not None]
            elif elem.tag == 'CtrItem':
                return parse_element(elem[0]) if len(elem) > 0 else None
            else:
                return elem.text.strip() if elem.text is not None else ''

        return parse_element(root)

    @staticmethod
    def DictToCtr(data):
        """Convert a dictionary to Citrine format XML."""
        def dict_to_element(data):
            if isinstance(data, dict):
                element = ET.Element('CtrDict')
                for key, value in data.items():
                    key_element = ET.SubElement(element, 'CtrKey')
                    key_element.text = key
                    value_element = dict_to_element(value)
                    if value_element is not None:
                        element.append(value_element)
                return element
            elif isinstance(data, list):
                list_element = ET.Element('CtrList')
                for item in data:
                    item_element = ET.SubElement(list_element, 'CtrItem')
                    item_sub_element = dict_to_element(item)
                    if item_sub_element is not None:
                        item_element.append(item_sub_element)
                return list_element
            else:
                value_element = ET.Element('CtrValue')
                value_element.text = str(data)
                return value_element

        root_element = dict_to_element(data)
        return ET.tostring(root_element, encoding='unicode')

    @staticmethod
    def ParseDataFormat(xml_data):
        """Parse the XML data format including Prompts and Metadata."""
        root = ET.fromstring(xml_data)
        data = {}
        
        # Extract Prompts
        prompts_elem = root.find('Prompts')
        if prompts_elem is not None:
            prompts = {}
            for child in prompts_elem:
                if child.tag == 'Text':
                    prompts['text'] = child.text
                elif child.tag == 'Dynamic':
                    name = child.get('name')
                    dtype = child.get('type')
                    default = child.get('default')
                    prompts[name] = {
                        'type': dtype,
                        'default': default,
                        'value': child.text
                    }
            data['prompts'] = prompts
        
        # Extract Metadata
        metadata_elem = root.find('Metadata')
        if metadata_elem is not None:
            metadata = {}
            for child in metadata_elem:
                metadata[child.tag] = child.text
            data['metadata'] = metadata

        return data