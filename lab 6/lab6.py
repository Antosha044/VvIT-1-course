class UserAccount:
    def __init__(self,username,email,password):
        self.username=username
        self.email=email
        self.__password=password
    def set_password(self,new_password):
        self.__password=new_password
    def check_password(self,password):
        if self.__password==password:
            return True
        else:
            return False
    def get_password(self):
        return "пароль {}".format(self.__password)
user_account=UserAccount('Pazhiloy_Kebab','Glad_Valakas123@mail.ru','12345')
#print(user_account.check_password('111'))

class Vehicle():
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def get_info(self):
        return "Т/с марки {} модель {} ".format(self.make,self.model)
class Car(Vehicle):
    def __init__(self,make,model,fuel_type):
        self.fuel_type=fuel_type
        super().__init__(make,model)
    def get_info(self):
        return "Т/с марки {} модель {} с видом топлива {} ".format(self.make, self.model,self.fuel_type)
car=Car('vaz','2105','gaz')
print(car.get_info())