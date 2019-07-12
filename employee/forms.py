from django import forms


class EmployeeExcelUpload(forms.Form):
    file = forms.FileField()
