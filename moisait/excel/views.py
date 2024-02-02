from django.shortcuts import render
from .models import Timetabl
def excelh(request):
    timetablos = Timetabl.objects.all()
    return render(request,'excel/basa.html',{'timetablos': timetablos})
# Create your views here.
