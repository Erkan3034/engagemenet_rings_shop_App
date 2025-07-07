# Engagement Rings App - Render.com Deployment Guide

This guide will help you deploy the Engagement Rings Django application to Render.com.

## Prerequisites

1. A Render.com account (free tier available)
2. Your code pushed to a Git repository (GitHub, GitLab, etc.)

## Files Added for Deployment

- `requirements.txt` - Updated with production dependencies
- `build.sh` - Build script for Render
- `render.yaml` - Render configuration file
- `env_example.txt` - Environment variables template
- Updated `settings.py` - Production-ready Django settings

## Deployment Steps

### Option 1: Using render.yaml (Recommended)

1. **Push your code to a Git repository**
   ```bash
   git add .
   git commit -m "Ready for Render deployment"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [render.com](https://render.com)
   - Sign in and click "New +"
   - Select "Blueprint"
   - Connect your repository
   - Render will automatically detect the `render.yaml` file

3. **The deployment will automatically**:
   - Create a PostgreSQL database
   - Set up environment variables
   - Build and deploy your app

### Option 2: Manual Setup

1. **Create a new Web Service**
   - Go to Render Dashboard
   - Click "New +" → "Web Service"
   - Connect your repository

2. **Configure the service**:
   - **Name**: `engagement-rings-app`
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn engagement_rings_backend.wsgi:application`

3. **Create a PostgreSQL Database**
   - Click "New +" → "PostgreSQL"
   - Choose a name: `engagement-rings-db`
   - Select Free tier

4. **Set Environment Variables**
   In your web service settings, add these environment variables:
   ```
   SECRET_KEY=<generate-a-strong-secret-key>
   DEBUG=False
   DATABASE_URL=<will-be-provided-by-render-database>
   DJANGO_SUPERUSER_USERNAME=admin
   DJANGO_SUPERUSER_EMAIL=admin@rings.com
   DJANGO_SUPERUSER_PASSWORD=<secure-password>
   ```

## Important Notes

### Security
- Never commit real `.env` files to your repository
- Use Render's environment variables for sensitive data
- The app is configured with production security settings

### Database
- The app will automatically switch to PostgreSQL when `DATABASE_URL` is present
- Initial data will be loaded from `products.json` during build
- Migrations will run automatically

### Static Files
- Static files are handled by WhiteNoise
- CSS, JavaScript, and images will be served efficiently

### Admin Access
- A superuser will be created automatically if environment variables are set
- Access admin at: `https://your-app-name.onrender.com/admin/`

## Generated Secret Key

Generate a new Django secret key for production:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Troubleshooting

### Build Failures
- Check the build logs in Render dashboard
- Ensure all dependencies are in `requirements.txt`
- Verify `build.sh` permissions (handled automatically by Render)

### Database Issues
- Ensure `DATABASE_URL` environment variable is set
- Check PostgreSQL database connection in Render dashboard

### Static Files Not Loading
- Verify `STATIC_ROOT` and `STATICFILES_DIRS` in settings
- Check WhiteNoise configuration
- Run `python manage.py collectstatic` locally to test

## Post-Deployment

1. **Test the application**
   - Visit your Render URL
   - Check all pages load correctly
   - Test the admin interface

2. **Monitor logs**
   - Use Render dashboard to monitor application logs
   - Set up log alerts if needed

## Support

If you encounter issues:
1. Check Render documentation: https://render.com/docs
2. Review Django deployment guide: https://docs.djangoproject.com/en/stable/howto/deployment/
3. Check application logs in Render dashboard

## Cost

- Web Service: Free tier available (with limitations)
- PostgreSQL: Free tier available (90 days, then paid)
- Consider upgrading for production workloads 