from django.shortcuts import render
from django.template import RequestContext
from models import Blog


def index(request):
    if request.method == "POST":
        form_data = request.POST

        data_update = Blog(First_name=form_data['First_name'], Last_name=form_data['Last_name'],
                           Street_add=form_data['Street_add'],Street_add2=form_data['Street_add2'],
                           city=form_data['city'],state=form_data['state'], zip=form_data['zip'],
                           email=form_data['email'],areac=form_data['areac'],phone=form_data['phone'])
        data_update.save()
        return render(request, 'index.html',{'abc':data_update})
    else:
        name = 'this is else'
        return render(request, 'index.html',{'name':name})


def me(request):
    abc = Blog.objects.all()
    return render(request,'train_me/db2html.html',{'abc':abc})



