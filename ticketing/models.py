from django.db import models


class Movie(models.Model):
    # movie model

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField('نام فیلم', max_length=100)
    director = models.CharField('کارگردان', max_length=50)
    cover = models.ImageField('عکس', upload_to='Movie_Covers/', null=False, blank=False)
    length = models.IntegerField('مدت فیلم')
    year = models.IntegerField('سال ساخت')
    description = models.TextField('توضیحات')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    # Cinema model

    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    name = models.CharField('نام سینما', max_length=50)
    capacity = models.IntegerField('ظرفیت سینما')
    city = models.CharField('شهر', max_length=50, default='تهران')
    phone = models.CharField('شماره تماس', max_length=20, null=True)
    image = models.ImageField('عکس', upload_to='Cinema_Images/', null=True, blank=True)
    address = models.TextField('آدرس')

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    # showtime model

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name='فیلم')
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, verbose_name='سینما')

    start_time = models.DateTimeField('زمان شروع سانس')
    price = models.IntegerField('قیمت')
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

    status = models.IntegerField('وضعیت', choices=status_choices, default=status_choices)

    def __str__(self):
        return '{}-{}-{}'.format(self.movie.name, self.cinema.name, self.start_time)

    def reserve_seats(self, person_count):
        assert isinstance(person_count, int) and person_count > 0, 'Number of seats should be a positive integer'
        assert self.status == ShowTime.sale_start, 'Sale is not open'
        assert self.free_seats >= person_count, 'Not enough free seats'
        self.free_seats -= person_count
        if self.free_seats == 0:
            self.status = ShowTime.tickets_finished
        self.save()


class Ticket(models.Model):
    class Meta:
        verbose_name = 'بلیت'
        verbose_name_plural = 'بلیت'

    customer = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, verbose_name='کاربر')
    showtime = models.ForeignKey('ShowTime', on_delete=models.PROTECT, verbose_name='سانس')
    buy_time = models.DateTimeField('زمان خرید بلیت', auto_now_add=True)
    person_count = models.IntegerField('تعداد نفرات')

    def __str__(self):
        return '{}-{}-{}-{}'.format(self.showtime.movie, self.showtime, self.person_count, self.customer)


class News(models.Model):
    # news model

    class Meta:
        verbose_name = 'خبر'
        verbose_name_plural = 'خبر'

    news_id = models.AutoField(primary_key=True, verbose_name='کد خبر')
    title = models.CharField('عنوان خبر', max_length=100)
    subject = models.CharField('موضوع خبر', max_length=50)
    image = models.ImageField('عکس', upload_to='News_Images/', null=False, blank=False)
    time = models.DateTimeField('زمان خبر')
    text = models.TextField('متن خبر')

    def __str__(self):
        return self.title
