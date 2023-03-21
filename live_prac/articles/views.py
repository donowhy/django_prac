from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk) # id는 pk라고 써줘도 괜찮다. django 내부적으로
    
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

################
#new 와 create를 합치기 GET방식이면 new, POST방식이면 create
# def create(request): 
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             return redirect('articles:detail', article.pk)
    
#             # 몇 번 페이지인지 pk가 필요하기 때문

#         # title = request.POST.get('title')
#         # content = request.POST.get('content')

#         # article = form.save() 얘가 아래와 같음!
#         # article = Article(title=title, content=content)
#         # article.save()
#         return redirect('articles:create')

#     else:  #요청 방식이 GET이라면
#         form = ArticleForm()
#         context = { 'form' : form }
#         return render(request, 'articles/create.html', context)

#다시 정리
def create(request): 
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    
    else:  #요청 방식이 GET이라면
        form = ArticleForm()
        
    context = { 'form' : form }
    return render(request, 'articles/create.html', context)

##########
#edit과 update를 합칠 수 있다.

# def update(request,pk):
#     article = Article.objects.get(pk=pk)
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
    
#         return redirect('articles:detail', article.pk)
#     else:
#         # 인스턴스, DB 레코드 삭제
#         context = {'article: article'}
#         return render(request, 'articles/update.html', context)


def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        #instance 는 가져온 article을 넣는것 !
        if form.is_valid():
            form.save()     
            return redirect('articles:detail', pk=article.pk)

    
    else:
        form = ArticleForm(instance=article)

    context = {'form': form}
    return render(request, 'articles/update.html', context)
        
def delete(request, pk):
    #pk에 해당되는 게시판 글 하나 정보를 가져오기
    article = Article.objects.get(pk=pk)
    # 인스턴스, DB 레코드 삭제
    article.delete()
    return redirect('articles:index')




# def new(request):  # GET방식
#     return render(request, 'articles/new.html')

# def create(request):  #POST 방식 처리
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    
    #DB에 새로운 Article 저장
    # Article.objects.create(
    #     title=title,
    #     content=content
    # )

# def edit(request, pk):
#     #pk에 해당되는 게시판 글 하나 정보를 가져오기
#     article = Article.objects.get(pk=pk)
#     # 인스턴스, DB 레코드 삭제
#     context = {
#         'article: article'
#     }
#     return render(request, 'articles/edit.html', context)

# def update(request,pk):
#     article = Article.objects.get(pk=pk)
#     article.title = request.POST.get('title')
#     article.content = request.POST.get('content')
#     article.save()
    
#     return redirect('articles:detail', article.pk)






