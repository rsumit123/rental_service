# Rental Service

This project is a simple Vehicle Rental Service made in Django and Python.

## Dependencies

1. [Python 3.8](https://www.python.org/)
2. [Django 4.0](https://www.djangoproject.com/)
3. [Django Rest Framework](https://www.django-rest-framework.org/)
4. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
5. [Python Decouple](https://pypi.org/project/python-decouple/)
6. [PipEnv](https://pypi.org/project/pipenv/)

## Features

1. Add a Customer : Employees can add a new customer, if not already present,
   upon successful addition the page will redirect to customer list
2. Create a new Booking : A new booking can be made in the name of the
   customer.. If the inventory slots for the selected vehicle is full, customer
   has to select new vehicle or contact admin to increase inventory.

   `Note: The Booking Rental Date is automatically filled`

3. All Existing bookings, Inventory and customers can be viewed from View
   Bookings, View Inventory and View Customers pages

## Usage

1. Install Pipenv by running

   ```bash
   pip install pipenv
   ```

2. Clone/Fork this project and cd into the root folder
3. Enter the following commands to install the required dependencies.
   ```bash
   pipenv shell
   pipenv install
   ```
4. Start the Django development server by running
   ```bash
   python manage.py runserver
   ```
5. Navigate to `https://localhost:8000/home/` to use the app.

## Limitations

1. SQLITE3 is being used as a database, which is not recommended for production
   
2. Further Improvements in UI required, Currently only simple HTML and Bootstrap are used (Django Templates).
   
3. Add validators for various fields and add more robust checks.

4. This app is currently not deployed anywhere.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
