from .models import InappPosts
from bs4 import BeautifulSoup
from requests import get



def update_inapp_posts():

    url = "https://inapp.com/blog/"
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    post_containers = html_soup.find_all('div',
                                         class_='vc_grid-item vc_clearfix vc_col-sm-4 vc_grid-item-zone-c-bottom')
    # InappPosts.objects.all().delete()
    for i in range(6):
        title = post_containers[i].h4.text
        link = post_containers[i].a['href']
        obj, created = InappPosts.objects.get_or_create(pk=i)
        obj.title = title
        obj.link = link
        obj.save()
