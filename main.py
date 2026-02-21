import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)
        for player in players:
            player_race = players[player].get("race")

            race, created = Race.objects.get_or_create(
                name=player_race["name"],
                defaults={
                    "description": player_race["description"]
                }
            )

            for skill in player_race["skills"]:
                Skill.objects.update_or_create(
                    name=skill["name"],
                    defaults={
                        "bonus": skill["bonus"],
                        "race": race
                    }
                )
            guild_data = players[player].get("guild")
            if guild_data:
                guild, created = Guild.objects.get_or_create(
                    name=guild_data["name"],
                    defaults={
                        "description": guild_data["description"]
                    }
                )
            else:
                guild = None

            Player.objects.create(
                nickname=player,
                email=players[player]["email"],
                bio=players[player]["bio"],
                race=race,
                guild=guild
            )


if __name__ == "__main__":
    main()
