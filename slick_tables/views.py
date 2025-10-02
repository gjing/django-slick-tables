from django.views import ListView

from slick_tables.headers import Header


# Create your views here.
class SlickTableListView(ListView):
    def render_headers(self) -> list[str]:
        headers: list[str] = []
        for attr in self._meta.fields:
            headers.append(self.render_header(getattr(self, attr)))
        return headers

    def render_header(self, field: Header) -> str:
        return field.render()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headers'] = self.render_headers()
        return context

    class Meta:
        abstract = True
        fields: list[str] = []
