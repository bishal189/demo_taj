from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import FileResponse
from tab.froms import DocumentsForms
import random
from .models import Document
import string
# Create your views here.


def home(request,length=10):
    if request.method == 'POST':
        characters = string.ascii_letters + string.digits + string.punctuation
        random_string = ''.join(random.choice(characters) for _ in range(length))
        forms=DocumentsForms(request.POST,request.FILES)
        if forms.is_valid():
            new=forms.save(commit=False)
            new.documnet_number=str(random_string)
            new.save()
            context={
                'code':random_string
            }
            return render(request,'code.html',context)
    
    forms=DocumentsForms()
    context={
        'forms':forms,
    }
    return render(request,'home.html',context)



# def upload(request):
#     if request.method == 'POST':
#         forms=DocumentsForms(request.POST)
#         if forms.is_valid():
#             forms.save()
#             return redirect('home')


def search(request):
    if request.method == 'POST':
         get_key=request.POST.get('code')
         print(get_key)
         get_obj=Document.objects.get(documnet_number=get_key)
         context={
            'get_obj':get_obj
         }
         return render(request,'download.html',context)
    
    else:
        return HttpResponse('cant used this page directly restricted to the user please go back.')



def download_file(request, file_id):
    file_instance = get_object_or_404(Document, id=file_id)
    file_path = file_instance.document.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)
