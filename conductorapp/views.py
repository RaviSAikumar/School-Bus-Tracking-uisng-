from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from adminapp.models import *
from conductorapp.models import *
from django.contrib import messages
# import decode
# from PIL import ImageMode
import PIL
from PIL import Image, ImageDraw
from pyzbar.pyzbar import decode

def conductor_index(request):
    return render(request,'conductor/conductor-index.html')

def conductor_home_school(request):
    # children=ChildModels.objects.get()
    if request.method=='POST' and request.FILES['image']:
        qr=request.FILES['image']
        print(qr,'hhhh')
        obj = QRModels.objects.create(qrcode=qr)
        print(obj.qrcode)
        file = 'media/'+str(obj.qrcode)
        d = decode(Image.open(file))
        print(d[0].data)
        data = d[0].data
        children_id = data.decode()

        print(type(children_id))
        print(children_id)
        # Get card details using card number
        try:
            card =get_object_or_404(ChildModels,pk=children_id)
            card.children_status2='Home'
            card.save(update_fields=["children_status2"])
            card.save()
            if card.children_status1 =='Boarded':
                
                card.children_status1='Dropped'
                card.save(update_fields=["children_status1"])
                card.save()
                return redirect('conductor_drop_status')
            else:

                card.children_status1='Boarded'
                card.save(update_fields=["children_status1"])
                card.save()
                print(card,'lll')
                print(card.children_status1)
                messages.success(request, 'Boarded Successfully')
                return redirect('conductor_boarding_status')

        except:
            messages.error(request,'This Code is not Approved')


            

        # Delete all temp data
        os.remove(file)
        obj.delete()
        return redirect('conductor_home_school')
    
        
    return render(request,'conductor/conductor-home-school.html')


# def conductor_hometoschool(request):
#     return render(request,'conductor/conductor-hometoschool.html')

def conductor_school_home(request):
    if request.method=='POST' and request.FILES['image']:
        qr=request.FILES['image']
    
        obj = QRModels.objects.create(qrcode=qr)
        print(obj.qrcode)

        file = 'media/'+str(obj.qrcode)
        d = decode(Image.open(file))
        print(d[0].data)
        data = d[0].data
        children_id = data.decode()

        
        print(type(children_id))
        print(children_id)
        # Get card details using card number
        try:
            card =get_object_or_404(ChildModels,pk=children_id)
            card.children_status2='School'
            card.save(update_fields=["children_status2"])
            card.save()
            if card.children_status1 =='Boarded':
                card.children_status1='Dropped'
                card.save(update_fields=["children_status1"])
                card.save()
                return redirect('conductor_drop_status')
           
            else:

                card.children_status1='Boarded'
                card.save(update_fields=["children_status1"])
                card.save()
                print(card,'lll')
                print(card.children_status1)
                messages.success(request, 'Boarded Successfully')
                return redirect('conductor_boarding_status')

        except:
            messages.error(request,'This Code is not Approved')
           

        # Delete all temp data
        os.remove(file)
        obj.delete()
        return redirect('conductor_school_home')
    
        
       
    return render(request,'conductor/conductor-school-home.html')

def conductor_bus_delay(request):
    return render(request,'conductor/conductor-bus-delay-update.html')

def conductor_boarding_status(request):
   
        card = ChildModels.objects.filter(children_status1='Boarded')
    
        return render(request,'conductor/conductor-boarding-status.html',{
            'card':card})

    # return render(request,'conductor/conductor-boarding-status.html')
def conductor_drop_status(request,):
       card = ChildModels.objects.filter(children_status1='Dropped')

       return render(request,'conductor/conductor-drop-status.html',{
            'card':card})

    
    
    #  return render(request,'conductor/conductor-drop-status.html')