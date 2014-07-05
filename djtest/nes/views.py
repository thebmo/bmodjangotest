from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail #for contact form email submission
from nes.models import Users, Games, TestEntries
from nes.forms import ContactForm, RandomGameForm #import forms here

# Create your views here.
def text_test(request):
    return render(request, 'text.html',)

def e404(request):
    u = request.path
    return render(request, 'test.html', {'url' : u})

def home(request):
    entries = Users.objects.all()
    return render(request, 'test.html', {'users' : entries})

# def game(request):
    # entries = Games.objects.all()
    # return render(request, 'games.html', {'games' : entries})   

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Hey dummy, you left this blank!')
        elif len(q) > 20:
            errors.append('Please limit search to less than 20 characterss')
            
        else:
            games = Games.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'games' : games, 'query' : q})
    
    all_titles = Games.objects.all()
    return render(request, 'search_form.html', {'errors' : errors, 'titles': all_titles} )
    
# random game form view
def random_game(request):
    form = RandomGameForm()
    return render(request, 'random_game.html', {'form' : form})

# new contact view        
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['bmosier@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'your forms are tops'}
        )
    return render(request, 'contact_form.html', {'form' : form})