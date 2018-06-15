from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseNotFound

from forms import ExecuteSumForm
from tasks import add

class ExecuteSumView(FormView):
    template_name = 'sample_form.html'
    form_class = ExecuteSumForm

    def form_valid(self, form):
        x = form.cleaned_data.get('x')
        y = form.cleaned_data.get('y')
        total = add.delay(x, y)
        messages.success(self.request, 'Calculating the result...')        
        return HttpResponse('your result is {}'.format(total.get(timeout=2)))
