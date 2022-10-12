from django.shortcuts import render, redirect
from .models import AddCompanyModel

from .forms import AddCompanyForm

# Create your views here.
def company_list(request):
    companies = AddCompanyModel.objects.all()
    return render (request, 'companies/company_list.html',{'companies':companies})


def add_company(request):
    if request.method == 'POST':
        company_form = AddCompanyForm(request.POST)
        if company_form.is_valid():
            company_form.save()
            return redirect('company_list')
    
    else:
        company_form = AddCompanyForm()
    return render(request, 'companies/company-add_edit.html',{'company_form':company_form})

