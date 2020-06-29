from django.shortcuts import render, redirect, HttpResponse
from .models import League, Team, Player

from . import team_maker


def index(request):
    baseball_conference = League.objects.get(id=2).teams.all()
    for team_baseball in baseball_conference:
        for player_baseball in team_baseball.curr_players.all():
            pass

    football_conference = League.objects.get(id=7).teams.all()
    for team_football in football_conference:
        for player in team_football.curr_players.all().filter(last_name__contains="lopez"):
            pass

    football = League.objects.filter(sport__contains="football")
    for league_football in football:
        for football_team in league_football.teams.all():
            for player_football in football_team.curr_players.all():
                print(player_football.first_name)

    context = {
        "leagues": League.objects.all(),
        "teams": Team.objects.all(),
        "players": Player.objects.all(),
        'soccer_atlanta': Team.objects.get(id=5),
        'boston_peguins': Team.objects.get(id=28).curr_players.all(),
        # Baseball
        'team_baseball': team_baseball.curr_players.all(),
        # Football
        'team_football': team_football.curr_players.all().filter(last_name__contains="lopez"),
        # All FOOTBALL PLAYER
    }

    return render(request, "leagues/index.html", context)


def make_data(request):
    team_maker.gen_leagues(10)
    team_maker.gen_teams(50)
    team_maker.gen_players(200)
    return redirect("index")
