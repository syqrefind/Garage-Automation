#Importing required django packages to process URLs.
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#Importing required functions from parking/views.py
from . import views
#Namespace for this urls.py file to be used in main urls.py file (../mysite/urls.py)
app_name = 'parking'

#Python list of url instances holding url patterns
urlpatterns = [

    # /parking/
    url(r'^$', views.index, name='index'),
    # /parking/main/
    url(r'^main/$', views.main, name='main'),
    # /parking/add_lot/
    url(r'^add_lot/$', views.add_lot, name='add_lot'),
    # /parking/delete_lot/
    url(r'^(?P<parkingLot_id>[0-9]+)/delete_lot/$', views.delete_lot, name='delete_lot'),
    # /parking/<Parking_Lot ID>/detail
    url(r'^(?P<parkingLot_id>[0-9]+)/$', views.detail, name='detail'),
    # /parking/<Parking_Lot ID>/add_spot
    url(r'^(?P<parkingLot_id>[0-9]+)/add_spot/$', views.add_spot, name='add_spot'),
    # /parking/<Parking_Lot ID>/delete_spot
    url(r'^(?P<parkingLot_id>[0-9]+)/delete_spot/(?P<spot_id>[0-9]+)/$', views.delete_spot, name='delete_spot'),
    # /parking/<Parking_Lot ID>/level/map
    url(r'^(?P<parkingLot_id>[0-9]+)/(?P<level>[0-9]+)/map/$', views.map, name='map'),
    # /parking/register_manager
    url(r'^register_manager/$', views.register_manager, name='register_manager'),
    # /parking/login_manager
    url(r'^login_manager/$', views.login_manager, name='login_manager'),
    # /parking/logout_manager
    url(r'^logout_manager/$', views.logout_manager, name='logout_manager'),
    # Polls the sensors and updates the spot occupation status
    # /parking/<parkingLot ID>/update_occupancy
    url(r'^(?P<parkingLot_id>[0-9]+)/update_occupancy/$', views.update_occupancy, name='update_occupancy'),
    # /parking/<Parking_Lot ID>/disable_spot
    url(r'^(?P<parkingLot_id>[0-9]+)/disable_spot/(?P<spot_id>[0-9]+)/$', views.disable_spot, name='disable_spot'),
    # /parking/<Parking_Lot ID>/disable_spot
    url(r'^(?P<parkingLot_id>[0-9]+)/enable_spot/(?P<spot_id>[0-9]+)/$', views.enable_spot, name='enable_spot'),
    # /parking/<Parking_Lot ID>/level/map      
    url(r'^(?P<parkingLot_id>[0-9]+)/(?P<level>[0-9]+)/map$', views.map, name='map'),
    # URL for checking lot status
    # /parking/<Parking_Lot ID>/system
    url(r'^(?P<parkingLot_id>[0-9]+)/system$', views.system, name='system'),
    # URL for simulating enter session
    # /parking/<Parking_Lot ID>/system/enter_session
    url(r'^(?P<parkingLot_id>[0-9]+)/system/enter_session/$', views.enter_session, name='enter_session'),
    # URL for simulating exit session
    # /parking/<Parking_Lot ID>/system/exit_session
    url(r'^(?P<parkingLot_id>[0-9]+)/system/exit_session/$', views.exit_session, name='exit_session'),
    #/parking/<Parking_Lot ID>/system/enter_guest/LICENSE_PLATE
    url(r'^(?P<parkingLot_id>[0-9]+)/system/enter_guest/(?P<license_plate>[A-Z0-9]+)/$', views.enter_guest, name='enter_guest'),
    #/parking/<Parking_Lot ID>/system/enter_guest/LICENSE_PLATE
    url(r'^(?P<parkingLot_id>[0-9]+)/system/enter_cash_guest/(?P<license_plate>[A-Z0-9]+)/$', views.enter_cash_guest, name='enter_cash_guest'),

]
#Add the list of static file URL pattern list.
urlpatterns += staticfiles_urlpatterns()                                                            
