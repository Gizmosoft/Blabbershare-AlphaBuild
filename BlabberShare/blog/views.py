from django.shortcuts import render, redirect
from .models import blogPost
from .forms import PostForm

# Create your views here.
def index(request):
    blogs = blogPost.objects.order_by("-date_added")
    context = {'blogs' : blogs}
    return render(request,'blog/index.html', context)

def ipform(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            new_req = blogPost(posttitle = request.POST['posttitle'],
            postdesc = request.POST['postdesc'])

            new_req.save()
            return redirect('index')

    else: 
        form = PostForm()

        context = {'form' : form}

    return render(request, 'blog/ipform.html',context)
