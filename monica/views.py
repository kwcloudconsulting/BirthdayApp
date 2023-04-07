from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BirthdayMessage
from django.views import View
from .forms import BirthdayMessageForm

@login_required
def home(request):
    messages = BirthdayMessage.objects.all()
    form = BirthdayMessageForm()
    if request.method == 'POST':
        form = BirthdayMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('home')
    context = {'messages': messages, 'form': form}
    return render(request, 'index.html', context)
