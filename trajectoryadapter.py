from abc import ABC, abstractmethod

class TrajectoryAdapter(ABC):
    @abstractmethod
    def compute_center_of_mass():
        pass

    @abstractmethod
    def compute_radius_of_gyration():
        pass