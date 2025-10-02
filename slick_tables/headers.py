from django.shortcuts import render


class Header():
    name = "Header"
    template_name = "slick_tables/headers/default.html"

    def render(self) -> str:
        return render(self.template_name, {"header": self})

    class Meta:
        abstract = True
