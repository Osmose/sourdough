from django.shortcuts import render


def index(request):
    return render(request, 'base/index.html', {'foo': request.POST.get('bar', 'baz')})
