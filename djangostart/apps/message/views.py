from django.shortcuts import render
from .models import UserMessage


def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name='石敢当')
    if all_messages:
        message = all_messages[0]




    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     email = request.POST.get('email', '')
    #     object_id = request.POST.get('object_id', '')
    #     address = request.POST.get('address', '')
    #
    #     user_messages = UserMessage()
    #     user_messages.name = name
    #     user_messages.message = message
    #     user_messages.email = email
    #     user_messages.object_id = object_id
    #     user_messages.address = address
    #     user_messages.save()

    return render(request, 'message_form.html',{'my_message': message})