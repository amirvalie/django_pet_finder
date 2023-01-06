from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class AdapterProfile(models.Model):
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

class AdapterInformation(models.Model):
    title=models.CharField(
        max_length=250
    )
    description=models.TextField(
        blank=True,
        null=True,
    )

class Input(models.Model):
    adapterinfo = models.OneToOneField(
        AdapterInformation,
        on_delete=models.CASCADE,
        null=True, related_name='input',
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
        ('MCSS' , 'Multiple Choice Single Select'),
        ('MCMS' , 'Multiple Choice Multi Select'),
        ('STVC' , 'Simple Threshold Value Comparision'),
        ('NA' , 'Numeric Answer'),
        ('UF' , 'Upload File'),
    ]
    input_type = models.CharField(
        max_length=12,
        choices = INPUT_TYPE_CHOICES,
        default='MCSS',
    )

    # def check_input_options(self,type_option,id):
    #     related_input=[
    #         self.mcss_input_options,
    #         self.ipip_input_options,
    #         self.mcms_input_options,
    #         self.stvc_input_options,
    #         self.cfda_input_options,
    #     ]
    #     input_type=['MCSS','IPIP','MCMS','STVC','CFDA' ,]
    #     for iter_input_type in range(len(input_type)):
    #         if type_option in input_type[iter_input_type]:
    #             try:
    #                 related_input[iter_input_type].get(id=int(id))
    #                 return True
    #             except:
    #                 return False
    #     else:
    #         return "input_type_error"

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











    
    
    
