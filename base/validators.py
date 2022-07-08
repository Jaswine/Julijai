from django.core.exceptions import ValidationError

def story_size(value):
    filesize = value.size
    if filesize>60000000:
        raise ValidationError('Допустимый размер 60мб, если вас это не устраивает напишите в поддержку')

def img__size(value):
    filesize = value.size
    if filesize>4000000:
        raise ValidationError('Допустимый размер 4мб, если вас это не устраивает напишите в поддержку')