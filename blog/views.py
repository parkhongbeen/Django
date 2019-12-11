import os
from django.http import HttpResponse


def post_list(request):
    # 상위폴더(blog)의
    #  상위폴더 (djangogirls)의
    #   하위폴더 (templates)의
    #     하위폴더 (post_list.html)내용을 read()한 결과를 HttpResponse에 인자로 전달

    # 경로이동
    # os.path.abspath(__file__) <- 현재 파일의절대 경로를 리턴해줌
    #  os.path.dirname
    #  os.path.join
    # 파일열기
    #  open
    cur_file_path = os.path.abspath(__file__)
    blog_dir_path = os.path.dirname(cur_file_path)
    root_dir_path = os.path.dirname(blog_dir_path)
    templates_dir_path = os.path.join(root_dir_path, 'templates')
    post_list_html_path = os.path.join(templates_dir_path, 'post_list.html')

    f = open(post_list_html_path, 'rt')
    html = f.read()
    f.close()

    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>post List!</h1>'
        '<div>'
        '<p>publicished: 12.11.2019, 14:38</p>'
        '<h2><a href="">My First post</a></h2>'
        '<p>asdfasdfsadf</p>'
        '</div>'
        '<div>'
        '<p>publicished: 12.11.2019, 14:38</p>'
        '<h2><a href="">My second post</a></h2>'
        '<p>asdfasdfsadf</p>'
        '</div>'
        '</body>'
        '</html>'
    )
