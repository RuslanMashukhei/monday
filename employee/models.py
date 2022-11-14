import datetime
from django.db import models

class AbstractPerson(models.Model):
    name = models.CharField(max_length=20)
    birth_date = models.DateField(default='20.07.2005')

    def get_age(self):
        age = datetime.datetime.now() - birth_date
        return age
    def __str__(self):
        return self.name

class Employee(AbstractPerson):
    #super().__init__(self, name, birth_date, position, salary_ work_experience)
    position = models.CharField(max_length=20)
    salary = models.IntegerField(default=1000)
    work_experience = models.CharField(max_length=200)

    def __str__(self):
        return self.position

class Passport(models.Model):
    inn = models.CharField(max_length=100)
    id_card = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def get_gender(self):
        if inn.startswith(1):
            return "Male"
        else:
            return "Female"

    def __str__(self):
        return self.inn


class WorkProject(models.Model):
    project_name = models.CharField(max_length=50)
    employee = models.ManyToManyField(Employee, through="Membership")
    def __str__(self):
        return self.project_name

class Membership(models.Model):
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.postion} - {self.project_name}"

class Client(AbstractPerson):
    address = models.CharField(default='Street Ptushkina')
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address} - {self.phone_number}"

class VIPClient():
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()
    client = models.ManyToManyField(Client, through="Membership")
