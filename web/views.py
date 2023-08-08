from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import redirect
from django.contrib import messages

from .forms import ContactForm
from .models import Nutshell
from .models import Gallery
# def index(request):
#     context = {"is_index": True}
#     return render(request, "web/index.html", context)




def index(request):
    context = {"is_index": True,
               "nutshell":Nutshell.objects.all()}
    return render(request, "web/index.html", context)

def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)
 
def gallery(request):
    context = {"is_gallery": True,
               "gallery":Gallery.objects.all()}
    return render(request, "web/gallery.html", context)

# def contact(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             response_data = {
#                 "status": "true",
#                 "title": "Successfully Submitted",
#                 "message": "Message successfully updated",
#             }
#         else:
#             print(form.errors)
#             response_data = {
#                 "status": "false",
#                 "title": "Form validation error",
#             }
#         return HttpResponse(
#             json.dumps(response_data), content_type="application/javascript"
#         )
#     else:
#         context = {
#             "is_contact": True,
#             "form": form,
#         }
#     return render(request, "web/connect.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        messages.success(request,"succsessfully saved")
        return redirect('/contact')
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/connect.html",context)