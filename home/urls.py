from django.urls import path

from . import views

urlpatterns = [
	path('signin', views.signin, name='signin'),
	path('handleSignin', views.handleSignin, name='handleSignin'),

	path('', views.login, name='login'),
	path('handleLogin', views.handleLogin, name='handleLogin'),
	path('handleLogout', views.handleLogout, name='handleLogout'),

	path('home', views.home, name='home'),

	path('PurchaseOrder', views.PurchaseOrder, name='PurchaseOrder'),
	path('CreatedPurchaseOrder', views.CreatedPurchaseOrder, name='CreatedPurchaseOrder'),
	path('ReceivedPurchaseOrder', views.ReceivedPurchaseOrder, name='ReceivedPurchaseOrder'),
	path('ViewReceivedPurchaseOrder', views.ViewReceivedPurchaseOrder, name='ViewReceivedPurchaseOrder'),

	path('handlePurchaseOrder', views.handlePurchaseOrder, name='handlePurchaseOrder'),
	path('handleReceivedPurchaseOrder', views.handleReceivedPurchaseOrder, name='handleReceivedPurchaseOrder'),

	path('Invoice', views.invoice, name='Invoice'),
	path('CreatedInvoice', views.CreatedInvoice, name='CreatedInvoice'),
	path('ReceivedInvoice', views.ReceivedInvoice, name='ReceivedInvoice'),
	path('ViewReceivedInvoice', views.ViewReceivedInvoice, name='ViewReceivedInvoice'),

	path('handleInvoice', views.handleInvoice, name='handleInvoice'),
	path('handleReceivedInvoice', views.handleReceivedInvoice, name='handleReceivedInvoice'),

	path('Challan', views.challan, name='Challan'),
	path('CreatedChallan', views.CreatedChallan, name='CreatedChallan'),
	path('ReceivedChallan', views.ReceivedChallan, name='ReceivedChallan'),
	path('ViewReceivedChallan', views.ViewReceivedChallan, name='ViewReceivedChallan'),

	path('handleChallan', views.handleChallan, name='handleChallan'),
	path('handleReceivedChallan', views.handleReceivedChallan, name='handleReceivedChallan'),
    

	path('about',views.about,name='about'),
]