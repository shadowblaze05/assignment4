from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib import messages
from pages.models import Author, Book, Category
# from pages.forms import PostForm
from django.shortcuts import redirect


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def home(request):
    ctx = {"title": "Home", "features": ["Django", "Templates", "Static files"]}
    return render(request, "home.html", ctx)

def about(request):
    return render(request, "about.html", {"title": "About"})

def hello(request, name):
    return render(request, "hello.html", {"name": name})

def gallery(request):
    # Assume images placed in pages/static/img/
    images = ["img1.jpg", "img2.jpg", "img3.jpg"]
    return render(request, "gallery.html", {"images": images})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def server_error_view(request):
    return render(request, '500.html', status=500)

def admin(request):
    return redirect('/admin/')

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


# def post_list(request):
#     # Model.objects.all()
#     posts = Post.objects.all().prefetch_related('comments')
#     context = {
#         'posts': posts,
#         'title': 'Posts',
#     }
#     return render(request, 'post_list.html', context)

# def admin(request):
#     return redirect('/admin/')

# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'New post created')
#             return redirect('post_list')
#         messages.error(request, 'Get Better!')
#     else:
#         form = PostForm()
#     return render(request, 'post_form.html', {'form': form})

# def post_view(request, pk):
#     #post = get_object_or_404(Post, pk=pk)
#     post = Post.objects.get(pk=pk)
#     comments = Post.objects.prefetch_related('comments')
#     return render(request, 'post_view.html', {'post': post})

# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'New post created')
#             return redirect('post_list')
#         messages.error(request, 'Get Better!')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'post_form.html', {'form': form})

# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         messages.success(request, f"Goodbye {post.title} ")
#         return redirect('post_list')
#     return render(request, 'post_confirm_delete.html', {'post': post})