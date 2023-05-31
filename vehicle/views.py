from django.db.models import Q, Sum
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random
from django.utils import timezone
from datetime import timedelta
# Create your views here.

def Index(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        ar_l = Parkings.objects.filter(location__contains=query)
        print(query)
        print(len(ar_l))

        context = {'details': ar_l, 'msg': ''}
        return render(request, 'index.html', context)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def navbar(request):
    return render(request, 'navbar.html')

def user_view_outgoing(request,pid):

    vehicle = Vehicle.objects.get(id=pid)

    d = {'vehicle': vehicle}
    return render(request, 'user_view_outgoing.html',d)




def userhome(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        ar_l = Parkings.objects.filter(location__contains=query)
        print(query)
        print(len(ar_l))

        context = {'details': ar_l, 'msg': ''}
        return render(request, 'user_home.html', context)
    return render(request, 'user_home.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    today = datetime.now().date()
    yesterday = today - timedelta(1)
    lasts = today - timedelta(7)

    tv = Vehicle.objects.filter(pdate=today).count()
    yv = Vehicle.objects.filter(pdate=yesterday).count()
    ls = Vehicle.objects.filter(pdate__gte=lasts,pdate__lte=today).count()
    totalv = Vehicle.objects.all().count()
    total_charges = Booking.objects.aggregate(total=Sum('parkingcharge'))['total']


    d = {'tv':tv,'yv':yv,'ls':ls,'totalv':totalv,"total":total_charges}

    return render(request,'admin_home.html',d)


def Logout(request):
    logout(request)
    return redirect('index')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == "POST":
        o = request.POST['password']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'change_password.html',d)


def add_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        cn = request.POST['categoryname']
        try:
            Category.objects.create(categoryname=cn)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_category.html', d)

def manage_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.all()
    d = {'category':category}
    return render(request, 'manage_category.html', d)


def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('manage_category')

def edit_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        cn = request.POST['categoryname']
        category.categoryname = cn
        try:
            category.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category}
    return render(request, 'edit_category.html',d)


def add_vehicle(request):
    u=request.session['user_id']
    user=User_login.objects.get(id=u)
    category1 = Category.objects.all()
    if request.method=="POST":
        pn = str(random.randint(10000000, 99999999))
        ct = request.POST['category']
        vc = request.POST['vehiclecompany']
        rn = request.POST['regno']
        on = request.POST['ownername']
        oc = request.POST['ownercontact']
        pd = request.POST['pdate']

        status = "In"
        category = Category.objects.get(categoryname=ct)


        v=Vehicle.objects.create(parkingnumber=pn,category=category,vehiclecompany=vc,regno=rn,ownername=on,ownercontact=oc,pdate=pd,parkingcharge='',remark='',status=status,user=user)
        v.save()
        return redirect("http://127.0.0.1:8000/user_home")

    d = {'category1':category1}
    return render(request, 'add_vehicle.html', d)

def manage_incomingvehicle(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = Vehicle.objects.filter(status="In")
    d = {'vehicle':vehicle}
    return render(request, 'manage_incomingvehicle.html', d)

def view_incomingdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_home')
    error = ""
    vehicle = Vehicle.objects.get(id=pid)

    d = {'vehicle': vehicle,'error':error}
    return render(request,'view_incomingdetail.html', d)


def manage_outgoingvehicle(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = Booking.objects.filter(status="Out" )
    d = {'vehicle':vehicle}
    return render(request, 'manage_outgoingvehicle.html', d)


def view_outgoingdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    book = Booking.objects.get(id=pid)

    d = {'vehicle': book}
    return render(request,'view_outgoingdetail.html', d)


def print_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    vehicle = Vehicle.objects.get(id=pid)

    d = {'vehicle': vehicle}
    return render(request,'print.html', d)


def search(request):
    q = None
    if request.method == 'POST':
        q = request.POST['searchdata']
    try:
        vehicle = Vehicle.objects.filter(Q(parkingnumber=q))
        vehiclecount = Vehicle.objects.filter(Q(parkingnumber=q)).count()

    except:
        vehicle = ""
    d = {'vehicle': vehicle,'q':q,'vehiclecount':vehiclecount}
    return render(request, 'search.html',d)


def betweendate_reportdetails(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'betweendate_reportdetails.html')



def betweendate_report(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        vehicle = Vehicle.objects.filter(Q(pdate__gte=fd) & Q(pdate__lte=td))
        vehiclecount = Vehicle.objects.filter(Q(pdate__gte=fd) & Q(pdate__lte=td)).count()
        d = {'vehicle': vehicle,'fd':fd,'td':td,'vehiclecount':vehiclecount}
        return render(request, 'betweendate_reportdetails.html', d)
    return render(request, 'betweendate_report.html')

def user_details_add(request):
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        username=email
        #status = "new"

        if  User_details.objects.filter(email=email).exists():
            context = {'msg': 'User already exists'}
            return render(request, 'user_details_add.html', context)
        print(email)

        ul = User_login(username=email, password=password, u_type='user')
        ul.save()
        um=User_login.objects.get(username=email)
        user_id =um.id
        print(user_id)

        ud = User_details(user_id=user_id,first_name=first_name, last_name=last_name, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'user_login.html',context)

    else:
        return render(request, 'user_details_add.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        ul = User_login.objects.filter(username=username, password=password, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].username
            print(request.session['user_id'])
            #context = {'username': request.session['user_name']}
            # send_mail('Login','welcome'+uname,uname)
            return redirect("http://127.0.0.1:8000/user_home")
            

            



          
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'user_login.html', context)
    else:
        return render(request, 'user_login.html')
   
def edit(request,pk):
    vehicle = Vehicle.objects.get(id=pk)
    if request.method == "POST":
        vc = request.POST['vehiclecompany']
        rn = request.POST['regno']
        on = request.POST['ownername']
        oc = request.POST['ownercontact']
        if 'outtime' in request.POST:
            out = request.POST['outtime']
            vehicle.outtime = out
        vehicle.vehiclecompany = vc
        vehicle.regno = rn
        vehicle.ownername = on
        vehicle.ownercontact = oc

        vehicle.save()
        return redirect("http://127.0.0.1:8000/user_home")

    else:
        context={'vehicle':vehicle}
        return render(request,'edit_d.html',context)


def user_add_vehicle(request):
    u = request.session['user_id']
    user = User_login.objects.get(id=u)
    category1 = Category.objects.all()
    if request.method == "POST":
        pn = str(random.randint(10000000, 99999999))
        ct = request.POST['category']
        vc = request.POST['vehiclecompany']
        rn = request.POST['regno']
        on = request.POST['ownername']
        oc = request.POST['ownercontact']
        pd = request.POST['pdate']

        status = "In"
        category = Category.objects.get(categoryname=ct)

        v = Vehicle.objects.create(parkingnumber=pn, category=category, vehiclecompany=vc, regno=rn, ownername=on,
                                   ownercontact=oc, pdate=pd, parkingcharge='', remark='', status=status, user=user)
        v.save()
        return redirect("all", id=v.id)

    d = {'category1': category1}
    return render(request, 'user_add_vehicle.html', d)


def user_edit(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    if request.method == "POST":
        vc = request.POST['vehiclecompany']
        rn = request.POST['regno']
        on = request.POST['ownername']
        oc = request.POST['ownercontact']
        if 'outtime' in request.POST:
            out = request.POST['outtime']
            vehicle.outtime = out
        vehicle.vehiclecompany = vc
        vehicle.regno = rn
        vehicle.ownername = on
        vehicle.ownercontact = oc

        vehicle.save()
        return redirect("http://127.0.0.1:8000/user_home")

    else:
        context = {'vehicle': vehicle}
        return render(request, 'user_edit.html',context)
    
def all_park(request,id):
    all=Parkings.objects.all()
    context={'all':all,'id':id}
    return render(request,'allparking.html',context)

def slots(request):
    v=request.GET["v"]
    pk=request.GET["id"]
    p=Parkings.objects.get(id=pk)
    a=Slots.objects.filter(parking=p)
    context={'p':p,'all':a,'v':v}
    return render(request,'slots.html',context)
def book_slot(request):
    u = request.session['user_id']
    user = User_login.objects.get(id=u)
    pk=request.GET["id"]
    v=request.GET["v"]
    print(v)
    slot = Slots.objects.get(id=pk)
    p=slot.parking.id
    f=f"http://127.0.0.1:8000/slots?v={v}&id={p}"
    veh=Vehicle.objects.get(id=v)
   

    if slot.available:
       
        slot.available = False
        slot.save()

       
        slot.parking.remaining_slot -= 1
        slot.parking.save()
        new=Booking.objects.create(user=user,slot=slot,status="Booked",vehicle=veh,intiime=timezone.now())
        new.save()

      
       

        return redirect(f)  
    else:
        return redirect(f)

def mybook(request):
    u = request.session['user_id']
    user = User_login.objects.get(id=u)

    bookings = Booking.objects.filter(user=user)


    for book in bookings:
        start = book.intiime
        end = book.outtime
        difference = end - start
        total_hours = difference.total_seconds() / 3600
        parking_charge = total_hours * 100
        book.parkingcharge = round(parking_charge)
        book.save()
        context = {'book': bookings}
    return render(request, 'book.html', context)

def out(request,pk):
    booking = Booking.objects.get(id=pk)

    if booking.status == "Booked":
        
        booking.status = "Out"
        booking.outtime = timezone.now()
        booking.save()

        
        slot = booking.slot
        slot.available = True
        slot.save()

        
        parking = slot.parking
        parking.remaining_slot += 1
        parking.save()

    return redirect("http://127.0.0.1:8000/mybook")


def user_print(request,pid):
    u = request.session['user_id']
    user = User_login.objects.get(id=u)
    book = Booking.objects.get(id=pid)
    d = {'book': book}
    return render(request,'user_print.html', d)

    
def user_print2(request):
    u = request.session['user_id']
    user = User_login.objects.get(id=u)
    book = Booking.objects.filter(user=user)
    context = {'book': book}
    return render(request, 'user_print2.html', context)


def payment(request):

    return render(request, 'payment.html')


def add_parkings(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if request.method == "POST":
        vc = request.POST['parking_id']
        rn = request.POST['location']
        on = request.POST['street']
        oc = request.POST['park_name']
        pd = request.POST['slot']
        pr = request.POST['remaining_slot']
        pn = request.POST['price']

        v = Parkings.objects.create(parking_id=vc, location=rn, street=on, park_name=oc, slot=pd, remaining_slot=pr,
                                    price=pn)
        v.save()
        return redirect("http://127.0.0.1:8000/add_parkings")
    return render(request, 'add_parkings.html')


def add_slot(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    categories = Parkings.objects.all()

    if request.method == "POST":
        slot_no = request.POST['slot_no']
        parking_id = request.POST['category']

        parking = Parkings.objects.get(id=parking_id)
        slot = Slots.objects.create(slot_no=slot_no, parking=parking)
        slot.save()

        return redirect("http://127.0.0.1:8000/add_slot")

    context = {'categories': categories}
    return render(request, 'add_slot.html', context)


def total():
    total_charges = Booking.objects.aggregate(total=Sum('parkingcharge'))['total']
    return total_charges or 0


def total_charges(request):
    total_charges = Booking.objects.aggregate(total=Sum('parkingcharge'))['total']

    context = {
        'total_charges': total_charges
    }

    return render(request, 'admin_home.html', context)