import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'content_detection.settings')
django.setup()

from Remote_User.models import ClientRegister_Model

# Create demo user
demo_user, created = ClientRegister_Model.objects.get_or_create(
    username='demo',
    defaults={
        'email': 'demo@example.com',
        'password': 'demo123',
        'phoneno': '1234567890',
        'country': 'USA',
        'state': 'California',
        'city': 'Los Angeles',
        'gender': 'Male',
        'address': '123 Demo Street'
    }
)

if created:
    print("✓ Demo user created successfully!")
else:
    print("✓ Demo user already exists!")

print("\n" + "="*50)
print("DEMO USER CREDENTIALS:")
print("="*50)
print("Username: demo")
print("Password: demo123")
print("="*50)
