from django.contrib import messages

from .models import Category

def validate(request, form):
    errors = False
    
    if form.price <= 0:
        messages.error(request, "The price must be higher than $0")
        errors = True
    
    if len(form.title) > 50:
        messages.error(request, "The title must be under 50 characters.")
        errors = True
    
    if form.categ not in Category.objects.all():
        messages.error(request, "Invalid category.")
        errors = True

    return errors