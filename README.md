# Financy, The Personal Finance Tracker

## Overview
The **Personal Finance Tracker, Financy** is a web-based application designed to help users manage their finances efficiently. Built using Django framework, the app allows users to track their income and expenses, visualize their financial data through interactive charts, and gain insights into their spending habits. The project aims to promote better financial planning and decision-making by providing a simple, intuitive, and user-friendly interface.

This application supports essential functionalities such as creating, viewing, updating, and deleting (CRUD) financial transactions, categorizing expenses, and generating insights using dynamic visualizations. The app is responsive, ensuring a seamless experience on both desktop and mobile devices.

---

## Features
1. **User Authentication**:
   - Secure login and signup system using Django’s authentication framework.
   - Personalized user sessions to ensure data privacy.

2. **Transaction Management**:
   - CRUD functionality for recording income and expenses.
   - Support for categorizing transactions into predefined categories such as "Food & Dining", "Transportation", and more.

3. **Charts and Insights**:
   - Line chart to track portfolio value over time.
   - Pie chart displaying expense distribution by category.
   - Bar chart comparing monthly income versus expenses.

4. **Responsive Design**:
   - Optimized for desktop and mobile browsers.

---

## File Structure
Below is a description of the primary files and their purpose in the project, which is mostly the default structure defined by Django:

### **1. `dashboard/`**
This directory contains the main Django app for the project.

- **`models.py`**:
  Defines the `Transaction` model, which includes fields for user, date, type (income or expense), amount, category, and description. It also includes `CATEGORY_CHOICES` and `TYPE_CHOICES` for categorization.
  The `User` model used in this app is a subclass of the `AbstractUser` model, which is the standard model defined by Django.

- **`views.py`**:
  Contains the logic for handling user requests, including:
  - Creating a user account, login and logout.
  - CRUD operations for transactions.
  - APIs for fetching data for the charts (e.g., portfolio value, expense categories).

- **`utils.py`**:
  Contains the logic for processing transaction data into lists (arrays) of data points, which can be used and visualized by the ApexCharts API on the frontend.

- **`urls.py`**:
  Defines URL patterns for accessing various views and API endpoints in the application.

- **`templates/`**:
  Contains the HTML files rendered by Django views, including:
  - `layout.html`: The main layout shared by all pages.
  - `index.html`: The homepage and dashboard for the app.
  - `transactions.html`: The tarnsactions page for adding and editing the user transactions, which are displayed as a paginated list.
  - `login.html` and `register.html`: The authentication pages.

- **`static/`**:
  Includes static assets such as CSS, JavaScript, and images used by the frontend.

### **2. `financy/`**
The Django project configuration directory.

- **`settings.py`**:
  Configures the project, including database connections, installed apps, middleware, and static file handling.

- **`urls.py`**:
  Routes project-level URLs to the app-specific URLs.

- **`wsgi.py` and `asgi.py`**:
  Provide entry points for the web server.

### **3. `README.md`**
The current file. Provides a comprehensive overview of the project.

### **4. `requirements.txt`**
Lists the Python dependencies required to run the project. Use `pip install -r requirements.txt` to set up the environment.

### **5. `manage.py`**
The entry point for running Django commands, such as starting the development server, running migrations, or creating superusers.

---

## Design Choices
### **Database Design**
The `Transaction` model was designed with simplicity and scalability in mind:
- A `category` field allows categorization of expenses for detailed analysis.
- A `type` field distinguishes between income and expenses.
- Using `ForeignKey` for `user` ensures multi-transaction support for each user.

### **Charting Library**
[ApexCharts](https://apexcharts.com/) was chosen for visualizing financial data due to its simplicity, interactivity, and rich feature set. The library allows responsive designs and dynamic updates, making it ideal for both desktop and mobile users.

### **Frontend Framework**
The app uses plain HTML/CSS with Bootstrap for styling. This ensures responsiveness without introducing unnecessary complexity.

### **Key Debates**
1. **Using Predefined vs. User-Defined Categories**:
   - Predefined categories were chosen to simplify the user experience and avoid clutter in visualizations. However, allowing user-defined categories is a potential enhancement.
   
2. **Expense Aggregation Logic**:
   - Aggregating transactions directly in the database using Django's ORM was chosen over Python-based aggregation for better performance and scalability.

3. **Authentication Implementation**:
   - Django's built-in authentication framework was used for simplicity and security, avoiding the need to implement custom solutions.

---

## Setup Instructions

Follow these steps to set up and run the Personal Finance Tracker:

1. **Clone the Repository**:
   Create a new folder and clone the project repository from GitHub to your local machine:
   ```
   git clone <repository_url>
   cd financy
   ```

2. **Install Dependencies**:
   Make sure you have Python and pip installed. Create a local vertual environment for example using the python venv module.
    ```
    python -m venv .venv
    ```
    Make sure to activate the VE befor installing any dependencies. To activate it on       Windows PowerShell:
    ```
    .venv\Scripts\Activate.ps1
    ```
    and on Linux/MacOS:
    ```
    .venv/bin/activate
    ```

    Finally install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
    Installing the the ApexCharts library separately is **not required**, as it is included directly via a script tag in the template.

  
3. **Set Up the Database**:
   Apply the database migrations to create the necessary tables:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser (Optional)**:
   Create a superuser account to access the admin panel:
   ```
   python manage.py createsuperuser

5. **Run the Development Server**:
   Start the development server to run the application:
   ```
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your web browser and navigate to the following URL:
   http://127.0.0.1:8000
    
    For accessing the django admin page navigate to: _root-URL/admin_. For exapmle when running on the development server: http://127.0.0.1:8000/admin

You can now use the Personal Finance Tracker to manage your transactions and view insights into your financial data.

---

## Conclusion
The Personal Finance Tracker empowers users to take control of their finances through a clean, user-friendly interface and insightful visualizations. While the project focuses on simplicity, it lays a strong foundation for future enhancements like budgeting and recurring transactions.