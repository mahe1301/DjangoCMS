from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.mail import send_mass_mail
from django.core.mail import mail_admins
from django.core.mail import mail_managers
from django.core.mail import EmailMessage
from email.message import EmailMessage as em


def sendSimpleEmail(e_subject,e_msg,email_to=['mahe78611@gmail.com'],email_from='mahe.786.puthumana@gmail.com'):
   print(e_subject,e_msg ,email_from , email_to)
   res = send_mail(e_subject,e_msg ,email_from , email_to)
   print(res)
   if res == 1:
       msg = "Mail Sent Successfuly"
   else:
       msg = "Mail could not sent"
   return msg


def sendMassEmail(e_subject,e_msg,email_to='mahe78611@gmail.com',email_from='mahe.786.puthumana@gmail.com'):
   msg1 = (e_subject + ' 1', e_msg + ' 1', email_from, [email_to])
   msg2 = (e_subject + ' 2', e_msg + ' 2', email_from, [email_to])
   res = send_mass_mail((msg1, msg2), fail_silently = False)
   return HttpResponse('%s'%res)


# def sendAdminsEmail(request):
#    res = mail_admins('my subject', 'site is going down.')
#    return HttpResponse('%s'%res)
#
# # inside settings.py
# # ADMINS = (('polo', 'polo@polo.com'),)
# #
# # MANAGERS = (('popoli', 'popoli@polo.com'),)
#
# def sendManagersEmail(request):
#    res = mail_managers('my subject 2', 'Change date on the site.')
#    return HttpResponse('%s'%res)


def sendHTMLEmail(e_subject,e_msg,email_to='mahe78611@gmail.com',email_from='mahe.786.puthumana@gmail.com'):
   html_content = "<strong>"+e_msg+"</strong>"
   email = EmailMessage(e_subject, html_content, email_from, [email_to])
   email.content_subtype = "html"
   res = email.send()
   return HttpResponse('%s'%res)


def sendEmailWithAttach(e_subject,e_msg,email_to='mahe78611@gmail.com',email_from='mahe.786.puthumana@gmail.com'):
    html_content = "Comment tu vas?"
    email = EmailMessage(e_subject, html_content, email_from, [email_to])
    email.content_subtype = "html"

    fd = open('manage.py', 'r')
    email.attach('manage.py', fd.read(), 'text/plain')

    res = email.send()
    return HttpResponse('%s' % res)

def sendEmailWithInvoice(e_subject,e_msg,email_to,email_from,attachment_file):
   try: 
      res=0
      email = EmailMessage(e_subject, e_msg, email_from, email_to)
      email.content_subtype = "html"
      email.attach_file(attachment_file)
      res = email.send()
      if res == 1:
         msg = "Mail Sent Successfuly"
      else:
         msg = "Mail could not sent"
   except Exception as e:
      res=0
   return res
   
def sendEmailForOrderProcessing(e_subject,html_content,email_to,email_from,email_bcc):
   try: 
      res=0
      email = EmailMessage(e_subject, html_content, email_from, email_to,email_bcc)
      email.content_subtype = "html"
      res = email.send()
      res = email.send(fail_silently=True)
      if res == 1:
         msg = "Mail Sent Successfuly"
      else:
         msg = "Mail could not sent"
   except Exception as e:
      # print(e)
      res=0
   return res
