from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date

def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 5) # Show 5 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
	
    return render(request, 'blog/index.html', {
		'posts': posts,
		'categories': Category.objects.all()
	})
 
def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def contacts(request):
     return render(request, 'blog/contacts.html') 

	 
def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'blog/index.html')
        else:
            return render(request, 'blog/disabled.htnl')
    else:
        return render(request, 'blog/invalid.html')
		
def profile(request):
	return render(request, 'blog/profile.html')
	
def logout_view(request):
	logout(request)
	return redirect('/')
	
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {
        'form': form,
    })
	