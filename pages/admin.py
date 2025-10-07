from django.contrib import admin
from pages.models import Author, Category, Book
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    ordering = ("published",)



#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
    #list_display = ("title", "body", "created_at")
    #inlines = [CommentInLine]
    #search_fields = ("title", "body")
    #list_filter = ("created_at",)
    #ordering = ("created_at",)
    
#@admin.register(Comment)
#class CommentAdmin(admin.ModelAdmin):
 #   list_display = ("author", "post", "created_at")
  #  search_fields = ("author", "text")
   # list_filter = ("created_at",)


#@admin.register(Student)
#@admin.register(Course)
#@admin.register(Enrollment)
