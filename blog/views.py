from django.shortcuts import render


def post_list(request):
    # Template을 찾을 경로에서
    # post_list.htmldmf ckwdktj
    # 그 파일을 text로 만들어서 HttpRespons형태로 돌려준다.
    # 위 기능을 하는 shortcut함수
    return render(request, 'post_list.html')