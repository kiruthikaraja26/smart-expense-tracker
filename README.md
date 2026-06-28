# smart-expense-tracker
The Smart Expense Tracker is a Django-based web application that helps users efficiently manage their daily expenses. It provides a secure authentication system, allowing users to register, log in, and maintain their personal expense records.

The application follows the Model-View-Template (MVT) architecture of Django. User requests are routed through the URL configuration, processed by views, validated using forms, stored in the SQLite database through models, and finally displayed using HTML templates.
SMART_EXPENSE_TRACKER
│
├── manage.py
│   └── Django project management file
│
├── db.sqlite3
│   └── SQLite database
│
├── expense_tracker/
│   │
│   ├── settings.py
│   │   └── Project configuration
│   │
│   ├── urls.py
│   │   └── Main URL routing
│   │
│   └── __pycache__/
│       └── Python cache files
│
└── tracker/
    │
    ├── models.py
    │   └── Database models (Expense data)
    │
    ├── views.py
    │   └── Business logic & request handling
    │
    ├── forms.py
    │   └── User input forms
    │
    ├── urls.py
    │   └── App-specific URL routing
    │
    ├── templates/
    │   │
    │   ├── base.html
    │   │   └── Common layout
    │   │
    │   ├── register.html
    │   │   └── User Registration
    │   │
    │   ├── login.html
    │   │   └── User Login
    │   │
    │   ├── dashboard.html
    │   │   └── Expense Dashboard
    │   │
    │   └── add_expense.html
    │       └── Add New Expense
    │
    └── __pycache__/
        └── Python cache files
