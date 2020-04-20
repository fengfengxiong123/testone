from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from UpDown.models import Rank
import json


# Create your views here.
def index(request):
    return render(request, 'UpDown/index.html')


def upScoreClientnum(request):
    """上传分数和客户端号"""
    if request.method == 'POST':
        client_num = request.POST['client_num']
        score = request.POST['score']
        obj, create = Rank.objects.update_or_create(client_num=client_num, defaults={'score': score})
        context = {'create': create}
    else:
        context = {'create': None}
    return JsonResponse(context)


def checkRank(request):
    """查看排行榜"""
    if request.method == "POST":
        # 仅有客户端号时执行
        if request.POST['check_client_num'] != '':
            check_client_num = request.POST['check_client_num']
            objs = Rank.objects.order_by('-score').values('client_num', 'score')
            ranks_all = [{'name': v, 'num': i + 1} for i, v in enumerate(objs)]
            ranks = ranks_all[0:10]
            try:
                obj_one = Rank.objects.get(client_num=check_client_num)
            except Exception as e:
                context = {'ranks': ranks, 'obj_one': None}
            else:
                for i in ranks_all:
                    if check_client_num == i['name']['client_num']:
                        obj_one_num = i['num']
                context = {'ranks': ranks, 'obj_one': {'client_num': check_client_num, 'score': obj_one.score},
                           'obj_one_num': obj_one_num}

        # 仅有排名范围时执行
        elif (request.POST['pre_num'] != '') and (request.POST['next_num'] != ''):  # 排名范围查询
            pre_num = request.POST['pre_num']
            next_num = request.POST['next_num']

            # 输入的范围信息正确时执行
            if pre_num.isdigit() and next_num.isdigit() and int(next_num) > int(pre_num) and int(pre_num) > 0:
                objs = Rank.objects.order_by('-score').values('client_num', 'score')
                ranks = [{'name': v, 'num': i + 1} for i, v in enumerate(objs)]
                ranks = ranks[int(pre_num) - 1:int(next_num)]
                context = {'ranks': ranks}
            # 范围信息有误时执行
            else:
                ranks = [{'name': {'client_num': '请按顺序输入正整数', 'score': '无'}, 'num': '无'}]
                context = {'ranks': ranks}


        # 客户端号和范围都有或都无
        else:
            ranks = [{'name': {'client_num': '输入客户端号和范围中的一项', 'score': '无'}, 'num': '无'}]
            context = {'ranks': ranks}

        return JsonResponse(context)
    else:
        return HttpResponse('请求有误')
