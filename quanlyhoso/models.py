from datetime import timedelta

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

# Create your models here.
class Hospital(models.Model):
    """docstring for Hospital"""
    name = models.CharField(max_length=200, unique=True, verbose_name = 'Tên bệnh viện')
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name='Địa chỉ')
    contact = models.CharField(max_length=300, blank=True, null=True, verbose_name='Liên hệ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "bệnh viện"
        verbose_name_plural = "bệnh viện"

class Employer(models.Model):
    """docstring for Employer"""
    name = models.CharField(max_length=200, unique=True, verbose_name = _('Employer Name'))
    phone = models.CharField(max_length=12, unique=True, verbose_name = _('Phone'))
    phone2 = models.CharField(max_length=12, unique=True, blank=True, null=True,
                              verbose_name = _('Phone 2'))
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name='Địa chỉ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "người môi giới"
        verbose_name_plural = "người môi giới"

class Profile(models.Model):
    """docstring for Profile"""
    IN_PROGRESS = 0
    GOOD = 1
    NOT_GOOD = 2
    BAD = 3
    RESULTS = (
        (IN_PROGRESS, 'Chưa có'),
        (GOOD, 'Đạt'),
        (NOT_GOOD, 'Có vấn đề'),
        (BAD, 'Loại'),
    )
    WORKDAYS_TO_DEADLINE = 3
    days_to_deadline = WORKDAYS_TO_DEADLINE
    today = now().date()
    for x in range(WORKDAYS_TO_DEADLINE):
        check_day = today + timedelta(days=x)
        if check_day.weekday() in (5,6):
            days_to_deadline +=1
    default_deadline = today + timedelta(days=days_to_deadline)


    name = models.CharField(max_length=200, unique=True, verbose_name = _('Labor Name'))
    year_of_birth = models.PositiveSmallIntegerField(
                        validators=[MinValueValidator(1900), MaxValueValidator(2018)],
                        verbose_name='Năm sinh')
    id_card_number = models.CharField(max_length=12, verbose_name=_("ID Card Number"))
    action_date = models.DateField(default=today, verbose_name='Ngày khám')
    hospital = models.ForeignKey('Hospital', on_delete=models.PROTECT,
                                 verbose_name = 'Bệnh viện')
    employer = models.ForeignKey('Employer', on_delete=models.PROTECT,
                                 verbose_name='Người môi giới')
    phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Số điện thoại')
    result = models.PositiveSmallIntegerField(choices=RESULTS, default=IN_PROGRESS, verbose_name='Kết quả')
    deadline = models.DateField(default=default_deadline, verbose_name='Hạn trả kết quả')
    is_returned = models.BooleanField(default=False, verbose_name='Trả kết quả')
    note = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ghi chú')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def colored_result(self):
        if self.result == self.BAD:
            return format_html(
                '<span style="color: #{};">{}</span>',
                'C70039',
                self.RESULTS[self.result][1],
            )
        if self.result == self.NOT_GOOD:
            return format_html(
                '<span style="color: #{};">{}</span>',
                'FFC300',
                self.RESULTS[self.result][1],
            )
        if self.result == self.GOOD:
            return format_html(
                '<span style="color: #{};">{}</span>',
                '5EFF33',
                self.RESULTS[self.result][1],
            )
        return self.RESULTS[self.result][1]


    colored_result.admin_order_field = 'result'
    colored_result.short_description = 'Kết quả'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "người khám"
        verbose_name_plural = "người khám"
        
        
        