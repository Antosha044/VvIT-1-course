class Employee:
    def __init__(self,name,id,**kwargs):
        self.name=name
        self.id=id
    def get_info(self):
        return "Сотрудник {} с id {}".format(self.name,self.id)
    def code(self):
        return "Двоичный код id = {}".format(bin(int(self.id))[2:])

class Manager(Employee):
     def __init__(self,name,id,department,salary,project_name,period,**kwargs):
         super().__init__(name,id,**kwargs)
         self.department=department
         self.salary=salary
         self.project_name=project_name
         self.period=period
     def get_info_manager(self):
        return "Менеджер {} с id {} из отдела {}  с зарплатой {}".format(self.name,self.id,self.department,self.salary)
     def manage_project(self):
         return "{} управляет проектом {}. Срок реализации до {}".format(self.name,self.project_name,self.period)

class Technician(Employee):
    def __init__(self,name,id,specialization,test_score,**kwargs):
        super().__init__(name,id,**kwargs)
        self.specialization=specialization
        self.test_score=test_score
    def perform_maintenance(self):
        return "{} Выполняет техническое обслуживание".format(self.name)
    def demolition(self):
        return "{} снес все БД с сервера".format(self.name)
    def get_info_technician(self):
        return "{}: Специализая - {}, результат теста по специализации - {} баллов".format(self.name,self.specialization,self.test_score).format(self.name,self.specialization,self.test_score)
class TechManager(Technician,Manager):
    def __init__(self, name, id, department=None, salary=None, project_name=None, period=None, specialization=None, test_score=None):
        super().__init__(name, id,department=department,salary=salary,project_name=project_name,period=period, specialization=specialization, test_score=test_score)

        self.team=[]
    def manage_project(self):
        return super().manage_project()
    def add_employee(self,employee):
        self.team.append(employee)
        print("{} принят в команду".format(employee.name))
    def get_team_info(self):
        information='Список сотрудников: \n'
        for employers in self.team:
            information+=employers.get_info() + '\n'
        return information

Vazgen=Manager('Вазген','2291','закупка авто','2 шаурмы в неделю','Чип-тюнинг служебных авто','август 2027')

Robert_Polson=Technician('Роберт','1234','технический специалист','50')

tayler=TechManager('Тайлер','1337','развитие','90 тысяч рублей','Проект разгром','второй квартал 2028 года','Магистр Линукса','99')

tayler.add_employee(Robert_Polson)
tayler.add_employee(Vazgen)
print(Vazgen.get_info_manager())
print(tayler.get_team_info())