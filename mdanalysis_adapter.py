from trajectoryadapter import TrajectoryAdapter
import MDAnalysis as mda
import numpy as np

class MDAnalysisAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.universe = mda.Universe(filename)
        print('Selected MDAnalysis')
    
    def compute_center_of_mass(self):
        mass_by_frame = np.ndarray(shape=(len(self.universe.trajectory), 3))
        for ts in self.universe.trajectory:
            mass_by_frame[ts.frame] = self.universe.atoms.center_of_mass(compound="segments")
        return mass_by_frame

    def compute_radius_of_gyration(self):
        rg_by_frame = np.empty(len(self.universe.trajectory))
        for ts in self.universe.trajectory:
            rg_by_frame[ts.frame] = self.universe.atoms.radius_of_gyration()
        return rg_by_frame