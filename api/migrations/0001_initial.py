from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="nadeem", 
                          email="ahmedinadeem99@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="9820889475",
                          gender="Male"
                          )
        user.set_password("nad.don.24463")
        user.save()
    
    dependencies = [

    ]
    operations = [
        migrations.RunPython(seed_data),
    ]