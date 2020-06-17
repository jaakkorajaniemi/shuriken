from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm

# Create your views here.
def index(request):
   context = {
      'debug_state': str(settings.DEBUG)
   }
   return render(request, 'core/index.html', context)

def contact(request):
   if request.method == 'GET':
        form = ContactForm()

   else:
      form = ContactForm(request.POST)

      if form.is_valid():
         subject = form.cleaned_data['subject']
         message = form.cleaned_data['message']

         try:
               send_mail(subject, message, 'info@rajaniemi.fi', ['jaakko@rajaniemi.fi'])
         except BadHeaderError:
               return HttpResponse('Invalid header found.')
         return redirect('success')

   return render(request, "core/contact.html", {'form': form})

def success(request):
   return render(request, 'core/index.html')