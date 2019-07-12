from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import EmployeeExcelUpload
from .models import Employee

# Create your views here.


@login_required(login_url='/admin/login')
def index(request):
    if request.method == 'POST':
        form = EmployeeExcelUpload(request.POST, request.FILES)

        def is_admin_func(row):
            row[3] = True if row[3] == 'Yes' else False
            return row

        if form.is_valid():
            request.FILES['file'].save_to_database(
                name_columns_by_row=2,
                model=Employee,
                initializer=is_admin_func,
                mapdict=['first_name', 'last_name', 'roll_number', 'is_admin']
            )
    else:
        form = EmployeeExcelUpload()

    return render(request, "upload.html", context={'form': form})
