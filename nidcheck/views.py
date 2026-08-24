from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, FormView

from django_ratelimit.decorators import ratelimit

from .forms import NIDCheckForm
from .intelligence import NIDExposureEngine
from .models import NIDCheck


def get_client_ip(request):
    """
    Return the client's IP address.
    Supports proxies that send X-Forwarded-For.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        return x_forwarded_for.split(",")[0].strip()

    return request.META.get("REMOTE_ADDR")


@method_decorator(
    ratelimit(
        key="ip",
        rate="5/m",
        method="POST",
        block=True,
    ),
    name="dispatch",
)
class NIDCheckView(FormView):
    template_name = "check.html"
    form_class = NIDCheckForm

    def form_valid(self, form):
        print(
        "RATE LIMIT DEBUG:",
        self.request.META.get("REMOTE_ADDR"),
        self.request.META.get("HTTP_X_FORWARDED_FOR"),
        self.request.get_host(),
        self.request.path,
        self.request.method,
    )

        nid_number = form.cleaned_data["nid_number"]

        result = NIDExposureEngine.check(nid_number)

        visitor_ip = get_client_ip(self.request)

        check = NIDCheck.objects.create(
        nid_number=nid_number,
        visitor_ip=visitor_ip,
        is_exposed=result["is_exposed"],
        match_count=result["match_count"],
        )

        self.success_url = reverse_lazy(
        "nid_result",
            kwargs={"pk": check.pk},
        )

        return super().form_valid(form)


class NIDResultView(DetailView):
    model = NIDCheck
    template_name = "result.html"
    context_object_name = "check"


from django.http import HttpResponse


def ratelimited(request, exception):
    return HttpResponse(
        "RATE LIMIT HIT",
        status=429,
    )