class Extension:
    def __init__(self, data):
        """
        Accepts a row from extensions.csv and assigns values to properties.
        """
        self.id = data['Id']
        self.category = data['Category']
        self.core = data['Core'] == 'true'
