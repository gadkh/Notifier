class Controller:

    def __init__(self, name):
        self.name = name

    def get_message(self):
        return {"message": "{} controller work !".format(self.name)}
