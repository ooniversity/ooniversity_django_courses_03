from django.shortcuts import render, get_object_or_404
from courses.models import *

def view_item(request, obj_id, obj_class):
    class_name = obj_class.__name__.lower()
    obj = get_object_or_404(obj_class, id=obj_id)
    return render(request, '%s/item.html' % class_name, {class_name: obj})
