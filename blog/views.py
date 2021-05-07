from django.shortcuts import render,HttpResponse
from blog.models import Blog,Contact

# Create your views here.
def home(requests):
    return render(requests,'index.html')

def about(requests):
    return render(requests,'about.html')

def blog(requests):
    blogs = Blog.objects.all()
    context = {'blogss':blogs}
    print(context)
    return render(requests,'bloghome.html',context)


def blogpost(request,slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}

    return render(request,'blogpost.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        instance = Contact(name = name,email = email,phone = phone,desc =desc)
        instance.save()
    return render(request,'contact.html')

def search(request):
    query = request.GET['query']
    searchedPosts= Blog.objects.filter(title__icontains=query)
    params = {'searchedPosts':searchedPosts}

    return render(request,'search.html',params)