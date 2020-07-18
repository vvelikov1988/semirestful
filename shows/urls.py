from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    # path('/new', views.index),
    # path('/create', views.create),
    # path('/<int:show:id>', views.showdetails),
    # path('/<int:show:id>/edit', views.editshow),
    # path('/<int:show:id>/update', views.update),
    # path('/<int:show:id>/destroy', views.destroy),

]