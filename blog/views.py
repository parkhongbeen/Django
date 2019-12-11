from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
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
