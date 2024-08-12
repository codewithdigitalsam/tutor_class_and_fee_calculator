from django.shortcuts import render, redirect
from tutor.models import Tutor
from tutor.forms import TutorForm, TutorEditForm
from django.db.models import Sum
from datetime import datetime
from dateutil.relativedelta import relativedelta
from num2words import num2words
from django.contrib import messages

def showTable(request):
    tutor = Tutor.objects.all()
    return render(request,'table.html',{'tutor':tutor})

def showForm(request):
    if request.method == 'POST':
        fm = TutorForm(request.POST)
        if fm.is_valid():
            cd = fm.cleaned_data['classdate']
            md = fm.cleaned_data['mode']
            ch = fm.cleaned_data['classhour']
            reg = Tutor(classdate=cd,mode=md,classhour=ch)
            reg.save()
            messages.success(request, 'Your operation was successful!')
    else:
        fm = TutorForm()
    return render(request,'form.html',{'form':fm})

def showBill(request):
    # Finding out the current month
    totalclass = Tutor.objects.aggregate(total_amount=Sum('classhour'))
    totalclass1 = totalclass['total_amount']
    # Finding out the previous month
    currentmonth = datetime.now().strftime('%B')
    current_date = datetime.now()
    previous_month_date = current_date - relativedelta(months=1)
    previousmonth = previous_month_date.strftime('%B')
    # Calculation of extra fees for extra class taken
    fixedclass = 24
    extraclass = totalclass1-fixedclass
    extraclassfee = extraclass*500
    devidedextraclassfee = extraclassfee/2
    # Calculation of total fees when extra class taken
    totalamount1 = 6000 + 6000 + extraclassfee
    devidedtotalamount1 = totalamount1/2
    extratotaltowords = num2words(totalamount1)
    devidedextratotaltowords = num2words(devidedtotalamount1)
    # Calculation of deducted fees for extra class taken
    fixedclass = 24
    deficitclass = fixedclass-totalclass1
    deficitclassfee = deficitclass*500
    devideddeficitclassfee = deficitclassfee/2
    # Calculation of total fees for deficit class
    totalamount2 = 6000 + 6000 - deficitclassfee
    devidedtotalamount2 = totalamount2/2
    deficittotaltowords = num2words(totalamount2)
    devideddeficittotaltowords = num2words(devidedtotalamount2)


    if extraclass >= 0:
        return render(request,'bill.html',{
        'totalclass': totalclass1, 
        'currentmonth':currentmonth, 
        'previousmonth':previousmonth,
        'fixedclass':fixedclass,
        'extraclass':extraclass,
        'extraclassfee':extraclassfee,
        'devidedextraclassfee':devidedextraclassfee,
        'deficitclass':deficitclass,
        'deficitclassfee':'0',
        'devideddeficitclassfee':'0',
        'totalamount1':totalamount1,
        'totalamount2':0,
        'devidedtotalamount1':devidedtotalamount1,
        'extratotaltowords':extratotaltowords,
        'devidedextratotaltowords':devidedextratotaltowords
        

        })
    else:
        return render(request,'bill.html',{
        'totalclass': totalclass1, 
        'currentmonth':currentmonth, 
        'previousmonth':previousmonth,
        'fixedclass':fixedclass,
        'extraclass':extraclass,
        'extraclassfee':'0',
        'devidedextraclassfee':'0',
        'deficitclass':deficitclass,
        'deficitclassfee':deficitclassfee,
        'devideddeficitclassfee':devideddeficitclassfee,
        'totalamount2':totalamount2,
        'totalamount1': 0,       
        'devidedtotalamount2':devidedtotalamount2,
        'deficittotaltowords':deficittotaltowords,
        'devideddeficittotaltowords':devideddeficittotaltowords


        })
    
def showDelete(request,id):
    deleteclass = Tutor.objects.filter(id=id).delete()
    return redirect('table1')

def showEdit(request,id):
    editclass = Tutor.objects.filter(id=id).get()

    if request.method == 'POST':
        fm = TutorEditForm(request.POST,instance=editclass)
        if fm.is_valid():
            Tutor.objects.filter(id=id).update(
                classdate = fm.cleaned_data['classdate'],
                mode = fm.cleaned_data['mode'],
                classhour = fm.cleaned_data['classhour']
            )
        return redirect('table1')
    else:
        fm = TutorEditForm(instance=editclass)    
        return render(request,'edit.html',{'tutor':editclass,'form':fm})
    
def showHome(request):
    return render(request,'index.html')





    


