from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Challan, Received_Challan, Invoice, Received_Invoice, Received_Purchase_Order, Purchase_Order

# Create your views here.

def login(request):
	return render(request, 'home/login.html')

def handleLogin(request):
	if request.method == 'POST':
		#Get the parameters here
		loginusername = request.POST['loginusername']
		loginpassword = request.POST['loginpassword']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request)
			messages.success(request, "LogIn successfull!")
			return redirect('home')
		else:
			messages.error(request, "Invalid credentials!")
			return redirect('/')

	return HttpResponse('404 Page not found')

def handleLogout(request):
	logout(request)
	messages.success(request, "Logout successfull!")
	return redirect('/')

def signin(request):
	return render(request, 'home/signin.html')

def handleSignin(request):
	if request.method == 'POST':
		#Get the parameters here
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		username = request.POST['username']
		password = request.POST['password']
		confirmpassword = request.POST['confirmpassword']

		#Check for errors
		if len(username) > 10:
			messages.error(request, "Username must be less than 10 characters")
			return redirect('signin')
			
		if not username.isalpha():
			messages.error(request, "Username should not contain numbers & special characters")
			return redirect('signin')

		if len(password) <= 7:
			messages.error(request, "Passwords should be equal or more than 8 characters")
			return redirect('signin')

		if password != confirmpassword:
			messages.error(request, "Passwords do not match")
			return redirect('signin')

		#Create the user
		myuser = User.objects.create_user(username, email, password)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.save()
		messages.success(request, "Your account has been successfully created!")
		return redirect('/')
	else:
		return HttpResponse('404 Page not found')

def home(request):
	return render(request, 'home/home.html')

def about(request):
	return render(request,'home/about.html')

def PurchaseOrder(request):
	return render(request, "purchase/PurchaseOrder.html")

def handlePurchaseOrder(request):
	if request.method == 'POST':
		#Get Parameters here
		pono = request.POST['pono']
		date = request.POST['date']
		orderto = request.POST['orderto']
		shipto = request.POST['shipto']
		dt = request.POST['dt']
		mtop = request.POST['mtop']
		suppref = request.POST['suppref']
		otherref = request.POST['otherref']
		dthrough = request.POST['dthrough']
		pc = request.POST['pc']
		particulars = request.POST['particulars']
		quantity = request.POST['quantity']
		rate = request.POST['rate']
		amount = request.POST['amount']
		discount = request.POST['discount']
		ald = request.POST['ald']
		gst = request.POST['gst']
		shc = request.POST['shc']
		total = request.POST['total']

		#Saving data in database
		purchaseorder = Purchase_Order(Purchase_Order_No = pono, Date = date, Order_To = orderto, Ship_To = shipto, Delivery_Terms = dt, Mode_Terms_Of_Payment = mtop, Supplier_Reference = suppref, Other_Reference = otherref, Despatched_Through = dthrough, Particulars_Code = pc, Particulars = particulars, Quantity = quantity, Rate = rate, Amount = amount, Discount = discount, Amount_Less_Discount = ald, GST = gst, Shipping_Handling_Charges = shc, Total = total)
		purchaseorder.save()
		messages.success(request, "Purchase Order is saved!")
		return redirect('CreatedPurchaseOrder')
	else:
		messages.error(request, "Purchase Order doesn't saved")
		return redirect('PurchaseOrder')

def CreatedPurchaseOrder(request):
	pos = Purchase_Order.objects.all()
	print(pos)
	params = {'purchase_order': pos}
	return render(request, 'purchase/CreatedPurchaseOrder.html', params)

def ReceivedPurchaseOrder(request):
	return render(request, "purchase/ReceivedPurchaseOrder.html")

def handleReceivedPurchaseOrder(request):
	if request.method == 'POST':
		#Get Parameters here
		pono = request.POST['pono']
		date = request.POST['date']
		invoiceto = request.POST['invoiceto']
		shipto = request.POST['shipto']
		dt = request.POST['dt']
		mtop = request.POST['mtop']
		suppref = request.POST['suppref']
		otherref = request.POST['otherref']
		dthrough = request.POST['dthrough']
		pc = request.POST['pc']
		particulars = request.POST['particulars']
		quantity = request.POST['quantity']
		rate = request.POST['rate']
		amount = request.POST['amount']
		discount = request.POST['discount']
		ald = request.POST['ald']
		gst = request.POST['gst']
		shc = request.POST['shc']
		total = request.POST['total']

		#Saving data in database
		receivedpurchaseorder = Received_Purchase_Order(Purchase_Order_No = pono, Date = date, Invoice_To = invoiceto, Ship_To = shipto, Delivery_Terms = dt, Mode_Terms_Of_Payment = mtop, Supplier_Reference = suppref, Other_Reference = otherref, Despatched_Through = dthrough, Particulars_Code = pc, Particulars = particulars, Quantity = quantity, Rate = rate, Amount = amount, Discount = discount, Amount_Less_Discount = ald, GST = gst, Shipping_Handling_Charges = shc, Total = total)
		receivedpurchaseorder.save()
		messages.success(request, "Purchase Order is saved!")
		return redirect('ViewReceivedPurchaseOrder')
	else:
		messages.error(request, "Purchase Order doesn't saved")
		return redirect('ReceivedPurchaseOrder')

def ViewReceivedPurchaseOrder(request):
	rpos = Received_Purchase_Order.objects.all()
	print(rpos)
	params = {'received_purchase_order': rpos}
	return render(request, 'purchase/ViewReceivedPurchaseOrder.html', params)

def invoice(request):
	return render(request, "invoice/Invoice.html")

def handleInvoice(request):
	if request.method == 'POST':
		#Get parameters here
		invoiceno = request.POST['invoiceno']
		date_1 = request.POST['date_1']
		invoiceto = request.POST['invoiceto']
		orderno = request.POST['orderno']
		date_2 = request.POST['date_2']
		particulars = request.POST['particulars']
		challanno = request.POST['challanno']
		quantity = request.POST['quantity']
		rate = request.POST['rate']
		amount = request.POST['amount']
		gst = request.POST['gst']
		total = request.POST['total']

		#Saving data in database
		invoice = Invoice(InvoiceNo = invoiceno, Date_1 = date_1, InvoiceTo = invoiceto, OrderNo = orderno, Date_2 = date_2, Particulars = particulars, ChallanNo = challanno, Quantity = quantity, Rate = rate, Amount = amount, GST = gst, Total = total)
		invoice.save()
		messages.success(request, "Invoice is saved!")
		return redirect('CreatedInvoice')
	else:
		messages.error(request, "Invoice doesn't saved")
		return redirect('Invoice')

def CreatedInvoice(request):
	invoices = Invoice.objects.all()
	print(invoices)
	params = {'invoice': invoices}
	return render(request, 'invoice/CreatedInvoice.html', params)

def ReceivedInvoice(request):
	return render(request, "invoice/ReceivedInvoice.html")

def handleReceivedInvoice(request):
	if request.method == 'POST':
		#Get parameters here
		invoiceno = request.POST['invoiceno']
		supplier = request.POST['supplier']
		date = request.POST['date']
		delivery_note = request.POST['delivery_note']
		mtop = request.POST['mtop']
		suppref = request.POST['suppref']
		otherref = request.POST['otherref']
		orderno = request.POST['orderno']
		dnd = request.POST['dnd']
		ddn = request.POST['ddn']
		dt = request.POST['dt']
		tod = request.POST['tod']
		particulars = request.POST['particulars']
		hsnsac = request.POST['hsnsac']
		quantity = request.POST['quantity']
		rate = request.POST['rate']
		amount = request.POST['amount']
		gst_1 = request.POST['gst_1']
		hsa = request.POST['hsa']
		gst_2 = request.POST['gst_2']
		total = request.POST['total']
		paidby = request.POST['paidby']

		#Saving data in database
		receivedinvoice = Received_Invoice(InvoiceNo = invoiceno, Supplier = supplier ,Date = date, Delivery_Note = delivery_note, Mode_Terms_Of_Payment = mtop, Supplier_Reference = suppref, Other_Reference = otherref, OrderNo = orderno, Delivery_Note_Date = dnd, Despatched_Document_No = ddn, Despatched_Through = dt,Terms_Of_Delivery = tod, Particulars = particulars, HSN_SAC = hsnsac,Quantity = quantity, Rate = rate, Amount = amount, GST_1 = gst_1, HSN_SAC_Amount = hsa, GST_2 = gst_2, Total = total, PaidBy = paidby)
		receivedinvoice.save()
		messages.success(request, "Invoice is saved!")
		return redirect('ViewReceivedInvoice')
	else:
		messages.error(request, "Invoice doesn't saved")
		return redirect('ReceivedInvoice')

def ViewReceivedInvoice(request):
	rinvoices = Received_Invoice.objects.all()
	print(rinvoices)
	params = {'received_invoice': rinvoices}
	return render(request, 'invoice/ViewReceivedInvoice.html', params)

def challan(request):
	return render(request, "challan/Challan.html")

def handleChallan(request):
	if request.method == 'POST':
		#Get the parameters here
		challanno = request.POST['challanno']
		date = request.POST['date']
		challanto = request.POST['challanto']
		particulars = request.POST['particulars']
		quantity = request.POST['quantity']

		#Saving the data in database
		challan = Challan(ChallanNo = challanno, Date = date, ChallanTo = challanto, Particulars = particulars, Quantity = quantity)
		challan.save()
		messages.success(request, "Challan is saved!")
		return redirect('CreatedChallan')
	else:
		messages.error(request, "Challan doesn't saved")
		return redirect('Challan')

def CreatedChallan(request):
	challans = Challan.objects.all()
	print(challans)
	params = {'challan': challans}
	return render(request, 'challan/CreatedChallan.html', params)

def ReceivedChallan(request):
	return render(request, "challan/ReceivedChallan.html")

def handleReceivedChallan(request):
	if request.method == 'POST':
		#Get parameters here
		challanno_1 = request.POST['challanno_1']
		date_1 = request.POST['date_1']
		subject = request.POST['subject']
		particulars = request.POST['particulars']
		quantity = request.POST['quantity']
		weight = request.POST['weight']
		rate = request.POST['rate']
		total = request.POST['total']
		challanno_2 = request.POST['challanno_2']
		date_2 = request.POST['date_2']
		returned_quantity = request.POST['returned_quantity']

		#Saving the data
		received_challan = Received_Challan(ChallanNo_1 = challanno_1, Date_1 = date_1, Subject = subject, Particulars = particulars, Quantity = quantity, Weight = weight, Rate = rate, Total = total, ChallanNo_2 = challanno_2, Date_2 = date_2, Returned_Quantity = returned_quantity)
		received_challan.save()
		messages.success(request, "Challan is saved!")
		return redirect('ViewReceivedChallan')
	else:
		messages.error(request, "Challan doesn't saved")
		return redirect('ReceievedChallan')

def ViewReceivedChallan(request):
	rchallans = Received_Challan.objects.all()
	print(rchallans)
	params = {'received_challan': rchallans}
	return render(request, 'challan/ViewReceivedChallan.html', params)