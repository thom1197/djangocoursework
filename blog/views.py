from blog.models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_view(request):
    return render(request, 'blog/home.html', {})

def get_latest_post(request):
    published_posts = Post.objects.exclude(published_date=None).order_by('-published_date')
    return {
        'latestpost': published_posts.first()
        }

def post_detail(request, pk):
    published_posts = Post.objects.exclude(published_date=None).order_by('-published_date')
    post = get_object_or_404(Post, pk=pk)

    posts_context = {
        'thispost': post,
        'otherposts': published_posts.exclude(pk=post.pk)
    }
    return render(request, 'blog/posts.html', posts_context)

def cv_view(request):
    return render(request, 'blog/cv.html', {})

def contact_view(request):
    return render(request, 'blog/contact.html', {})
