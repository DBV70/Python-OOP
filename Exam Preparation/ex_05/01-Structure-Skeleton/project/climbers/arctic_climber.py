from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    MIN_STRENGTH = 100
    STRENGTH_DECREASE_PER_CLIMB = 20

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.MIN_STRENGTH

    def climb(self, peak: BasePeak):
        ratio = 2 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= self.STRENGTH_DECREASE_PER_CLIMB * ratio
        self.conquered_peaks.append(peak.name)