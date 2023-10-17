from django.shortcuts import render, redirect
from web01 import models
from django.utils.safestring import mark_safe


def user_info(request):
    queryset = models.UserInfo.objects.all()

    # for obj in queryset: print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%M-%D"), obj.gender,
    # obj.get_gender_display(), obj.depart_id, obj.depart.title) obj.depart_id  获取数据库中存储的字段值 obj.depart.title
    # 根据id自动去级联的表中查询对应的数据 get_gender_display()  根据定义的元组来匹配对应的值
    return render(request, 'user_info.html', {"queryset": queryset})


def user_add(request):
    """添加用户"""
    if request.method == 'GET':
        context = {
            'gender_list': models.UserInfo.gender_choices,
            'depart_list': models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)

    # 从前端拿到数据
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('account')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gender')
    depart_id = request.POST.get('dp')
    print(name, pwd, age, account, ctime, gender, depart_id)

    # 把数据插入到数据表中
    models.UserInfo.objects.create(name=name, password=pwd, age=age, account=account,
                                   create_time=ctime, gender=gender, depart_id=depart_id)

    # 重定向到用户列表页面
    return redirect('/user/info/')


# ###################################   ModelForm示例   ###################################
from django import forms


class UserModelForm(forms.ModelForm):
    # 单独对一个字段校验
    name = forms.CharField(min_length=3, label='用户名')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender',
                  'depart']
        # widgets = {
        #     'name': forms.TextInput(attrs={"class": "form_control"})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


def user_model_form_add(request):
    """添加用户，基于modelform版本"""
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {'form': form})

    # 用户POST提交数据，数据校验
    form = UserModelForm(data=request.POST)
    # {'name': '11', 'password': '11', 'age': 123, 'account': Decimal('11'),
    #  'create_time': datetime.datetime(2021, 1, 1, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')), 'gender': 1, 'depart'
    #  : < Department: 运营部 >}
    if form.is_valid():
        print(form.cleaned_data)
        # 保存到数据库
        # models.UserInfo.objects.create()
        # 自动保存到数据库  包括了  常规操作的，取值，并create
        form.save()
        return redirect('/user/info/')
    # 校验失败  页面上提升错误信息
    print(form.errors)
    return render(request, 'user_model_form_add.html', {'form': form})


def user_edit(request, nid):
    """编辑用户"""
    # 根据id获取要编辑的哪一个用户对应的数据
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        # instance=获取到的值   会在前端自动显示出来
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 单独添加字段
        # form.instance.字段名 = 值
        # 默认保存的时用户输入的所有数据
        form.save()
        return redirect('/user/info/')
    return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/info/')
