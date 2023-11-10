from django.http import HttpResponse
from django.shortcuts import render
from notice.models import notice,Head_Master_Message, Sliders, Gallery, smc, club, result
from student.models import student
#from django.views.generic import ListView, DetailView

# Create your views here.
def index(request):
    sidenotice=notice.objects.all().order_by('-notice_date')
    latestnotice=notice.objects.all().order_by('-notice_date')[:1]
    head=Head_Master_Message.objects.all()[:1]
    slider=Sliders.objects.all()
    gallery=Gallery.objects.all()
    sixboy=student.objects.filter(gender='Boy', class_name='6').count()
    sixgirl=student.objects.filter(gender='Girl', class_name='6').count()
    six = student.objects.filter(class_name='6').count()
    sevenboy=student.objects.filter(gender='Boy', class_name='7').count()
    sevengirl=student.objects.filter(gender='Girl', class_name='7').count()
    seven = student.objects.filter(class_name='7').count()
    eightboy=student.objects.filter(gender='Boy', class_name='8').count()
    eightgirl=student.objects.filter(gender='Girl', class_name='8').count()
    eight = student.objects.filter(class_name='8').count()
    nineboy=student.objects.filter(gender='Boy', class_name='9').count()
    ninegirl=student.objects.filter(gender='Girl', class_name='9').count()
    nine = student.objects.filter(class_name='9').count()
    tenboy=student.objects.filter(gender='Boy', class_name='10').count()
    tengirl=student.objects.filter(gender='Girl', class_name='10').count()
    ten = student.objects.filter(class_name='10').count()
    return render(request, "index.html",{'side': sidenotice, 'latest': latestnotice,'head':head,'slidersshow':slider,'galleryshow':gallery,'sixboyshow':sixboy,'sixgirlshow':sixgirl,'sevenboyshow':sevenboy,'sevengirlshow':sevengirl,'eightboyshow':eightboy,'eightgirlshow':eightgirl,'nineboyshow':nineboy,'ninegirlshow':ninegirl,'tenboyshow':tenboy,'tengirlshow':tengirl,'totalsix':six,'totalseven':seven,'totaleight':eight,'totalnine':nine,'totalten':ten})
#notice page
def notice_view(request):
    show_notice=notice.objects.all().order_by('-notice_date')
    return render(request, "notices/notice.html",{'sn': show_notice})

def gallery_view(request):
    showgallery=Gallery.objects.all()
    return render(request, "gallery.html",{'showgal': showgallery})

# notice details page
def notice_details(request,id): 
    noticedetails=notice.objects.get(id=id)
    return render(request, "notices/notice_details.html", {'nd': noticedetails})
#smc page
def smc_view(request):
    showsmc=smc.objects.all()
    return render(request, "smc.html",{'showsmc': showsmc})

#club page
def club_view(request):
    showclub=club.objects.all()
    return render(request, "club.html",{'showclub': showclub})

#school result page
def result_view(request):
    showresult=result.objects.all()
    return render(request, "school-result.html",{'showresult': showresult})

