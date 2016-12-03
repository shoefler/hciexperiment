from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/newAccount
    url(r'newAccount/$', views.NewAccountView.as_view(), name='newAccount'),
    # ex: /polls/account/
    url(r'account/$', views.AccountView.as_view(), name='account'),

    url(r'payment/$', views.PaymentView.as_view(), name='payment'),
    url(r'receipt/$', views.ReceiptView.as_view(), name='receipt'),
    url(r'approval/$', views.ApprovalView.as_view(), name='approval'),
    url(r'done/$', views.DoneView.as_view(), name='done'),
    #url(r'account/$', views.AccountView.as_view(), name='account'),
    #url(r'account/$', views.AccountView.as_view(), name='account'),
    #url(r'account/$', views.AccountView.as_view(), name='account'),



    # ex: /polls/saveAction/
    url(r'saveAction/$', views.SaveAction, name='saveAction'),

    url(r'saveOption/$', views.SaveOption, name='saveOption'),

    #url(r'myAccount/$', views.AccountView.as_view(), name='myAccount'),

    # ex: /polls/userOption/
    url(r'userOption/$', views.UserOptionView.as_view(), name='userOption'),

]