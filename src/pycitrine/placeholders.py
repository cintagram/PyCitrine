import re

class PlaceholderHandler:
    @staticmethod
    def ReplacePlaceholders(text, values):
        """Replace placeholders in text with provided values."""
        def replace_match(match):
            placeholder = match.group(0)
            key = placeholder[2:-2]  # Extract key from <@key/>
            return str(values.get(key, f"<Placeholder '{key}' not found>"))

        # Find all placeholders in the format <@key/>
        return re.sub(r'<@\w+/?>', replace_match, text)

    @staticmethod
    def Locate(text, key):
        """Locate a placeholder in the text and return its value."""
        pattern = f"<@{key}/>"
        matches = re.findall(pattern, text)
        if matches:
            return matches[0]  # Simplified extraction, adjust as needed
        return f"Placeholder '{key}' not found."