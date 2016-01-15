from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView


from models import Analysis
from forms import AnalysisForm

# Create your views here.
def index(request):

    analyses = Analysis.objects.all()

    print 'get analysis'
    for analysis in analyses:
        print analysis.name

    return render(request, 'analyses/index.html', {'analyses':analyses})

def create(request):

    if request.method == 'POST': # If the form has been submitted...
        form = AnalysisForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            
            # analysis = form.save(commit=False)
            analysis = AnalysisForm(request.POST)

    
            #schedule task
                        

            # print 'request.user', request.user

            # analysis.user = request.user

            analysis.save()

            return redirect('analyses')

    else:
        form = AnalysisForm()

    return render(request, 'analyses/create.html', {'form':form})


class AnalysisCreate(CreateView):
    model = Analysis
    # model = Author
    form_class = AnalysisForm
    # fields = ['name', 'files', 'type']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(AnalysisCreate, self).form_valid(form)


def bulk_actions(request):

    print 'entrou no bulk'
    if request.method == 'POST': 
      
        analyses = request.POST.getlist('analyses')

        print 'analyses', analyses
        for analysis_id in analyses:
            instance = Analysis.objects.get(id=analysis_id)
            instance.delete()

    #get select objects


    return redirect('analyses')