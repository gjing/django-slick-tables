from django.template.loader import render_to_string


class Header():
    name = "Header"
    template_name = "slick_tables/headers/default.html"

    def render(self) -> str:
        return render_to_string(self.template_name, {"header": self})

    class Meta:
        abstract = True
