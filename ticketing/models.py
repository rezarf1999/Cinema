from django.db import models


class Movie(models.Model):
    # movie model

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField('نام فیلم', max_length=100)
    director = models.CharField('کارگردان', max_length=50)
    cover = models.ImageField('عکس', upload_to='files/Movie_Covers', null=False, blank=False)
    length = models.IntegerField('مدت فیلم')
    year = models.IntegerField('سال ساخت')
    description = models.TextField('توضیحات')


class Cinema(models.Model):
    # Cinema model

    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    name = models.CharField('نام سینما', max_length=50)
    capacity = models.IntegerField('ظرفیت سینما')
    city = models.CharField('شهر', max_length=50, default='تهران')
    phone = models.CharField('شماره تماس', max_length=20, null=True)
    image = models.ImageField('عکس', upload_to='files/Cinema_Images', null=False, blank=False)
    address = models.TextField('آدرس')


class ShowTime(models.Model):
    # showtime model

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name='فیلم')
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, verbose_name='سینما')

    start_time = models.DateTimeField('زمان شروع سانس')
    price = models.IntegerField('قیمت')
    salable_seats = models.IntegerField('تعداد صندلی های قابل فروش')
    free_seats = models.IntegerField('تعداد صندلی های خالی')

    sale_start = 1
    sale_not_started = 2
    tickets_finished = 3
    show_canceled = 4
    movie_finished = 5
    sale_closed = 6
    status_choices = (
        (sale_start, 'فروش بلیت شروع شد'),
        (sale_not_started, 'فروش بلیت آغاز نشده'),
        (tickets_finished, 'بلیت ها تمام شدند'),
        (show_canceled, 'سانس لغو شد'),
        (movie_finished, 'فیلم تمام شد'),
        (sale_closed, 'فروش بلیت بسته شد'),
    )
    status = models.IntegerField('وضعیت', choices=status_choices, default=sale_not_started)
