# class Car:
#     def __init__(self, model):
#         self.model = model
#
#     def get_model(self):
#         print(self.model)
#
#     def set_model(self, model):
#         self.model = model
#
#
# toyota = Car('Civic')
# toyota.get_model()
# toyota.set_model('New model')
# toyota.get_model()

class Car:
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        print(self.__model)

    @model.setter
    def model(self, model):
        self.__model = model


toyota = Car('Civic')
toyota.model
toyota.model = 'New civic'
toyota.model
