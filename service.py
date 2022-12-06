from models import Habit_Model, User_Model

class User_Service:
    def __init__(self):
        self.model = User_Model()

    def create_user(self, params):
        return self.model.create_user(params)

    def check_user(self, username, password):
        return self.model.check_user(username, password)



class Habit_Service:
    def __init__(self):
        self.model = Habit_Model()

    def create_habit(self, params):
        return self.model.create_habit(params)

    def list_all_habit(self, user_id):
        return self.model.list_habit(user_id)

    def list_by_id(self, item_id):
        response = self.model.get_by_id(item_id)
        return response

    def update_habit(self, user_id, params):
        print(params)
        return self.model.update_habit(user_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

