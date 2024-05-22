from django.contrib import admin
from .models import TodoItem, Customer, News
from django.contrib.auth.models import User
from django.contrib import admin




admin.site.register(News)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'booking_date', 'booking_time', 'display_number_of_people')

    def display_number_of_people(self, obj):
        return obj.number_of_people

    display_number_of_people.short_description = 'Number of People'

admin.site.register(Customer, CustomerAdmin)









