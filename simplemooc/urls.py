from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#OBS - podemos criar varias urls pra N modulos de um aplicação r'^' caminho do modulo da url
	#O django deixa colocar prefixos nos endereço da urls ex: r'^nome_modulo/' 
	#o namespace e muito utilizado pra podemos utilizar urls com nome iguais
    url(r'^', include('simplemooc.core.urls',namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
