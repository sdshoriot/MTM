from django.shortcuts import render
from django.shortcuts import get_object_or_404

from home.models import *
from notice.models import Notice


def home(request):
	home = Home.objects.all()
	notices = Notice.objects.all().order_by('-date')[:4]
	facilities = Facility.objects.all()[:4]
	messages = Message.objects.all()[:3]
	feedbacks = Feedback.objects.all()[:4]
	ctx = {'home': home, 
		   'notices': notices,
		   'facilities': facilities,
		   'messages': messages,
		   'feedbacks': feedbacks,
		   }
	return render(request, 'theme/home/home.html', ctx)


def message_detail(request, pk):
	message = get_object_or_404(Message, pk=pk)
	ctx = {'message': message}
	return render(request, 'theme/home/message_detail.html', ctx)


def gallery(request):
    return render(request, 'theme/home/gallery.html')


def feedback(request):
    return render(request, 'theme/home/feedback.html')