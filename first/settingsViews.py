from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm,TransactionForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm,EmployeeForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department,Employee
from fpdf import FPDF
from .models import Transaction
from django.urls import path,include

departments = Employees.objects.all()
managers = Manager.objects.all()
commision_saralies =  Commision_saraly.objects.all()
fixed_salaries = Fixed_saraly.objects.all()
allowanceses = allowances.objects.all()
deduction = deductions.objects.all()
salary_detail = salary_details.objects.all()
job_types = job_type.objects.all()
commission_template = commission_templates.objects.all()
manageSalaries =  ManageSalary.objects.all()
SelectDepartments = SelectDepartment.objects.all()
PayrollSummaries =  PayrollSummary.objects.all()
advanceSalaries =  AdvanceSalary.objects.all()
departments = Department.objects.all()
dailyWorks = DailyWork.objects.all()
first_departments = first_department.objects.all()
employees = Employees.objects.all()
context = {
        'employees' : employees,
        'departments' : departments,
        'managers' : managers,
        'commision_saralies' : commision_saralies,
        'fixed_salaries' :  fixed_salaries,
        'allowanceses' :  allowanceses,
        ' deductions' :  deduction,
        'salary_details' : salary_detail,
        'job_types' : job_types,
        'commission_templates' : commission_template,
        'manageSalaries ' :  manageSalaries,
        'SelectDepartments' :  SelectDepartments,
        'PayrollSummaries' : PayrollSummaries,
        'advanceSalaries' : advanceSalaries,
        'dailyWorks ' :  dailyWorks,
        'first_departments' :  first_departments  
        }
       

def settings(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ManagerForm()
        context = {
            'form' : form
        }
    return render(request, 'Dashboard/settings.html', context)

def company_account(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/balanceSheet')
    else:
        form = TransactionForm()
        context = {
            'form' : form
        }
    return render(request, 'Dashboard/company_account.html', context)

def company_account_deleteAll(request):
    if request.method == 'POST':
        Transaction.objects.all().delete()
        return redirect('/home')
    return render(request, 'Dashboard/company_account.html')
    