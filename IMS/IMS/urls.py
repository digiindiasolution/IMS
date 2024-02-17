from django.contrib import admin
from django.urls import path
from home.views import home, raw_material , home , finished_goods , semi_finished_goods ,all_manufacture_order , all_purchase_order , all_bills_order,our_members,our_vendors


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home.home_view),
    path('raw-materials/',raw_material.rawMaterial_view),
    path('finished-goods/',finished_goods.finisedGoods_view),
    path('semi-finished-goods/',semi_finished_goods.semiFinishedGoods_view),
    path('all-purchase-order/',all_purchase_order.allPurchaseOrder_views),
    path('all-manufacture-order/',all_manufacture_order.allManufactureOrder),
    path('all-bills-order/',all_bills_order.allBillsOrder_view),
    path('our-members/',our_members.ourMembers_view),
    path('our-vendors/',our_vendors.ourVendors_view),
    
    # path('')
]
