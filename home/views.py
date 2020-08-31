from django.shortcuts import render,redirect
from urunler.models import Urunler,Category
from .models import Sepet,Filtrele,Siparislerim
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages



def index(request):
    urunler=Urunler.objects.all().order_by('-upload_date')
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    uyari = False
    eklendi= False
    if request.method=="POST":
        id=request.POST.get("urun")
        category=request.POST.get("category")
        if len(Sepet.objects.filter(product_id=id))>0:
            uyari=True
        else:
            urun=Urunler.objects.get(id=id)
            Sepet.objects.create(product=urun)
            eklendi= True
        if category!="tumu":
            if uyari:
                messages.add_message(request, messages.INFO, "uyari")
            else:
                messages.add_message(request, messages.INFO, "eklendi")
            return redirect(request.META["HTTP_REFERER"])
    context={
        "urunler":urunler,
        "kategoriler":kategoriler,
        "filtre":filtre,
        "category":"tumu",
        "uyari":uyari,
        "eklendi":eklendi
    }
    return render(request,"home.html",context)


def giris(request):
    mesaj=""
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,username=email,password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        mesaj="Kullanıcı adı veya şifre yanlış."
    context={"msg":mesaj}
    return render(request,"login.html",context)

def kayit(request):
    if request.method=="POST":
        isim=request.POST.get("isim")
        soyisim=request.POST.get("soyisim")
        email=request.POST.get("email")
        password=request.POST.get("password")
        password_again=request.POST.get("password_again")
        if not (len(email) and len(password) and len(password_again) and len(isim) and len(soyisim)):
            mess="Tüm alanlar doldurulmalı."
            context={
                "msg":mess
            }
            return render(request, "kayit.html",context)
        else:
            pass
            user=User.objects.create_user(username=email,email=email,password=password)
            user.first_name=isim
            user.last_name=soyisim
            user.save()
            login(request, user)
            return redirect("/")
    return render(request,"kayit.html")

def iletisim(request):
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    context={
        "kategoriler":kategoriler,
        "filtre":filtre
    }
    return render(request,"iletişim.html",context)

def sepetim(request):
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    if request.method=="POST":
        id=request.POST.get("sepetten_sil")
        Sepet.objects.filter(id=id).delete()
        return redirect("sepetim")
    sepet=Sepet.objects.all()
    toplam=0
    for i in sepet:
        toplam+=i.product.price
    context={
        "sepet":sepet,
        "toplam":"  "+str(toplam),
        "toplam_urun":sepet,
        "kategoriler":kategoriler,
        "filtre":filtre
    }

    return render(request,"sepetim.html",context)


def sepeti_sil(request):
    if request.method=="POST":
        Sepet.objects.all().delete()
        return redirect("sepetim")

def ara(request):
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    if request.method=="POST":
        urun=request.POST.get("ara")
        urunler=Urunler.objects.filter(name__icontains=urun)
        urun_yok=False
        if len(urunler)==0:
            urun_yok=True
        context = {
            "urunler": urunler,
            "urun_yok": urun_yok,
        "kategoriler":kategoriler,
            "filtre":filtre
        }
        return render(request,"search.html",context)
    return redirect("home")
def icerik(request,id):
    urun=Urunler.objects.get(id=id)
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    context={"urun":urun,
             "kategoriler":kategoriler,
             "filtre":filtre}
    return render(request,"urun_icerigi.html",context)


def kategori(request,id,name):
    category=Category.objects.get(id=id)
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    urunler=Urunler.objects.filter(category=category)
    urun_yok=False
    if len(urunler)==0:
        urun_yok=True
    veri=get_messages(request)
    uyari=False
    eklendi=False
    bilgi=""
    for i in veri:
        bilgi=str(i)
        break
    if bilgi=="uyari":
        uyari=True
    elif bilgi=="eklendi":
        eklendi=True
    context={
        "urunler":urunler,
        "urun_yok":urun_yok,
        "kategoriler": kategoriler,
        "filtre":filtre,
        "category":category.category_name,
        "uyari":uyari,
        "eklendi":eklendi
    }
    return render(request,"search.html",context)

def filtre(request,id,name):
    global urunler
    kategoriler=Category.objects.all()
    filtreler=Filtrele.objects.all()
    filte=Filtrele.objects.get(id=id)
    if filte.id==1:
        if name=="tumu":
            urunler = Urunler.objects.all().order_by('-price')
        else:
            urunler=Urunler.objects.filter(category__category_name=name).order_by('-price')
    if filte.id==2:
        if name=="tumu":
            urunler = Urunler.objects.all().order_by('price')
        else:
            urunler=Urunler.objects.filter(category__category_name=name).order_by('price')
    if filte.id==3:
        if name=="tumu":
            urunler = Urunler.objects.all().order_by('-upload_date')
        else:
            urunler=Urunler.objects.filter(category__category_name=name).order_by('-upload_date')
    if filte.id==4:
        if name=="tumu":
            urunler = Urunler.objects.all().order_by('upload_date')
        else:
            urunler=Urunler.objects.filter(category__category_name=name).order_by('upload_date')
    context={
        "urunler":urunler,
        "kategoriler":kategoriler,
        "filtre":filtreler,
        "category":name
    }
    return render(request,"search.html",context)

def siparis_et(request):
    sepet=Sepet.objects.all()
    kategoriler=Category.objects.all()
    filtre=Filtrele.objects.all()
    for i in sepet:
        Siparislerim.objects.create(siparislerim=i.product)
    Sepet.objects.all().delete()
    siparislerim=Siparislerim.objects.all()
    toplam=0
    for i in siparislerim:
        toplam+=i.siparislerim.price
    context={
        "toplam":toplam,
        "siparislerim":siparislerim,
        "kategoriler":kategoriler,
        "filtre":filtre,
    }
    return render(request,"siparislerim.html",context)
