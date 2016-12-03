from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from datetime import datetime
from ipware.ip import get_ip

from .models import Choice, Question, UserAction


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class UserOptionView(generic.ListView):
	model = UserAction
	template_name = 'polls/userOption.html'

class NewAccountView(generic.ListView):
	model = UserAction
	template_name = 'polls/newAccount.html'

class AccountView(generic.ListView):
	model = UserAction	
	template_name = 'polls/account.html'

class PaymentView(generic.ListView):
	model = UserAction
	template_name = 'polls/payment.html'

class ReceiptView(generic.ListView):
	model = UserAction
	template_name = 'polls/receipt.html'

class ApprovalView(generic.ListView):
	model = UserAction
	template_name = 'polls/approval.html'

class DoneView(generic.ListView):
	model = UserAction
	template_name = 'polls/done.html'

def SaveAction(request):
	user_action = UserAction(ip_address = get_ip(request), action_date = datetime.now(), action_object = 'My Account button', action = 'button press') 	
 	user_action.save()
 	return HttpResponseRedirect(reverse('polls:newAccount'))


def SaveOption(request):
	user_action = UserAction(ip_address = get_ip(request), action_date = datetime.now(), action_object = request.POST['option'] + ' button', action = 'button press')
	user_action.save()
	return HttpResponseRedirect(reverse('polls:index'))