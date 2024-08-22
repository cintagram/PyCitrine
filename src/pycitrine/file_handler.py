class FileHandler:
    @staticmethod
    def ReadFile(file_path):
        """Read the Citrine format data from a file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    @staticmethod
    def WriteFile(file_path, data):
        """Write the Citrine format data to a file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)