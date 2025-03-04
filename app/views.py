# -*- coding: utf-8 -*-



from django.contrib.auth.decorators import login_required
from .models import Model3D
from django.db import models
from datetime import datetime
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Model3DForm
from django.db.models import Q
from .models import Case
from django.core.paginator import Paginator
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json







@csrf_exempt
def create_case(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Extract required fields
            patient_name = data.get("patient_name")
            patient_code = data.get("patient_code")
            dentist_name = data.get("dentist_name")
            dentistry_type = data.get("dentistry_type")
            tooth_numbers = data.get("tooth_numbers", [])  # Accepts list of teeth
            shade_system = data.get("shade_system")
            shade = data.get("shade")
            notes = data.get("notes", "")

            # Validation
            if not all([patient_name, patient_code, dentist_name, dentistry_type, shade_system, shade]):
                return JsonResponse({"success": False, "message": "Missing required fields"}, status=400)

            # Ensure `tooth_numbers` is a list
            if not isinstance(tooth_numbers, list) or not all(isinstance(num, str) for num in tooth_numbers):
                return JsonResponse({"success": False, "message": "Tooth numbers must be a list of strings"}, status=400)

            # Create the case
            case = Case.objects.create(
                patient_name=patient_name,
                patient_code=patient_code,
                dentist_name=dentist_name,
                dentistry_type=dentistry_type,
                tooth_numbers=tooth_numbers,
                shade_system=shade_system,
                shade=shade,
                notes=notes,
            )

            return JsonResponse({
                "success": True,
                "message": "Case created successfully!",
                "case_id": case.case_number  # Returns the generated case number
            })

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON format"}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)










@csrf_exempt
def send_to_outsource(request, case_id):
    if request.method == "POST":
        # Logic to send the case to Outsource
        # Example: Update the case status in the database
        # case = Case.objects.get(id=case_id)
        # case.status = "Outsourced"
        # case.save()
        return JsonResponse({"success": True, "message": "Case sent to Outsource successfully!"})
    return JsonResponse({"success": False, "message": "Invalid request method"}, status=405)



#@login_required
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )

@login_required
def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )

@login_required
def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )

@login_required
def upload_model(request):
    if request.method == 'POST':
        form = Model3DForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_list')
    else:
        form = Model3DForm()
    return render(request, 'upload_model.html', {'form': form})

#@login_required
def model_list(request):
    models = Model3D.objects.all()
    return render(request, 'model_list.html', {'models': models})

#@login_required
def view_model(request, model_id):
    model = get_object_or_404(Model3D, id=model_id)
    return render(request, 'model_detail.html', {'model': model})

#@login_required
def cases(request):
    return render(request, 'app/cases.html', {'title': 'Cases'})

#def create_case(request):
    #return render(request, 'app/create_case.html', {'title': 'Create New Case'}) No need for this one, we are api apporach

def dashboard(request):
    return render(request, 'app/dashboard.html', {'title': 'Dashboard'})

def calls(request):
    return render(request, 'app/calls.html', {'title': 'Calls'})

def accounting(request):
    return render(request, 'app/accounting.html', {'title': 'Accounting'})




# Sales View
#@login_required
def sales(request):
    context = {
        'title': 'Sales',
        'this_month': '$0.00',
        'this_year': '$0.00',
        'lifetime': '$0.00',
    }
    return render(request, 'app/sales.html', context)

def designer_dashboard(request):
    return render(request, 'app/designer_dashboard.html')

#@login_required
def lab_product(request):
    tabs = [
        {'id': 'materials', 'label': 'Materials'},
        {'id': 'orders', 'label': 'Orders'},
        {'id': 'inventory', 'label': 'Inventory'},
        {'id': 'analytics', 'label': 'Analytics'}
    ]
    return render(request, 'app/lab_product.html', {'title': 'Lab Product', 'tabs': tabs})

def outsource(request):
    return render(request, 'app/outsource.html', {'title': 'Outsource'})

def settings(request):
    return render(request, 'app/settings.html', {'title': 'Settings'})

def accounts(request):
    return render(request, "app/accounts.html", {"title": "Accounts"})

def search_cases(request):
    # Get the search query from the GET request
    query = request.GET.get('query', '')
    
    # Filter the cases based on the search query
    results = Case.objects.filter(
        Q(case_id__icontains=query) |
        Q(patient_name__icontains=query) |
        Q(doctor_name__icontains=query) |
        Q(account_number__icontains=query)
    )
    
    # Implement pagination (10 results per page)
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')  # Get the current page number from the query params
    page_results = paginator.get_page(page_number)  # Get the paginated results for the current page
    
    # Render the results in the search_results.html template
    return render(request, 'cases/search_results.html', {'results': page_results, 'query': query})


