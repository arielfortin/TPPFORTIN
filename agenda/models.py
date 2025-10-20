from django.db import models


class Professional(models.Model):
    PROFESSION_CHOICES = [
    ('MAT', 'Profesor Matemáticas'),
    ('LEN', 'Profesor Lenguaje'),
    ('EDIF', 'Educadora Diferencial Domicilio'),
    ('IT', 'Consultor IT'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


def __str__(self):
    return f"{self.first_name} {self.last_name} - {self.get_profession_display()}"




class Client(models.Model):
    # modelo simple para quien agenda
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


def __str__(self):
    return self.name




class Appointment(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='appointments')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)


class Meta:
    unique_together = ('professional', 'date', 'time') # evita doble reserva exacta


def __str__(self):
    return f"{self.date} {self.time} - {self.professional} ({self.client})"