from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from teams.models import Team
from utils.dict_operations import completed_performances


def index(request):
    context = {"teams": Team.objects.all().select_related("club", "stream")}
    return render(request, "gymnastics/teams/index.html", context)


def detail(request, id):
    team = Team.objects.select_related("club", "stream").get(id=id)
    stream = team.stream
    disciplines = stream.get_ordered_disciplines()

    athletes = (
        team.athlete_set.all()
        .select_related("club", "stream", "team__stream", "squad")
        .prefetch_related("performance_set")
    )

    athletes_disciplines_result_dict = athletes.get_athletes_disciplines_result_dict()
    athletes_disciplines_rank_dict = stream.get_athletes_disciplines_rank_dict(
        athletes_disciplines_result_dict
    )

    context = {
        "team": team,
        "club": team.club,
        "stream": stream,
        "disciplines": disciplines,
        "athletes": athletes,
        "athletes_disciplines_result_dict": athletes_disciplines_result_dict,
        "athletes_disciplines_rank_dict": athletes_disciplines_rank_dict,
        "athlete_performances_completed": completed_performances(
            athletes_disciplines_result_dict
        ),
    }
    return render(request, "gymnastics/teams/detail.html", context)


class TeamCreateView(generic.CreateView):
    model = Team
    fields = ["name", "club", "stream"]
    template_name = "gymnastics/teams/new.html"
    success_url = reverse_lazy("teams.index")


class TeamUpdateView(generic.UpdateView):
    model = Team
    fields = ["name", "club", "stream"]
    template_name = "gymnastics/teams/edit.html"

    def get_success_url(self):
        return reverse("teams.detail", kwargs={"id": self.kwargs["pk"]})


class TeamDeleteView(generic.DeleteView):
    model = Team
    template_name = "gymnastics/teams/delete.html"
    success_url = reverse_lazy("teams.index")
