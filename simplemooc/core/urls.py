from django.conf.urls import patterns, include, url

urlpatterns = patterns('simplemooc.core',
    #OBS - no django existe a funcaoa patterns que tem um prefixo vazio o que 
    #podemos organizar nossa urls
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
    
)