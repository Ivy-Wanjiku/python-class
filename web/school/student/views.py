from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm
# Create your views here.
def register_student(request):
    # form=StudentRegistationForm()
    # return render(request,"student/register_student.html", {"form":form})
    if request.method=="POST":
        form= StudentRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("register_student")
    else:
        form=StudentRegistrationForm()
    return render(request,"student/register_student.html", {"form":form})