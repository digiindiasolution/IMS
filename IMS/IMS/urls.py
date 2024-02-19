from django.contrib import admin
from django.urls import path
from home.views import home, raw_material , home , finished_goods , semi_finished_goods ,all_manufacture_order , all_purchase_order , all_bills_order,our_members,our_vendors,add_row_material,manufacturing_order,create_purchase_order,add_finished_goods,create_bill,add_member


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home.home_view),
    path('raw-materials/',raw_material.rawMaterial_view),
    path('finished-goods/',finished_goods.finisedGoods_view),
    path('create-bill/',create_bill.createBill_view),
    path('add-member/',add_member.addMember_view),
    path('add-finished-goods/',add_finished_goods.addFinishedGoods_view),
    path('add-manufacture-order/',manufacturing_order.manufacturingOrder_view),
    path('semi-finished-goods/',semi_finished_goods.semiFinishedGoods_view),
    path('all-purchase-order/',all_purchase_order.allPurchaseOrder_views),
    path('create-purchase-order/',create_purchase_order.createPurchaseOrder_view),
    path('all-manufacture-order/',all_manufacture_order.allManufactureOrder),
    path('all-bills-order/',all_bills_order.allBillsOrder_view),
    path('our-members/',our_members.ourMembers_view),


    path('our-vendors/',our_vendors.ourVendors_view),
    path('add-vendor/',our_vendors.addVendor_view),
    path('delete-vendor/<id>/',our_vendors.deleteVendor_view),
    path('update-vendor/<id>/',our_vendors.updateVendor_view),



    path('add-raw-material/',add_row_material.addRowMaterial_view),

    
    # path('')
]
