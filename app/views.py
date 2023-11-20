from django.shortcuts import render

# Create your views here.
def data(request):
    da='hello welcome to jinja printing tags/expression tags/templates tags'
    d={'jinja':da}
    return render(request,'data.html',context=d)