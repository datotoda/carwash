from django.contrib import admin

from wash.models import Human, Car, Branch, Staff, Box, Order


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    readonly_fields = ['Added', 'updated']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
