from django import forms

from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError

from web01 import models
from web01.utils.encrypt import md5

def admin_info(request):
    queryset = models.Admin.objects.all()

    context = {
        'queryset': queryset,
    }

    return render(request, 'admin_info.html', context)


class AdminModelForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(render_value=True),  # render_value=True 可以让前端输入的内容错误时也不清空
    )

    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(render_value=True),  # render_value=True 可以让前端输入的内容错误时也不清空
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        # print(self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if pwd != confirm:
            raise ValidationError('密码不一致')
        # 返回什么，保存到数据库的就是什么
        # 就是：clean_字段名  return 字段名  将这个字段名存到数据库里
        return confirm


def admin_add(request):
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {'title': '新建管理员', 'form': form})
    form = AdminModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/info')

    return render(request, 'change.html', {'title': '新建管理员', 'form': form})
