# vendor-management
A Simple Vendor Management System

# Summary

This is a Vendor Management project built using Django and Django REST Framework. It includes features such as managing vendor profiles, purchase orders, and historical performance metrics.

# Features

* Vendor Profiles:** Stores essential information about each vendor, including performance metrics.
* Purchase Orders:** Stores details of each purchase order and calculate various performance metrics.
* Historical Performance:** Optionally store historical data on vendor performance for analysis

# Project Structure

The project consists of the following Django apps:

* vendor: This app contains models for Vendor, PurchaseOrder, and HistoricalPerformance.

# Setup Instructions

# STEP 1
Create a folder of your choice, open terminal with path of the folder and clone the repository `git clone <repository-url>`

# STEP 2
Create a virtual env and activate the environment and do a `cd managementSystem`

# STEP 3
Run the command `pip install -r requirements.txt`

# STEP 4
Apply database migrations using following commands

`python manage.py makemigrations`
`python manage.py migrate`

# STEP 5
Create a super user to use Django admin using `python manage.py createsuperuser`

# STEP 6
Run the development server using `python manage.py runserver`

# STEP 7
Access the Django admin at `http://localhost:8000/admin/` OR `http://127.0.0.1:8000/admin/` to manage vendors, purchase orders, and historical performance.

# STEP 8
Access the API at `http://localhost:8000/api/` or `http://127.0.0.1:8000/api/` for CRUD operations on vendors, purchase orders, and historical performance.

## API Endpoints

- `/api/token/` : To obtain acess token for user
- `api/token/refresh/` : To get new access token using refresh token
- `/api/vendors/`: List and create vendor profiles.
- `/api/purchase-orders/`: List and create purchase orders.
- `api/vendors/<int:po_id>/performance`: Retrieve and update historical performance for a vendor.
- `api/purchase_orders/<int:po_id>/acknowledge` : To acknowledge a purchase order and mark it as deliverd

