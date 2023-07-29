from django.db import models

# Create your models here.
class xailox(models.Model):
    title = models.CharField('Заголовок',max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField('Цена',max_digits=12, decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Поставьте галочку, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'
    
    

    class Meta:
        db_table = 'xailox'
    
