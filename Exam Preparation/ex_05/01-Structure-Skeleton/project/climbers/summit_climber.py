from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    MIN_STRENGTH = 75
    STRENGTH_DECREASE_PER_CLIMB = 30

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGTH

    def climb(self, peak: BasePeak):
        ratio = 1.3 if peak.calculate_difficulty_level() == "Advanced" else 2.5
        self.strength -= self.STRENGTH_DECREASE_PER_CLIMB * ratio
        self.conquered_peaks.append(peak.name)