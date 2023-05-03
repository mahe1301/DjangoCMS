from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..decorator import user_is_admin
from restapiservice.models import UserInfo, UserContact

def my_login(request):
    return render(request, template_name='back/login.html')


def login_check(request):

    if request.method == 'POST':
        txtuname = request.POST['login-email']
        txtpwd = request.POST['login-password']
        print(txtuname,txtpwd)
        if txtuname != "" and txtpwd != "":
            userinfo = authenticate(username=txtuname,password=txtpwd)
            # print(userinfo)
            if userinfo!=None:
                login(request,userinfo)
                return redirect('Home')
                # return HttpResponseRedirect('home')
    return redirect('Login')


def my_logout(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='/b2n/')
@user_is_admin
def user_list(request):
    user_obj=UserInfo.objects.all()
    usesr_data = []
    for user1 in user_obj:
        user_contact_obj = UserContact.objects.filter(user_id=user1.id)
        # print(user_contact_obj)
        # user_contact_obj = UserContact.objects.all()
        # print(user_contact_obj)
        usesr_data.append({
        'first_name' : user1.first_name, 
        'last_name': user1.last_name, 
        'email' : user1.email,
        'date_of_birth': user1.date_of_birth, 
        'phone' : user1.phone,
        'created' : user1.created,
        'isActive' : user1.isActive,
        'address1':user_contact_obj[0].address1 if len(user_contact_obj) != 0 else "",
        'address2':user_contact_obj[0].address2 if len(user_contact_obj) != 0 else "",
        'postalcode':user_contact_obj[0].postalcode if len(user_contact_obj) != 0 else "",
        'city':user_contact_obj[0].city if len(user_contact_obj) != 0 else ""
        })
    return  render(request, template_name='back/users/users_list.html',context={'users':usesr_data})