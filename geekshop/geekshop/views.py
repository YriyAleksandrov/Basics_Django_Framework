from django.shortcuts import render

content = {}


def main(request):
    return render(request, 'index.html', content)


def contacts(request):
    return render(request, 'contact.html', content)
