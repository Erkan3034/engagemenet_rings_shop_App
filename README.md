# Engagement Rings Collection - Django E-commerce Application

A modern e-commerce web application for engagement rings, built with Django framework and featuring beautiful, responsive design.

## 🚀 Features

### Frontend Features
- **Modern & Responsive Design**: Mobile-friendly design with Bootstrap 5 and custom CSS
- **Beautiful Typography**: Consistent Avenir/Montserrat font family throughout the application
- **Product Gallery**: Product viewing with different color options and image galleries
- **Advanced Filtering**: Filter by popularity, weight, color and search functionality
- **Sorting Options**: Sort by popularity, name, and weight
- **Product Detail Pages**: Comprehensive product information with image carousels
- **Smooth Animations**: Hover effects, transitions, and interactive elements
- **Complete Navigation**: Home, Products, About, and Contact pages

### Backend Features
- **RESTful API**: Django REST Framework with comprehensive API endpoints
- **Database Management**: SQLite for development, PostgreSQL for production
- **Admin Panel**: Django admin interface for product management
- **Advanced Filtering**: Server-side filtering and search system
- **JSON Data Loading**: Management commands for data import
- **Production Ready**: Configured for deployment with security settings

### Pages
- **Home Page**: Hero section with featured products
- **Products List**: Complete product catalog with filtering and sorting
- **Product Detail**: Individual product pages with galleries and specifications
- **About Page**: Company information, story, values, and team
- **Contact Page**: Contact information, form, FAQ, and working hours

## 🛠️ Technologies

- **Backend**: Django 5.2, Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Deployment**: Render.com ready with Gunicorn and WhiteNoise
- **Icons**: Font Awesome 6
- **Additional Packages**: 
  - django-cors-headers
  - django-filter
  - python-dotenv
  - gunicorn
  - psycopg2-binary
  - whitenoise
  - dj-database-url

## 📦 Installation

### Requirements
- Python 3.8+
- pip

### Step by Step Installation

1. **Clone the project**
```bash
git clone <repository-url>
cd engagement-rings-app
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create database**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Load product data**
```bash
python manage.py load_products
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Start the server**
```bash
python manage.py runserver
```

## 🌐 Usage

### Main Pages
- **Home Page**: `http://localhost:8000/`
- **Products List**: `http://localhost:8000/products/`
- **Product Detail**: `http://localhost:8000/products/{id}/`
- **About Page**: `http://localhost:8000/about/`
- **Contact Page**: `http://localhost:8000/contact/`
- **Admin Panel**: `http://localhost:8000/admin/`

### API Endpoints
- **All Products**: `GET /api/products/`
- **Product Detail**: `GET /api/products/{id}/`
- **Product Images**: `GET /api/products/{id}/images/`
- **Contact** : `GET /api/contact/`
- **About** : `GET /api/about/`

### Filtering Parameters
- `search`: Search in product names
- `min_popularity` / `max_popularity`: Popularity score range
- `min_weight` / `max_weight`: Weight range
- `color`: Color filter (white, yellow, rose)
- `ordering`: Sort by (name, -name, weight, -weight, -popularity_score)

## 📁 Project Structure

```
engagement-rings-app/
├── engagement_rings_backend/    # Main Django project
│   ├── settings.py             # Django settings (production-ready)
│   ├── urls.py                 # URL configuration
│   └── wsgi.py                 # WSGI configuration
├── products/                    # Product application
│   ├── models.py               # Product model
│   ├── views.py                # API views
│   ├── serializers.py          # API serializers
│   ├── admin.py                # Admin panel
│   └── management/             # Management commands
├── frontend/                   # Frontend application
│   ├── views.py                # Template views
│   └── urls.py                 # URL patterns
├── templates/                  # HTML templates
│   ├── base.html              # Base template
│   └── frontend/              # Frontend templates
│       ├── home.html          # Home page
│       ├── products_list.html # Products listing
│       ├── product_detail.html# Product detail
│       ├── about.html         # About page
│       └── contact.html       # Contact page
├── static/                     # Static files
│   ├── css/                   # CSS files
│   └── js/                    # JavaScript files
├── build.sh                   # Render build script
├── render.yaml                # Render deployment config
├── env_example.txt            # Environment variables example
├── manage.py                  # Django management
├── products.json              # Product data
└── README.md                  # This file
```

## 🚀 Production Deployment

### Render.com Deployment (Recommended)

This application is ready for deployment on Render.com with all necessary configurations:

1. **Push to Git repository**
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

2. **Deploy on Render**
- Go to [render.com](https://render.com)
- Click "New +" → "Blueprint"
- Connect your repository
- Render will auto-detect `render.yaml`

3. **Automatic Setup**
- PostgreSQL database creation
- Environment variables configuration
- Static files handling with WhiteNoise
- Superuser creation
- Product data loading

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@rings.com
DJANGO_SUPERUSER_PASSWORD=secure-password
```

## 🎨 Customization

### CSS Customization
Main CSS file: `static/css/style.css`
- Consistent Avenir/Montserrat typography
- Responsive design with multiple breakpoints
- Modern animations and effects

### JavaScript Customization
Main JS file: `static/js/main.js`
- Product filtering and sorting
- Image gallery functionality
- Form handling

### Template Customization
Edit HTML files in the templates folder for layout changes.

## 🔧 Management Commands

### Load Product Data
```bash
python manage.py load_products
```

### Database Backup
```bash
python manage.py dumpdata products > products_backup.json
```

### Database Restore
```bash
python manage.py loaddata products_backup.json
```

### Collect Static Files
```bash
python manage.py collectstatic
```

## 🛡️ Security Features

- Production-ready Django settings
- HTTPS enforcement in production
- Secure cookie settings
- CORS configuration
- SQL injection protection
- XSS protection headers

## 🎯 Performance Features

- WhiteNoise for efficient static file serving
- Compressed static files in production
- Database query optimization
- Responsive image loading
- Caching configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👨‍💻 Developer

**Erkan Turgut**
- Email: turguterkan1306@gmail.com
- GitHub: [@Erkan3034](https://github.com/Erkan3034)
- Portflyo: [Erkan Turgut](https://erkanturgut.netlify.app)

##  Acknowledgments

- Django team for the excellent framework
- Bootstrap team for responsive design components
- Font Awesome team for beautiful icons
- Render.com for easy deployment platform 