from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'blog/home.html', {})

def about_view(request):
    return render(request, 'blog/about.html', {})

def posts_view(request):
    return render(request, 'blog/posts.html', {})

def gallery_view(request):
    return render(request, 'blog/gallery.html', {})

def contact_view(request):
    return render(request, 'blog/contact.html', {})
    
