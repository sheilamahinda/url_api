# views.py

from django.shortcuts import render, redirect
from .models import SetUrlData
from .forms import SetURLDataForm

def set_url_data_view(request):
    set_url_data = SetUrlData.objects.first()
    form = SetURLDataForm(request.POST or None, instance=set_url_data)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('set_url_data')

    return render(request, 'url_data.html', {'form': form})
from django.shortcuts import render

# Create your views here.
