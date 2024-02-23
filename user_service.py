from datetime import datetime
from data_store import DataStore

class UserService:
    def __init__(self):
        self.data_store = DataStore()

    def get_all_users(self):
        return [self._convert_to_return_format(user) for user in self.data_store.get_all_users()]

    def get_user(self, user_id):
        user = self.data_store.get_user(user_id)
        if user:
            return self._convert_to_return_format(user)
        return None

    def create_user(self, user_data):
        user = self.data_store.add_user(user_data)
        return self._convert_to_return_format(user)

    def update_user(self, user_id, user_data):
        user = self.data_store.update_user(user_id, user_data)
        if user:
            return self._convert_to_return_format(user)
        return None

    def delete_user(self, user_id):
        return self.data_store.delete_user(user_id)

    def _convert_to_return_format(self, user):
        return {
            'id': user['id'],
            'firstName': user['firstName'],
            'lastName': user['lastName'],
            'age': datetime.now().year - user['birthYear'],
            'group': user['group']
        }
