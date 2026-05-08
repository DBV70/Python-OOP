from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    VALID_DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER_TYPES.keys():
            return f"{diver_type} is not allowed in our competition."

        if self._find_obj_by_name(diver_name, self.divers) is not None:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."


    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        if self._find_obj_by_name(fish_name, self.fish_list) is not None:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._find_obj_by_name(diver_name, self.divers)
        fish = self._find_obj_by_name(fish_name, self.fish_list)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

        return None

    def health_recovery(self):
        count = len([d for d in self.divers if d.has_health_issue])
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self._find_obj_by_name(diver_name, self.divers)
        result = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            result.append(f"{fish.fish_details()}")
        return '\n'.join(result)

    def competition_statistics(self):
        divers = [d for d in self.divers if not d.has_health_issue]
        divers_sorted = sorted(divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        for d in divers_sorted:
            result.append(str(d))
        return '\n'.join(result)

    # helper methods
    @staticmethod
    def _find_obj_by_name(name: str, obj_list: list):
        return next((obj for obj in obj_list if obj.name == name), None)