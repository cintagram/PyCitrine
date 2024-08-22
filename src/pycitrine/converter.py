import json
import csv
from .parser import CtrFormatParser

class DataConverter:
    @staticmethod
    def JsonToCtr(json_data):
        """Convert JSON data to Citrine format."""
        dict_data = json.loads(json_data)
        return CtrFormatParser.DictToCtr(dict_data)

    @staticmethod
    def CtrToJson(ctr_data):
        """Convert Citrine format data to JSON."""
        dict_data = CtrFormatParser.CtrToDict(ctr_data)
        return json.dumps(dict_data, indent=4)

    @staticmethod
    def CsvToCtr(csv_file):
        """Convert CSV file to Citrine format."""
        dict_data = {}
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row['Key']
                value = row['Value']
                dict_data[key] = value
        return CtrFormatParser.DictToCtr(dict_data)

    @staticmethod
    def CtrToCsv(ctr_data, csv_file):
        """Convert Citrine format data to CSV file."""
        dict_data = CtrFormatParser.CtrToDict(ctr_data)
        with open(csv_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Key', 'Value'])
            for key, value in dict_data.items():
                writer.writerow([key, value])