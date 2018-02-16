from django.conf import settings

from django.views.generic import TemplateView
from django_ajax.mixin import AJAXMixin

from .utils import Selector

# Create your views here.


class AjaxBaseSerializedView(AJAXMixin, TemplateView):
    pk = None
    strategy_name = None
    module_path = None
    obj = None
    template_name = None
    message = None

    def get_context_data(self, **kwargs):
        ctx = super(AjaxBaseSerializedView, self).get_context_data(**kwargs)
        ctx['object'] = self.obj
        ctx['message'] = self.message  # The error message
        return ctx

    def get(self, request, *args, **kwargs):

        try:
            self.pk = kwargs['pk']
            self.strategy_name = kwargs['strategy_name']
        except KeyError:
            pass

        self._populate_from_settings()

        if (self.pk is None) or (self.strategy_name is None):
            self.message = 'Missing pk or strategy_name in URL params'
            self.template_name = 'ajax/partials/error.html'
        else:

            try:
                self._call_strategy()
            except NotImplementedError:
                self.message = "Wrong setting configuration, unable to load the correct strategy"
                self.template_name = 'ajax/partials/error.html'
            except ImportError:
                self.message = "Wrong setting configuration, fix the module path"
                self.template_name = 'ajax/partials/error.html'
            except Exception as e:
                self.message = "Generic error in module_path: {0}".format(e)
                self.template_name = 'ajax/partials/error.html'

        return super(AjaxBaseSerializedView, self).get(request, *args, **kwargs)

    def _populate_from_settings(self):
        configuration = settings.EASY_AJAX

        try:
            config = configuration[self.strategy_name]
        except KeyError:
            self.template_name = 'ajax/partials/error.html'
            config = []

        try:
            self.template_name = config[1]
            self.module_path = config[0]
        except IndexError:
            self.template_name = 'ajax/partials/error.html'

    def _call_strategy(self):
        strategy = Selector(module_path=self.module_path, id=int(self.pk))
        self.obj = strategy.execute(id=int(self.pk))

    def get_template_names(self):
        return [self.template_name, 'ajax/partials/template_error.html']
