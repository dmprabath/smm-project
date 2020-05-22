from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from packages.models import Packages
from quotations.models import Quotation

# Create your views here.


def quotations(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['email'] and request.POST['address'] and request.POST['remarks']:

            if request.POST['select-package']:
                quotation = Quotation()
                quotation.name = request.POST['name']
                quotation.email = request.POST['email']
                quotation.address = request.POST['address']
                quotation.remarks = request.POST['remarks']
                quotation.date = timezone.datetime.now()
                selected_item = get_object_or_404(
                    Packages, pk=request.POST['select-package'])
                quotation.packNo = selected_item
                quotation.save()

                packages = Packages.objects
                return render(request, 'quotations.html', {'success': 'Quotations has been sent Successfully', 'packages': packages})
            else:
                packages = Packages.objects
                return render(request, 'quotations.html', {'error': 'Please select a Package', 'packages': packages})
        else:
            packages = Packages.objects
            return render(request, 'quotations.html', {'error': 'All fields are required', 'packages': packages})

    packages = Packages.objects
    return render(request, 'quotations.html', {'packages': packages})
