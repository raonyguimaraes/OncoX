from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


import json
import os
from forms import FileForm
from models import File

def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"


class JSONResponse(HttpResponse):
    """JSON response class."""
    def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
        content = json.dumps(obj,**json_opts)
        super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)


@login_required
def create(request):
    # return render(request, 'files/create.html', {"foo": "bar"})
    print 'entrou no create'

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        print 'request is post!'
        print form.errors
        if form.is_valid():
            print 'form is valid!'
            # print 'analysis name should be ', form.cleaned_data['name']

            # file.name = form.cleaned_data['name']

            file = File.objects.create(user=request.user)

            file.file= request.FILES.get('file')
            file.name= str(os.path.splitext(file.file.name)[0])
            file.user = request.user
            file.save()
            
            
            f = file.file
            #fix permissions
            #os.chmod("%s/genomes/%s/" % (settings.BASE_DIR, fastafile.user), 0777)
            
            # os.chmod("%s/uploads/%s/%s" % (settings.BASE_DIR, fastafile.user, fastafile.id), 0777)

            #Align.delay(analysis.id)

            data = {'files': [{'deleteType': 'DELETE', 'name': file.name, 'url': '', 'thumbnailUrl': '', 'type': 'image/png', 'deleteUrl': '', 'size': f.size}]}
            response = JSONResponse(data, mimetype=response_mimetype(request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
    else:
        
        form = FileForm()

    return render(request, 'files/create.html', {'form':form})



def list(request):
    files = File.objects.all()
    return render(request, 'files/index.html', {"files": files})