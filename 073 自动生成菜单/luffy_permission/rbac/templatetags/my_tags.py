from collections import OrderedDict

from django.conf import settings
from django.template import Library

register = Library()


@register.inclusion_tag('menu.html')
def generator(request):
    # 一级菜单
    # menus = request.session.get(settings.MENU_SESSION_KEY)
    # url = request.path
    # for i in menus:
    #     if re.match(r'{}$'.format(i['url']), url):
    #         i['class'] = 'active'
    #         break
    # return {'menus': menus}

    # 二级菜单
    menu_dic = request.session.get(settings.MENU_SESSION_KEY)

    # 通过有序字典，为菜单指定顺序
    od = OrderedDict()
    keys = sorted(menu_dic, key=lambda x: menu_dic[x]['weight'], reverse=True)
    for i in keys:
        od[i] = menu_dic[i]

    # 二级菜单样式
    url = request.path
    for i in menu_dic.values():
        i['class'] = 'hide'
        for m in i['children']:
            if request.current_menu_id == m['id']:
                m['class'] = 'active'
                i['class'] = ''
    return {'menu_dic': od}
