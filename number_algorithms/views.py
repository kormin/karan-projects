from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def find_pi(request, pi=0):
    return render(request, 'numbers/find_pi.html', {'pi': pi})

def pi_to_n(request):
    request.POST['digit']
    pi = math.pi
    url = reverse('numbers:find_pi', kwargs={'pi': pi})
    return HttpResponseRedirect(url)
