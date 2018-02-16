from django import template
register = template.Library()


@register.inclusion_tag('ajax/partials/render_ajax.html')
def get_ajax_object(strategy, id):
    return {
        'strategy': strategy,
        'id': id,
    }
