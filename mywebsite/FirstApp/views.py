from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import render_to_string

# Create your views here.
di = {'name': ['Prateek', 'Naresh', 'Nipun', 'Arnab'],
      'url': ['/name/prateek', '/name/naresh', '/name/nipun', '/name/arnab'],
      'age': [26, 27, 27, 28], 'li': [1, 2, 3, 7]}
details = list(zip(di['name'], di['url']))


def Home(request):
    return render(request, "index.html", {'details': details})


def Prateek(request):
    di = {'name': ['Naresh', 'Nipun', 'Arnab'],
          'url': ['/name/naresh', '/name/nipun', '/name/arnab'],
          }
    details = list(zip(di['name'], di['url']))
    return render(request, "names/prateek.html", {'details': details})


def Naresh(request):
    di = {'name': ['Prateek', 'Nipun', 'Arnab'],
          'url': ['/name/prateek', '/name/nipun', '/name/arnab'],
          }
    details = list(zip(di['name'], di['url']))
    return render(request, "names/naresh.html", {'details': details})


def Nipun(request):
    di = {'name': ['Prateek', 'Naresh', 'Arnab'],
          'url': ['/name/prateek', '/name/naresh', '/name/arnab'],
          }
    details = list(zip(di['name'], di['url']))

    return render(request, "names/nipun.html", {'details': details})


def Arnab(request):
    di = {'name': ['Prateek', 'Naresh', 'Nipun'],
          'url': ['/name/prateek', '/name/naresh', '/name/nipun'],
          }
    details = list(zip(di['name'], di['url']))

    return render(request, "names/arnab.html", {'details': details})


def Contactus(request):
    return render(request, "names/contactus.html", {'details': details})
