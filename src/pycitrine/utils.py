class Utils:
    @staticmethod
    def EncodeUtf8(data):
        """Encode data to UTF-8."""
        return data.encode('utf-8')

    @staticmethod
    def DecodeUtf8(data):
        """Decode UTF-8 data."""
        return data.decode('utf-8')

    @staticmethod
    def EncodeAscii(data):
        """Encode data to ASCII."""
        return data.encode('ascii', 'ignore')

    @staticmethod
    def DecodeAscii(data):
        """Decode ASCII data."""
        return data.decode('ascii')