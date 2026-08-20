from django.shortcuts import render
from .models import Case


def case_list(request):
    cases = Case.objects.filter(is_active=True)
    return render(request, 'cases/case_list.html', {'cases': cases})