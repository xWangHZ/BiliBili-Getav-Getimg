from django.shortcuts import render

from .Rep import reptile as rep

# Create your views here.

def get_html(request):
    if request.method == 'POST':
        name = request.POST.get('text')

        av, img = rep.get_html(name)
        return render(request, template_name='index.html', context={
            'av': av,'img': img
        })



    return render(request, 'index.html')