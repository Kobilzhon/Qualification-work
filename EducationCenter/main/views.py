from django.shortcuts import render, redirect
from main.models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    news_ob = News.objects.all()
    events = MasterClass.objects.all()
    courses_category = CourseCategory.objects.all()
    courses = Courses.objects.all()

    if request.method == 'POST':
        message = request.POST['message']
        phone = request.POST['phone']
        tel_data = Zayavka.objects.create(
            user=request.user,
            message=message,
            phone_num=phone,
        )
        courses = ''
        tel_data.save()
        return redirect('main-susses-message')
    context = {
        'news': news_ob,
        'events': events,
        'courses_category': courses_category,
        'courses': courses,
    }
    return render(request, 'index.html', context)


@login_required
def post(request):
    posts = Blog.objects.all()
    comments = Comment.objects.all()
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid() and request.POST.get("content") != "":
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.id_blog = int(request.POST.get("id_block"))
            instance.save()
            return redirect('main-posts')

    else:
        c_form = CommentForm()
    context = {
        'posts': posts,
        'c_form': c_form,
        'comments': comments
    }
    return render(request, 'blog.html', context)


@login_required
def news_detail(request, pk):
    news_by_id = News.objects.get(id=pk)
    send_news_comment = request.POST.get("comment")
    if request.method == "POST" and send_news_comment != "":
        tel_data = NewsComment.objects.create(content=send_news_comment, news=news_by_id, user=request.user)
        tel_data.save()
        return redirect('main-news-detail', pk=news_by_id.id)
    context = {
        'news': news_by_id
    }
    return render(request, 'news_detail.html', context)


@login_required()
def contact(request):
    return render(request, 'contact.html')


@login_required()
def admission(request):
    if request.method == 'POST':
        message = request.POST['message']
        phone = request.POST['phone']
        tel_data = Zayavka.objects.create(
            user=request.user,
            message=message,
            phone_num=phone,
        )
        tel_data.save()
        return redirect('main-susses-message')
    return render(request, 'Admissions.html')


@login_required()
def admission_susses(request):
    return render(request, 'susses_seng_page.html')


@login_required()
def get_courses_by_id(request, id):
    news_ob = News.objects.all()
    events = MasterClass.objects.all()
    courses_category = CourseCategory.objects.all()
    courses = Courses.objects.filter(category=id)
    context = {
        'news': news_ob,
        'events': events,
        'courses_category': courses_category,
        'courses': courses,
    }
    return render(request, 'index.html', context)


@login_required()
def event_details(request, id):
    context = {
        "events_detail": MasterClass.objects.filter(id=id)
    }
    return render(request, 'event_details.html', context)


@login_required()
def allcourses(request):
    courses_category = CourseCategory.objects.all()
    courses = Courses.objects.all()
    listCategory = []
    for i in courses_category:
        listCategory.append(i.id)
    print(listCategory)
    print(courses)
    context = {
        'courses_category': courses_category,
        'courses': courses,
        'listCategory': listCategory,
        'active': listCategory[0]
    }

    return render(request, 'Courses.html', context)


@login_required()
def get_events(request):
    context = {
        'events': MasterClass.objects.all()
    }
    return render(request, 'Event.html', context)


@login_required()
def error_404(request, exception):
    return render(request, 'errors/404.html')
