from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.db.models import Count

def get_categories():
    all_categories = Category.objects.all()
    count = all_categories.count() # 7
    half = count // 2 + count % 2
    first_half = all_categories[:half]
    second_half = all_categories[half:]
    return {"cat1": first_half, "cat2": second_half}


def index(request, id=None):
    comments = Comment.objects.filter(post_id=id).order_by("-published_date")
    all_categories = Category.objects.all()
    post_in_category = Post.objects.filter(category_id=Count('category_id')).count



    all_posts = Post.objects.all().order_by("-published_date")

    paginator = Paginator(all_posts.order_by("-published_date"), 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        p_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p_list = paginator.page(paginator.num_pages)

    context = {"p_list": p_list, "post_in_category":post_in_category, "all_categories":all_categories}
    context.update(get_categories())
    return render(request, "blog/blog.html", context)


def categories (request, id=None):
    comments = Comment.objects.filter(post_id=id).order_by("-published_date")
    all_categories = Category.objects.all()
    c_count = comments.count()
    print(c_count)
    all_posts = Post.objects.filter(category__pk=id).order_by("-published_date")

    paginator = Paginator(all_posts.order_by("-published_date"), 3)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        p_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        p_list = paginator.page(paginator.num_pages)

    context = {"p_list": p_list,  "all_categories": all_categories}
    context.update(get_categories())
    return render(request, "blog/blog_categories.html", context)




def post(request, id=None):
    p = get_object_or_404(Post, pk=id)  # Post.objects.get(pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)


        if form.is_valid():
            c = form.save(commit=False)
            c.published_date = now()
            c.user = request.user
            c.post = p
            c.save()
            print("saved", c)
            return redirect("blog")
        else:
            return render(request, "blog/blog-single.html", {"form": form})

    form = CommentForm()


    comments=Comment.objects.filter(post_id=id).order_by("-published_date")
    c_count=comments.count()
    all_categories = Category.objects.all()
    print(c_count)
    context = {"post": p, "comments": comments, "form": form, "c_count":c_count, "all_categories":all_categories }
    context.update(get_categories())
    return render(request, "blog/blog-single.html", context)


def category(request, id=None):
    posts = Post.objects.filter(category__pk=id).order_by("-published_date")
    all_categories = Category.objects.all()
    context = {"posts": posts, "all_categories ":all_categories}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def search(request):
    print(request.method)
    print(request.POST)

    if request.method == 'POST':
        query = request.POST['query']
        posts = Post.objects.filter(content__icontains=query).order_by("-published_date")
    else:
        posts = []

    context = {"posts": posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            p = form.save(commit=False)
            p.published_date = now()
            p.user = request.user

            p.save()
            print("saved", p)
            return redirect("blog")
        else:
            return render(request, "blog/create.html", {"form": form})

    form = PostForm()
    return render(request, "blog/create.html", {"form": form})



@login_required
def comment(request, id=None):
    p = get_object_or_404(Post, pk=id)
    print(request, id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        #print(form)
        if form.is_valid():
            c = form.save(commit=False)
            c.published_date = now()
            c.user = request.user
            c.post = p
            c.save()
            print("saved", c)
            return redirect("blog")
        else:
            return render(request, "blog/post.html", {"form": form})

    form = CommentForm()
    return render(request, "blog/post.html", {"form": form})


def proba(request):
    if request.method == 'POST':
        c = request.POST.get('content')
        print(c)
    return render(request, "blog/post.html")