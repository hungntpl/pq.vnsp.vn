
from django.core.management.base import BaseCommand, CommandError
from sa.models import sa 
from cs.models import cs 
from django.core.mail import send_mail
# import datetime
from datetime import datetime
from datetime import date
from django.urls import reverse
from set.models import EmailReport
from django.utils import timezone

# from django.contrib.sites.shortcuts import build_absolute_uri
# from django.contrib.sites.models import Site

class Command(BaseCommand):
    help = 'The SA`s deadline has passed notification'

    def handle(self, *args, **options):
#        
        today = timezone.localdate()
        start_date = timezone.datetime(2023, 5, 20).date()

        # Convert start_date to a timezone-aware datetime
        start_date = timezone.make_aware(timezone.datetime.combine(start_date, timezone.datetime.min.time()))

        # cs_list_sa_null = cs.objects.filter(DLine__lt=today, DLine__gt=start_date, SANo__isnull=True or SANo__exact='').order_by('-CSNo')

        cs_list_sa_null = cs.objects.filter(DLine__lt=today, DLine__gt=start_date, SANo__isnull=True).order_by('-CSNo')

        sa_not_approved = sa.objects.filter(SAApp__isnull=True)

        cs_list_sa_not_approved = cs.objects.filter(DLine__lt=today, DLine__gt=start_date, SANo__isnull=False, SANo__in=sa_not_approved).order_by('-CSNo')


        # cs_list = cs.objects.filter(DLine__lt=today, DLine__gt=start_date, SANo__isnull=False, ).order_by('-CSNo')

        

        # dobemp_list = temp_list.exclude(wstatus = "Q")
        final_list_null = ''
        final_list_not_null =''

        for index, item in enumerate(cs_list_sa_null, start=1):
        # for item in cs_list_sa_null:
            url = item.get_absolute_url()
            final_list_null += f"{index}. {item.CSNo} - {item.DLine}:     http://pq.vnsp.vn{url}\n\n"

        for index, item in enumerate(cs_list_sa_not_approved, start=1):
        # for item in cs_list_sa_not_approved:
            url = item.get_absolute_url()
            final_list_not_null += f"{item.CSNo} - {item.DLine}:     http://pq.vnsp.vn{url}\n\n"

        # url = reverse('cs-update', kwargs={'pk': item.CSNo})
        # # final_list = final_list + str(item.CSNo) + ':' + request.build_absolute_uri(url) + '\n'
        # final_list = final_list + str(item.CSNo) + ':' + str(item.get_absolute_url()) + '\n'
        message = 'Danh sách CS đã quá deadline: ' + '\n \n' + str(final_list_null) + '\n \n' + 'Danh sách SA chưa upload bản đã duyệt: '+ '\n \n'  + str(final_list_not_null)
        subject = 'Danh sách CS và SA quá hạn'
        sender = 'support@vnsp.vn'
        recipients = EmailReport.objects.filter(ActionName='CSDeadline').values_list('ReciEmail', flat=True)

        if final_list_null or final_list_not_null:
            send_mail(subject, message, sender, recipients)



        return