# Storefront

A Django-based web application for managing an online store.

## Features

- Product management
- User authentication
- Order processing
- Extensible architecture

## Requirements

- Python 3.8+
- Django 4.x

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mr-arashnm/StoreFront.git
   cd storefront
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the app:**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Development

- To create a superuser for admin access:
  ```bash
  python manage.py createsuperuser
  ```

- Static and media files are managed via Django's built-in mechanisms.

## Testing

Run tests with:
```bash
python manage.py test
```

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

For more details, see the Django documentation: https://docs.djangoproject.com/
