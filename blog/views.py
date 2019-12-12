from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    # Template을 찾을 경로에서
    # post_list.html을 찾아
    # 그 파일을 text로 만들어서 HttpRespons형태로 돌려준다.
    # 위 기능을 하는 shortcut함수

    # content = loader.render_to_string('post_list.html', None, request)
    # return HttpResponse(content)

    # 1. posts라는 변수에 전체 Post를 가지는 Queryset객체를 할당
    #    hint) Post.ovjects.무언가.....를 실행한 결과는 QuerySet객체가 된다.
    # 2. context라는 dict를 생성하며, 'post'키에 위 posts변수를 value로 사용하도록 한다.
    # 3. render의 세번째 위치인자로 위 context변수를 전달한다.
    posts = Post.objects.all()
    context = {
        'posts': posts,

    }
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    print('post_detail request', request)
    print('post_detail pk', pk)

    # 이 view함수의 매개변수로 전달되는 'pk'를 사용해서
    # 전달받은 'pk'값이 자신의 'pk'DB Column값과 같은 Post를 post변수에 지정
    # 이후 pk에 따라 /post-detail/에 접근했을 때, 다른 Post가 출력되는지 확인
    # posts = Post.objects.filter(pk=pk)
    # print = posts[0]

    # try:
    #     post = Post.objects.get(pk=pk)
    # except:
    #     return HttpResponse('없음')

    get_object_or_404(Post, pk=pk)


    # URL:      /post-detail/
    # View      post_detail(이 함수)
    # Template: post_detail.html
    # 내용으로<h1>Post Dtail!</h1>을 갖도록 함
    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)