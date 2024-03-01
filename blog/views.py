from django.shortcuts import render, get_object_or_404

from blog.models import Post


# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(active=True)
    context={
        "posts":posts,
        "taille":len(posts)
    }
    return render(request,"blog.html",context=context)


def blog_view_unique(request,slug):
    post=get_object_or_404(Post,slug=slug)
    others=Post.objects.filter(active=True).exclude(slug__in=[slug])
    context={
        "post":post,
        "taille":len(others)
    }
    return render(request,"blog_detail.html",context=context)



