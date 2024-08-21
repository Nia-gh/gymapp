from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category
from django.core.paginator import Paginator
# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    blog_list = paginator.get_page(page_number)

    context = {
        "blog_list": blog_list
    }
    return render(request, "blog/blog_list.html", context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    categories = Category.objects.all()

    context = {
        "blog": blog,
        "tags": tags,
        "categories": categories,
    }
    return render(request, "blog/blog_detail.html", context)


def blog_tag(request,tag):
    blogs = Blog.objects.filter(tags__slug=tag)
    context = {
        "blogs": blogs
    }
    return render(request, "blog/blog_list.html", context)


def blog_category(request,category):
    blogs = Blog.objects.filter(category__slug=category)
    context = {
        "blogs": blogs
    }
    return render(request, "blog/blog_list.html", context)
