class User:
    def __init__(self, data): # data == a dictionary
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_one():
        response = [{
            'id': 1,
            'first_name': "tyler",
            'last_name': "Tbo",
            'email': 'tt@email.com',
            'password': 'thibault',
            'created_at': '1900/01/01',
            'updated_at': '1900/01/01'
        }]

    tyler = User()