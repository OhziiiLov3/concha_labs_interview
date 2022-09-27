from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import AccountForm, AudioDataForm
from .serializers import UserAccountSerializer
from .models import UserAccount, AudioData
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status



#  CREATE VIEWS

def Home(request):
    accounts = UserAccount.objects.all()
    return render(request, "home.html", {'accounts': accounts})


def search_accounts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        accounts = UserAccount.objects.filter(name__contains=searched)
        return render(request, 'search_accounts.html',{'searched':searched,'accounts':accounts})
    else:
        return render(request, 'search_accounts.html', {})

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
    form = AccountForm(request.POST or None, instance=account)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'account': account, 'form':form})



def destroy(request, id):
    account = UserAccount.objects.get(id=id)
    account.delete()
    return redirect("/show")

# AUDIO DATA CRUD 


def audio(request):
    if request.method == "POST":
        form = AudioDataForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/audio')
            except:
                pass
    else:
        form = AudioDataForm()
    return render(request, 'audio-index.html', {'form': form})


def audio_show(request):
    audio = AudioData.objects.all()
    return render(request, "audio-show.html", {'audio': audio})


def editaudio(request, id):
    audio = AudioData.objects.get(id=id)
    return render(request, 'audio-edit.html', {'audio': audio})


def updateaudio(request, id):
    audio = AudioData.objects.get(id=id)
    form = AudioDataForm(request.POST or None, instance=audio)
    if form.is_valid():
        form.save()
        return redirect('/show/audio')
    return render(request, 'audio-edit.html', {'audio': audio, 'form': form})


def destroyaudio(request, id):
    audio = AudioData.objects.get(id=id)
    audio.delete()
    return redirect('/show/audio')





# UNIT TEST

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


    
