from django.shortcuts import render

# Create your views here.
def main_page_view(request):
    return render(request, "index.html", context={})
