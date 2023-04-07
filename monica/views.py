from django.shortcuts import render, redirect
from .models import BirthdayMessage
from django.views import View
from .forms import BirthdayMessageForm

def index(request):
    if request.method == 'POST':
        form = BirthdayMessageForm(request.POST)
        if form.is_valid():
            birthday_message = form.save(commit=False)
            birthday_message.user = request.user
            birthday_message.save()
            return redirect('index')
    else:
        form = BirthdayMessageForm()
    
    context = {'form': form}
    return render(request, "index.html", context)

class BirthdayMessageView(View):
    def get(self, request):
        messages = BirthdayMessage.objects.all().order_by('-date_created')
        context = {'messages': messages}
        return render(request, 'birthday_messages.html', context)
