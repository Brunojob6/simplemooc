from django.db import models

class CoursesManager(models.Manager):

	def search(self, query):
		
		return self.get_queryset().filter(
			models.Q(name__icontains=query) |\
			models.Q(description__icontains=query)
			)

class Courses(models.Model):
	#tive que instalar um dependecia para biblioteca Pillow, no ubuntu  
	#sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

	name = models.CharField('Nome', max_length=100)	
	slug = models.SlugField('Atalho')	
	description = models.TextField('Descrição', blank=True)	
	start_date = models.DateField( 
		'Data de Início ', null=True, blank=True 
	)
	image = models.ImageField(
		upload_to='courses/images', verbose_name='Imagem',
		null=True, blank=True
	)

	create_at = models.DateTimeField(
		'Criado em', auto_now_add=True
	)
	update_at = models.DateTimeField('Atualizado em', auto_now=True)
		
	objects = CoursesManager()