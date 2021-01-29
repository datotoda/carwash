from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=50, verbose_name="human name")
    last_name = models.CharField(max_length=100, verbose_name="human last name")
    phone = models.CharField(max_length=20, verbose_name="phone number")
    Added = models.DateTimeField(verbose_name="Added Date/Time", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated Date/Time", auto_now=True)

    class Meta:
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)



class Car(models.Model):
    manufacturer = models.CharField(max_length=50, verbose_name="car manufacturer")
    model = models.CharField(max_length=50, verbose_name="car model", null=True, blank=True)
    color = models.CharField(max_length=50, verbose_name="car color",  null=True, blank=True)
    gear = models.CharField(max_length=50, verbose_name="gear box type")
    code = models.CharField(max_length=20, verbose_name="car number", unique=True)
    type = models.CharField(max_length=20, verbose_name="car type")
    owner = models.ForeignKey(to='wash.Human', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return "%s %s - %s" % (self.manufacturer, self.model, self.owner)


class Branch(models.Model):
    name = models.CharField(max_length=50, verbose_name="branch name")
    location = models.CharField(max_length=20, verbose_name="branch address")

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branch'

    def __str__(self):
        return self.name


class Box(models.Model):
    number = models.CharField(max_length=50, verbose_name="box number")
    location = models.ForeignKey(to='wash.Branch', on_delete=models.PROTECT)
    is_free = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Box'
        verbose_name_plural = 'Boxes'

    def __str__(self):
        return "%s (%s)" % (self.location, self.number)


class Staff(models.Model):
    human = models.ForeignKey(to='wash.Human', on_delete=models.PROTECT)
    job_location = models.ForeignKey(to='wash.Branch', on_delete=models.PROTECT)
    job = models.CharField(max_length=50, verbose_name="position")
    salary = models.CharField(max_length=20, verbose_name="salary")

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Staff'

    def __str__(self):
        return "%s %s" % (self.human.name, self.human.last_name)


class Order(models.Model):
    human = models.ForeignKey(to='wash.Human', on_delete=models.PROTECT)
    car = models.ForeignKey(to='wash.Car', on_delete=models.PROTECT)
    washer = models.ForeignKey(to='wash.Staff', on_delete=models.PROTECT)
    cost = models.CharField(max_length=20, verbose_name="cost")
    started = models.DateTimeField(verbose_name="Started Date/Time", auto_now_add=True)
    ended = models.DateTimeField(verbose_name="Ended Date/Time", null=True, blank=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return "%s %s - %s %s" % (self.car.manufacturer, self.car.model, self.human.name, self.human.last_name)
