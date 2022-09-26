from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import AccountForm
from .serializers import UserAccountSerializer
from .models import UserAccount
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status



#  CREATE VIEWS

def useraccount(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = AccountForm()
    return render(request,'index.html',{'form': form})

def show(request):
    accounts = UserAccount.objects.all()
    return render(request, "show.html", {'accounts': accounts})


def edit(request, id):
    account = UserAccount.objects.get(id=id)
    return render(request, 'edit.html', {'account': account})


def update(request, id):
    account = UserAccount.objects.get(id=id)
    form = AccountForm(request.POST, instance=account)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'account': account})



def destroy(request, id):
    account = UserAccount.objects.get(id=id)
    account.delete()
    return redirect("/show")











# GET -> DATA FROM -> Return in JSON 
# CREATE AND READ DATA
@api_view(['GET','POST'])
def useraccount_list(request):

    if request.method == 'GET':
        accounts = UserAccount.objects.all()
        serializer = UserAccountSerializer(accounts, many =True)
        return JsonResponse({"user_accounts": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def useraccount_detail(request, id):
    # checks valid request 
    try:
        accounts = UserAccount.objects.get(pk=id)
    except UserAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserAccountSerializer(accounts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserAccountSerializer(accounts, data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        accounts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CREATE

# UPDATE 

# DELETE 


    
