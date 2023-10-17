from django.shortcuts import render, redirect
from web01 import models
from django.utils.safestring import mark_safe

# ##################################  靓号管理  ##################################


def pretty_info(request):
    # 测试数据使用
    # for i in range(100):
    #     models.PrettyNum.objects.create(mobile='12312341234', price=100, level=1, status=1)

    # queryset = models.PrettyNum.objects.all()

    # 定义空字典
    global page_string
    data_dict = {}
    # 从前端的请求获取到传过来的q
    value = request.GET.get('q', '')
    # 判断是否未空
    if value:
        data_dict['mobile__contains'] = value

    # 根据用户想要访问的页面，计算出起始位置和结束位置
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page - 1) * page_size
    end = page * page_size
    # print(start, end)
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")[start:end]

    # 数据总条数
    total_count = models.PrettyNum.objects.filter(**data_dict).order_by("-level").count()
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1

    # 计算出，显示当前页的前n页和后n页
    plus = 3
    start_page = page - plus
    if start_page <= 0:
        start_page = 1
    end_page = page + plus + 1
    if end_page >= total_page_count:
        end_page = total_page_count

    # 页码
    page_str_list = []
    page_string = []
    for i in range(start_page, end_page + 1):
        ele = i
        page_str_list.append(ele)
    # print(page_str_list)

    return render(request, 'pretty_info.html', {'queryset': queryset, 'value': value, 'page_str_list': page_str_list})


from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django import forms


class PrettyModelForm(forms.ModelForm):
    # 通过正则表达式添加错误信息
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = "__all__"      # 同上
        # exclude = ['level']     # 排除哪些字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    # 通过钩子方法添加错误信息
    def clean_mobile(self):
        text_mobile = self.cleaned_data['mobile']
        print(self.instance.pk)
        if models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists():
            raise ValidationError('手机号已存在')
        # 验证通过，返回用户输入的内容
        return text_mobile


def pretty_add(request):
    if request.method == 'GET':
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {'form': form})

    data = PrettyModelForm(data=request.POST)
    if data.is_valid():
        data.save()
        return redirect('/pretty/info/')
    print(data.errors)
    return render(request, 'pretty_info.html', {'data': data})


class PrettyEditModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label='手机号',
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')],
        disabled=True,
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = "__all__"      # 同上
        # exclude = ['level']     # 排除哪些字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    def clean_mobile(self):
        text_mobile = self.cleaned_data['mobile']
        # 获取当前信息的id
        # print(self.instance.pk)
        if models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists():
            raise ValidationError('手机号已存在')
        # 验证通过，返回用户输入的内容
        return text_mobile


def pretty_edit(request, nid):
    # 根据id查询出来用户要修改那一列数据的数据
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    # print(row_object)
    if request.method == 'GET':
        # 旧方法
        # queryset = models.PrettyNum.objects.all()
        # 新方法
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {"form": form})

    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/pretty/info/')
    return render(request, 'pretty_edit.html', {"form": form})


def pretty_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/info/')
