from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from blog.models import Post
from .models import Letter
from .forms import LetterForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.core import mail
from django.core.mail import EmailMessage


def index (request):
    all_posts = Post.objects.all().order_by("-published_date")

    post_1= all_posts[0:1]
    post_2 = all_posts[1:2]
    post_3 = all_posts[2:3]
    print(post_1)
    print(post_2)
    print(post_3)
    context = {"post_1": post_1, "post_2" : post_2, "post_3":post_3}
    return render(request, "krasotka/index.html", context)

@login_required
def letter (request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print( name, email,  subject , message)

        try:
            send_mail(subject, message, "krasotka.dnepr@gmail.com", ["dnepr.reklama@mail.ru"] )
        except BadHeaderError:  # Защита от уязвимости
            return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
    return render(request, 'krasotka/thanks.html')

@login_required
def thanks(reguest):
    thanks = 'thanks'
    return render(reguest, 'krasotka/thanks.html', {'thanks': thanks})


def send (request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        l = LetterForm()
        l.published_date=now()
        data={"name":name, "email": email, "subject": subject  , "message": message, "published_date":l.published_date}

        form=LetterForm(data)

        if form.is_valid():
            form.save()
            print( form)
            return  redirect("thanks")
        return redirect("index")

























