from django.db import models

class Album(models.Model):
	title = models.CharField("Название альбома", max_length=100)
	slug = models.SlugField("Ссылка для альбома", max_length=100, unique=True)
	img = models.ImageField("Изображение альбома", upload_to='images',
	help_text='Размер изображения 200px на 200px')
	class Meta:
		ordering = ['title']
		verbose_name = 'Альбом'
		verbose_name_plural = 'Альбомы'
	def __unicode__(self):
		return self.title

	@classmethod
	def get_all(cls):
		return cls.objects.all()

class Photo(models.Model):
	title = models.CharField("Название фотографии", max_length=100)
	album = models.ForeignKey(Album, verbose_name='Альбом')
	img = models.ImageField("Фото", upload_to='images',
	help_text='lololo')
	class Meta:
		ordering = ['title']
		verbose_name = 'Фото'
		verbose_name_plural = "Фотографии"
	def __unicode__(self):
		return self.title
