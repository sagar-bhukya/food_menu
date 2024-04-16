from django.urls import path
from .views import index,detail,create_item,update_item,delete_item,IndexClassView,FoodDetailView,CreateItem

urlpatterns = [
    #food/
    # path('',index,name="index"),
    path('',IndexClassView.as_view(),name="index"), #.as_view() method converts the class-based view into a callable function that Django can use to handle requests.

    #food/item
    # path('<int:item_id>/',detail,name="detail"),
    path('<int:pk>/',FoodDetailView.as_view(),name="detail"),#class based view
    # path('item',Item,name="item"),

    #add item
    # path('add/',create_item,name="create_item"),
    path('add/',CreateItem.as_view(),name="create_item"),#class based view

    #update item
    path('update/<int:id>',update_item,name="update_item"),

    #delete item
    path('delete/<int:id>',delete_item,name="delete_item"),
]
