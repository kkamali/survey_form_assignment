from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "surveyform/index.html")

def submit(request):
    if "attempts" in request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect("/result")

def result(request):
    return render(request, "surveyform/result.html")
