from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Keyword logic
def predict_category(desc):
    desc = desc.lower()
    if "uber" in desc or "bus" in desc:
        return "Travel"
    elif "pizza" in desc or "food" in desc:
        return "Food"
    elif "shirt" in desc or "shopping" in desc:
        return "Shopping"
    else:
        return "Other"
@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)

    total = sum(exp.amount for exp in expenses)

    return render(request, 'dashboard.html', {
        'expenses': expenses,
        'total': total
    })


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user

            # Auto category
            expense.category = predict_category(expense.description)

            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})