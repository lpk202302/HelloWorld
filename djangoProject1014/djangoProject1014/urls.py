"""
URL configuration for djangoProject1014 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import web01
from web01 import views
from web01.views import depart, pretty, user, admin

urlpatterns = [
    # path("admin/", admin.site.urls),
    # 部门管理
    path("depart/info/", depart.depart_info),
    path("depart/add/", depart.depart_add),
    path("depart/delete/", depart.depart_delete),
    path("depart/<int:nid>/edit/", depart.depart_edit),
    # 用户管理
    path("user/info/", user.user_info),
    path("user/add/", user.user_add),
    path("user/model/form/add/", user.user_model_form_add),
    path("user/<int:nid>/edit/", user.user_edit),
    path("user/<int:nid>/delete/", user.user_delete),
    # 靓号管理
    path("pretty/info/", pretty.pretty_info),
    path("pretty/add/", pretty.pretty_add),
    path("pretty/<int:nid>/edit/", pretty.pretty_edit),
    path("pretty/<int:nid>/delete/", pretty.pretty_delete),

    # 管理员管理
    path("admin/info/", admin.admin_info),
    path("admin/add/", admin.admin_add),
]
