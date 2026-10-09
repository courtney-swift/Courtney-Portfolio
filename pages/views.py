from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def about_me_view(request):
  return render(request, 'pages/about_me.html')

def contact_view(request):
  # POST: the vistor submitted the form
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      email = form.cleaned_data['email']
      message = form.cleaned_data['message']


      message_body=(
        f"New message from my portfolio\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Message: {message}"
      )
      try:
        send_mail(
          "Message from your Portfolio",
          message_body, # Email body
          email,
          ['courtneydezman@gmail.com']
        )
        # Success: Reset the form and show a confirmation message
        form, = ContactForm()
        return render(request, 'pages/contact.html', {"form": form})
      except Exception as e:
        return render(request, 'pages/contact.html', {"form": form})
    else:
      return render(request, 'pages/contact.html', {"form": form})

  else:
    form = ContactForm()
    return render(request, 'pages/contact.html', {"form": form})

def experience_view(request):
  return render(request, 'pages/experience.html')
  