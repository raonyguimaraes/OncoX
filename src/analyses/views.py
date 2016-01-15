from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView


from models import Analysis
from forms import AnalysisForm

from tasks import xhmm

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

            analysis = analysis.save()

            xhmm.delay(analysis.id)


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
    # print 'actions', actions
    if request.method == 'POST': 
      
        action = request.POST.get("actions_list", "")
        print 'action', action

        analyses = request.POST.getlist('analyses')


        if action == 'delete':
            for analysis_id in analyses:
                instance = Analysis.objects.get(id=analysis_id)
                instance.delete()
        elif action == 'rerun':
            print 'rerun'
            for analysis_id in analyses:
                analysis = Analysis.objects.get(id=analysis_id)
                print 'analysis', analysis.name
                print 'type', analysis.type
                xhmm.delay(analysis.id)
                            
        print 'analyses', analyses
        
    #get select objects


    return redirect('analyses')