from django.core.management.base import BaseCommand
from Remote_User.models import ClientRegister_Model


class Command(BaseCommand):
    help = 'Creates demo users for testing'

    def handle(self, *args, **options):
        # Create demo user 1
        user1, created1 = ClientRegister_Model.objects.get_or_create(
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
        
        # Create demo user 2
        user2, created2 = ClientRegister_Model.objects.get_or_create(
            username='testuser',
            defaults={
                'email': 'test@example.com',
                'password': 'test123',
                'phoneno': '9876543210',
                'country': 'USA',
                'state': 'New York',
                'city': 'New York City',
                'gender': 'Female',
                'address': '456 Test Avenue'
            }
        )
        
        self.stdout.write(self.style.SUCCESS('=' * 60))
        if created1:
            self.stdout.write(self.style.SUCCESS('✓ Demo User 1 created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('→ Demo User 1 already exists'))
            
        if created2:
            self.stdout.write(self.style.SUCCESS('✓ Demo User 2 created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('→ Demo User 2 already exists'))
            
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('\nDEMO CREDENTIALS:'))
        self.stdout.write(self.style.SUCCESS('-' * 60))
        self.stdout.write(self.style.SUCCESS('User 1:'))
        self.stdout.write(self.style.SUCCESS('  Username: demo'))
        self.stdout.write(self.style.SUCCESS('  Password: demo123'))
        self.stdout.write(self.style.SUCCESS('\nUser 2:'))
        self.stdout.write(self.style.SUCCESS('  Username: testuser'))
        self.stdout.write(self.style.SUCCESS('  Password: test123'))
        self.stdout.write(self.style.SUCCESS('-' * 60))
