from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        ctxt = {'user': request.user}#, 'auth': request.auth}
        return render(request, self.template_name, ctxt)


