from django.db import models

from django.core.validators import MinLengthValidator



# def validate_send_time(value):
#     if value:
#         # Get the current time in the specified time zone
#         tz = pytz.timezone(value)
#         now = datetime.datetime.now(tz)
#         # Check if the current time is outside the allowed range
#         if now.hour < 10 or now.hour >= 17:
#             raise ValidationError("Text messages can only be sent during the day (10AM to 5PM) in the specified time zone.")


class EmpAdress(models.Model):
   Type = {
      ("INDIA", "INDIA"),
    ("USA", "USA"),
   }
   Massage =models.TextField(max_length=160,blank=False,unique=True)
   Email=models.EmailField( max_length=25 ,unique=True)
   Phone=models.CharField(max_length=10)
   Country=models.CharField(max_length=50,choices=Type)
   Schedule_On= models.DateField(auto_created=True)



   

   Phone = models.CharField( max_length=10,
        validators=[
            MinLengthValidator(10, 'the field must contain at least 10 characters')
            ]
        )
    #     )
  # @classmethod
  # def valite_time(Schedule_on):
  #   if Schedule_on 
  
  
  #  time_zone = models.CharField(validators=[validate_send_time])
  
  
  
