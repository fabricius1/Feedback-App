from ninja import NinjaAPI, ModelSchema
from .models import Feedback


class FeedbackSchema(ModelSchema): 
    class Config:
        model = Feedback
        model_fields = ['type', 'comment', 'screenshot']
    
    
api = NinjaAPI()


@api.post('feedbacks/')
def feedbacks(request, feedback: FeedbackSchema):
    new_feedback = Feedback.objects.create(
        **feedback.dict()
    )
    new_feedback.save()
    return "Ok"
    
