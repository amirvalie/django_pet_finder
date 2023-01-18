from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class AdopterProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField(
        max_length=30,
    )
    last_name=models.CharField(
        max_length=30,
    )
    phone_number=models.CharField(
        max_length=11,
    )
    state=models.CharField(
        max_length=30,
    )
    city=models.CharField(
        max_length=30,
    )
    zip_code=models.CharField(
        max_length=10,
    )
    address=models.TextField()

class AdopterInformation(models.Model):
    title=models.CharField(
        max_length=250
    )
    description=models.TextField(
        blank=True,
        null=True,
    )

class Input(models.Model):
    adapterinfo = models.ForeignKey(
        AdopterInformation,
        on_delete=models.CASCADE,
        related_name='input',
    )
    title = models.CharField(
        max_length=150,
        default='',
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    prompt_text = models.TextField(
        blank=True,
        null=True,
    )
    INPUT_TYPE_CHOICES = [
        ('mcss_input_options' , 'Multiple Choice Single Select'),
        ('mcms_input_options' , 'Multiple Choice Multi Select'),
        ('stvc_input_options' , 'Simple Threshold Value Comparision'),
        ('na_input_options' , 'Numeric Answer'),
        ('uf_input_options' , 'Upload File'),
    ]
    input_type = models.CharField(
        max_length=50,
        choices = INPUT_TYPE_CHOICES,
        default='mcss_input_options',
    )
    active_input=models.BooleanField(default=True)

class BaseMultipleChoise(models.Model):
    value=models.CharField(
        max_length=250,
    )
    checked=models.BooleanField(
        default=False,
    )

    class Meta:
        abstract=True

class MCSSInputOption(BaseMultipleChoise):
    input = models.ForeignKey(
        'Input',
        on_delete=models.CASCADE,
        related_name='mcss_input_options'
    )

class MCMSInputOption(models.Model):
    input = models.ForeignKey(
        'Input',
        on_delete=models.CASCADE,
        related_name='mcms_input_options'
    )

class UFInputOption(models.Model):
    input = models.ForeignKey(
        'Input',
        on_delete=models.CASCADE,
        related_name='uf_input_options'
    )
    file = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True,
    )

class NAInputOption(models.Model):
    input = models.ForeignKey(
        'Input',
        on_delete=models.CASCADE,
        related_name='na_input_options'
    )
    key = models.IntegerField(        
        blank=True,
        null=True,
    )

class STVCInputOption(models.Model):
    input = models.ForeignKey(
        'Input',
        on_delete=models.CASCADE,
        related_name='stvc_input_options'
    )
    range_max = models.FloatField(
        blank=True,
        null=True,
    )
    range_min = models.FloatField(
        blank=True,
        null=True,
    )    











    
    
    
