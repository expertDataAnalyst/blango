from django import template
from django.contrib.auth import get_user_model
from django.utils.html import format_html

register = template.Library()
user_model = get_user_model()

@register.filter
def author_details(author):
  if not isinstance(author, user_model):
    #return empty strings as safe default
    return ""

  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"

  if author.email:
    email = author.email
    prefix = format_html('<a href="mailto:{email}">', author.email)
    suffix = format_html('</a>')
  else:
    prefix = ''
    sufflix ='' 

  return format_html('{}{}{}', prefix, name, suffix)