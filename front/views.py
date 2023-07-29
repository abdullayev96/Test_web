from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.views.generic import DetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin


def home(request):
    news = Book.objects.all().order_by('-id')


    # paginator = Paginator(news, 3)
    #
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    return render(request, "list.html", { "news": news})



#
def get_client_ip(request):
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip = address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class BookDetailView(DetailView):
    model = Book
    template_name = "detail.html"
    context_object_name = "new"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        ctx = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)



        if IpModel.objects.filter(ip=ip).exists():
            print("ip already views")
            new_id = request.GET.get('new-id')
            print(new_id)
            new = Book.objects.get(pk=new_id)
            new.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            new_id = request.GET.get('new-id')
            new = Book.objects.get(pk=new_id)
            new.views.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(ctx)

def contact(request):
    if request.method == 'POST':
        model = Contact()
        model.name = request.POST.get('name')
        model.subject = request.POST.get('subject')
        model.number = request.POST.get('number')
        model.tg_name = request.POST.get('tg_name')


        model.save()
        return render(request, "contact.html")

    else:
        return render(request, "contact.html")


#
#
# def BookDetail(request, pk):
#     pass

    # new  =  get_object_or_404(Book, pk=pk)
    #
    # def get_client_ip(request):
    #     address = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if address:
    #         ip = address.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip
    #
    # ip = get_client_ip(request)
    # u = IpModel(user=ip)
    # print(ip)
    # res = IpModel.objects.filter(Q(user__icontains=ip))
    # if len(res) == 1:
    #     print("already this is")
    #
    # elif len(res) > 1:
    #     print("already exists ")
    #
    # else:
    #     u.save()
    #
    # count = IpModel.objects.all().count()
    # print("user is ...", count)
    # ctx = {
    #
    #     "new": new,
    #     "count":count
    # }
    # return render(request, 'detail.html', ctx)






#
# def author_list(request):
#     authors=Author.objects.all()
#     ctx ={
#         "authors":authors
#     }
#     return render(request, 'authors_list.html', ctx)
#
#
#
# def author_details(request, author_id):
#     author=Author.objects.get(id=author_id)
#     books=Book.objects.filter(author_id=author_id)
#
#     ctx ={
#         "author":author,
#         "books":books
#     }
#     return render(request, 'author_details.html', ctx)
#
#
# def genre_list(request):
#     genres=Genre.objects.all()
#     ctx={
#         "genres":genres
#     }
#     return render(request, 'genre_list.html', ctx)
#
#
# def genre_details(request, genre_id):
#     genre=Genre.objects.get(id=genre_id)
#     books=Book.objects.filter(genre_id=genre_id)
#     ctx = {
#         "genre":genre,
#         "books":books
#     }
#     return render(request, 'genre_details.html', ctx)
#
# def book_list(request):
#     books=Book.objects.all()
#     ctx = {
#         "books":books
#     }
#     return render(request, 'book_list.html', ctx)
#
# def book_details(request, book_id):
#     book=Book.objects.get(id=book_id)
#     ctx ={
#         "book":book
#     }
#     return render(request, 'book_details.html', ctx)



