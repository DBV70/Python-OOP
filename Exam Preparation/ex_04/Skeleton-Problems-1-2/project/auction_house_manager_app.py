from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector

class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        artifact = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}.get(artifact_type)
        if not artifact:
            raise ValueError("Unknown artifact type!")

        if self._find_obj_by_name(artifact_name, self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")

        self.artifacts.append(artifact(artifact_name, artifact_price, artifact_space))
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        collector = {"Museum": Museum, "PrivateCollector": PrivateCollector}.get(collector_type)
        if not collector:
            raise ValueError("Unknown collector type!")

        if self._find_obj_by_name(collector_name, self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")

        self.collectors.append(collector(collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self._find_obj_by_name(collector_name, self.collectors)
        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = self._find_obj_by_name(artifact_name, self.artifacts)
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if collector.can_purchase(artifact.price, artifact.space_required):
            self.artifacts.remove(artifact)
            collector.purchased_artifacts.append(artifact)
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            return f"{collector.name} purchased {artifact.name} for a price of {artifact.price}."

        return "Purchase is impossible."

    def remove_artifact(self, artifact_name: str):
        artifact = self._find_obj_by_name(artifact_name, self.artifacts)
        if not artifact:
            return "No such artifact."
        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count = len([c.increase_money() for c in self.collectors if c.available_money <= max_money])
        return f"{count} collector/s increased their available money."

    def get_auction_report(self):
        collectors = sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name))
        sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)

        result = ["**Auction statistics**",
                  f"Total number of sold artifacts: {sold_artifacts}",
                  f"Available artifacts for sale: {len(self.artifacts)}",
                  "***"]

        [result.append(str(c)) for c in collectors]

        return "\n".join(result)

    @staticmethod
    def _find_obj_by_name(name, collection):
        return next((obj for obj in collection if obj.name == name), None)
