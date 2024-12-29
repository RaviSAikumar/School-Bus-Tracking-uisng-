from django.shortcuts import render,redirect
from userapp.models import *
from adminapp.models import *
from textblob import TextBlob
from django.contrib import messages



# Create your views here.

def user_index(request):
    return render(request,'user/user-index.html')


def user_about(request):    
    return render(request,'user/user-about.html')

def user_feedback(request):
    user_id = request.session['c_id']
    user = ChildModels.objects.get(c_id=user_id)
   
   
    # user=ChildModels.objects.get(user_id=c_id)
    # c_id=request.session['c_id']
    if request.method == "POST":
        rating=request.POST.get("rating")
        text=request.POST.get("text")
        
        analysis = TextBlob(text)

        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity > -0.5:
            sentiment = 'Negative'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negative'
        else:
            sentiment = 'Neutral'

        print(sentiment)
        user_feedback = UserFeedbackModel.objects.create(rating=rating,text=text,userfeedback=user,sentiment=sentiment)
        user_feedback.save()


        messages.success(request,"Successfully Sent")   
    return render(request,'user/user-feedback.html')


def user_myprofile(request):
   
    user_id = request.session['c_id']
    user = ChildModels.objects.get(c_id=user_id)
   
    print(user)
    

    if request.method =="POST"and request.FILES['image']:
        name=request.POST.get('name')
        childclass=request.POST.get('class')
        mothername=request.POST.get('mothername')
        fathername=request.POST.get('fathername')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        address=request.POST.get('address')
        childid=request.POST.get('childid')
        password=request.POST.get('password')
        image=request.FILES['image']
        print(image)
       
      
        if len(request.FILES)!=0:
            image=request.FILES['image']
            user.children_rollnum=childid
            user.children_name=name
            user.children_email=email
            user.children_password=password
            user.children_mothername=mothername
            user.children_fathername=fathername
            user.children_contact=contact
            user.children_class=childclass
            user.children_image=image
            user.children_address=address
            user.save()
        
        else:
            user.children_name=name
            user.children_rollnum=childid
            user.children_email=email
            user.children_password=password
            user.children_mothername=mothername
            user.children_fathername=fathername
            user.children_contact=contact
            user.children_class=childclass
            user.children_image=image
            user.children_address=address
            user.save()
    print(user.children_image,'ggg')
    return render(request,'user/user-myprofile.html',{'user':user})


def user_view_status(request):
    return render(request,'user/user-view-status.html')


def user_changepassword(request):
    
    user_id = request.session['c_id']
    user = ChildModels.objects.get(c_id=user_id)
    if request.method=="POST":
        oldpassword=request.POST.get('oldpassword')
        newpassword=request.POST.get('newpassword')
        confirmpassword=request.POST.get('confirmpassword')
        print(oldpassword,newpassword,confirmpassword)

        print(user)
        user.children_password=newpassword
        user.save()



    return render(request,'user/user-changepassword.html')

def boarding_status(request):
    user_id = request.session['c_id']
    card = ChildModels.objects.filter(children_status1='Boarded').filter(c_id=user_id)
    
    return render(request,'user/user-boarding-status.html',{
            'card':card})


    return render(request,'user/user-boarding-status.html')


def dropping_status(request):
       user_id = request.session['c_id']
       card = ChildModels.objects.filter(children_status1='Dropped').filter(c_id=user_id)

       return render(request,'user/user-dropping-status.html',{
            'card':card})

    # return render(request,'user/user-dropping-status.html')



def notification_status(request):
    data=DelayModel.objects.all().order_by('-pk')[0:1]
    print(data)

    return render(request,'user/user-notification.html',{'data':data})