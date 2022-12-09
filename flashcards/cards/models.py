from django.db import models

# Create your models here.
NUM_BOXES = 5
BOXES = range(1 , NUM_BOXES +1)

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    box = models.IntegerField(
            default=BOXES[0],
            choices=zip(BOXES , BOXES),
    )
    
    def __str__(self):
        return self.question
    
    def move(self,solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()
            
        return self #always when update an attribute we should retuen self 
        
    