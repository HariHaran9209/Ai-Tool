from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.exceptions import ValidationError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def og(request):
    data = Section1.objects.all()
    activity = Section2.objects.all()
    title_data = Titles.objects.all()
    return render(request, 'og.html', {"data": data, "activity": activity, "title_data": title_data})

def add_title(request):
    if request.method == 'POST':
        title1_name = request.POST.get('title1_name')
        title2_name = request.POST.get('title2_name')
        if title1_name and title2_name:
            try: 
                Titles.objects.create(title1=title1_name, title2=title2_name)
                return redirect('add_section')
            except ValidationError:
                return HttpResponse("sorry")
    return render(request, 'add_title.html')

def add_heading(request):
    if request.method == 'POST':
        data_heading1 = request.POST.get('heading1')
        data_subheading1 = request.POST.get('subheading1')
        data_heading2 = request.POST.get('heading2')
        data_subheading2 = request.POST.get('subheading2')
        data_heading3 = request.POST.get('heading3')
        data_subheading3 = request.POST.get('subheading3')
        if data_heading1 and data_heading2 and data_subheading1 and data_subheading2 and data_subheading3 and data_heading3:
            try:
                Section1.objects.create(t1h1=data_heading1, t1sh1=data_subheading1, t1h2=data_heading2, t1sh2=data_subheading2, t1h3=data_heading3, t1sh3=data_subheading3)
                return redirect('add_activity')
            except ValidationError:
                return HttpResponse("Sorry")
    return render(request, 'add_section.html')


def add_activity(request):
    if request.method == 'POST':
        activity_count = int(request.POST.get('activity_count', 0))
        for i in range(1, activity_count + 1):
            name = request.POST.get(f'name_{i}')
            email = request.POST.get(f'email_{i}')
            joined = request.POST.get(f'joined_{i}')
            type = request.POST.get(f'type_{i}')
            status = request.POST.get(f'status_{i}')
            
            if name and email and joined and type and status:
                try:
                    Section2.objects.create(
                        a1=name,
                        a2=email,
                        a3=joined,
                        a4=type,
                        a5=status
                    )
                except ValueError:
                    pass
        
        # Redirect or render a success page
        return redirect('og')  # Replace with your success page URL
    return render(request, 'add_activity.html')