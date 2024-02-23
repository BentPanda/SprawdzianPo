class DataStore:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def get_all_users(self):
        return self.users

    def get_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def add_user(self, user_data):
        user_data['id'] = self.next_id
        self.users.append(user_data)
        self.next_id += 1
        return user_data

    def update_user(self, user_id, update_data):
        for user in self.users:
            if user['id'] == user_id:
                user.update(update_data)
                return user
        return None

    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user['id'] == user_id:
                del self.users[i]
                return True
        return False
