from common.models import Discipline, Performance
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views import generic


# renders index / home page
def index(request):
    return redirect(reverse("tournaments.main"))


# renders todo page
def process(request):
    return render(request, "gymnastics/process.html", None)


def performances_index(request):
    context = {
        "performances": Performance.objects.all()
        .select_related("athlete")
        .select_related("discipline")
    }
    return render(request, "gymnastics/performances/index.html", context)


class PerformanceCreateView(generic.CreateView):
    model = Performance
    fields = ["athlete", "discipline", "value", "value_final"]
    template_name = "gymnastics/performances/new.html"
    success_url = reverse_lazy("performances.index")


class PerformanceDetailView(generic.DetailView):
    model = Performance
    template_name = "gymnastics/performances/detail.html"


class PerformanceUpdateView(generic.UpdateView):
    model = Performance
    fields = ["athlete", "discipline", "value", "value_final"]
    template_name = "gymnastics/performances/edit.html"

    def get_success_url(self):
        return reverse("performances.detail", kwargs={"pk": self.kwargs["pk"]})


class PerformanceDeleteView(generic.DeleteView):
    model = Performance
    template_name = "gymnastics/performances/delete.html"
    success_url = reverse_lazy("performances.index")


def disciplines_index(request):
    context = {"disciplines": Discipline.objects.all()}
    return render(request, "gymnastics/disciplines/index.html", context)


def discipline_detail(request, id, slug):
    discipline = Discipline.objects.get(id=id)
    streams = discipline.stream_set.all()
    performances = discipline.performance_set.all().select_related("athlete")

    context = {
        "discipline": discipline,
        "streams": streams,
        "performances": performances,
    }
    return render(request, "gymnastics/disciplines/detail.html", context)


class DisciplineCreateView(generic.CreateView):
    model = Discipline
    fields = ["name"]
    template_name = "gymnastics/disciplines/new.html"


class DisciplineUpdateView(generic.UpdateView):
    model = Discipline
    fields = ["name"]
    template_name = "gymnastics/disciplines/edit.html"


class DisciplineDeleteView(generic.DeleteView):
    model = Discipline
    template_name = "gymnastics/disciplines/delete.html"
    success_url = reverse_lazy("disciplines.index")
