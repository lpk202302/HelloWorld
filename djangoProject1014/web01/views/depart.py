from django.shortcuts import render, redirect
from web01 import models


def depart_info(request):
    # 去数据库中达到部门表的所有数据
    queryset = models.Department.objects.all()

    return render(request, 'depart_info.html', {'queryset': queryset})


def depart_add(request):
    # 判断数据传输方式
    if request.method == "GET":
        return render(request, "depart_add.html")

    # 从前端拿到数据
    title = request.POST.get("title")

    # 保存到数据库
    models.Department.objects.create(title=title)

    # 重定向到部门里表
    return redirect("/depart/info/")


def depart_delete(request):
    # 从前端获取序号
    nid = request.GET.get('nid')

    # 删除数据   http://127.0.0.1:8000/depart/delete/?nid=1
    models.Department.objects.filter(id=nid).delete()

    # 重定向到部门里表
    return redirect("/depart/info/")


def depart_edit(request, nid):
    if request.method == 'GET':
        # 获取nid  取第一行
        row_object = models.Department.objects.filter(id=nid).first()

        # row_object对应数据库的Department表
        # print(row_object.id, row_object.title)

        return render(request, 'depart_edit.html', {'row_object': row_object})

    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)

    # 重定向到部门里表
    return redirect("/depart/info/")

