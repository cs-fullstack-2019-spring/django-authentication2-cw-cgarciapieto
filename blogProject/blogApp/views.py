from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import BlogModel
# function that pulls in the model and assigns it to context to be rendered on the page
@login_required
def all_blogs(request):
    blog_list = BlogModel.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'blogApp/all_blogs.html', context)

# pulls the users entries not all blogs

@login_required
def blog_entry(request):
    blog_list = BlogModel.objects.filter(blog_user=request.user)
    context = {'blog_list': blog_list}
    return render(request, 'blogApp/my_entries.html',context)