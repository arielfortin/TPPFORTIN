from django.db import models

class Professional(models.Model):
    PROFESSION_CHOICES = [
        ('Matemática', 'Profesor de Matemática'),
        ('Lenguaje', 'Profesor de Lenguaje'),
        ('Domicilio', 'Educadora Diferencial Domicilio'),
        ('IT', 'Consultor IT'),
    ]
    first_name = models.CharField("Nombres", max_length=80)
    last_name = models.CharField("Apellidos",max_length=80)
    email = models.EmailField("Correo Eléctronico",unique=True)
    profession = models.CharField("Profesional",max_length=50, choices=PROFESSION_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.profession}"


class Client(models.Model):
    name = models.CharField("Nombre:", max_length=100)
    email = models.EmailField("Correo Electrónico", unique=True)
    phone = models.CharField("Celular", max_length=20)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    professional = models.ForeignKey(
        'Professional',
        verbose_name="Profesional",
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        'Client',
        verbose_name="Cliente",
        on_delete=models.CASCADE
    )
    date = models.DateField("Fecha")
    time = models.TimeField("Hora")

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

    def __str__(self):
        return f"{self.client} con {self.professional} el {self.date} a las {self.time}"
