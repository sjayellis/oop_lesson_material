from trajectoryadapter import TrajectoryAdapter
import mdtraj as mdt

class MDTrajAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.trajectory = mdt.load_pdb(filename)
        print('Selected MDTraj')

    def compute_center_of_mass(self):
        return 10*mdt.compute_center_of_mass(self.trajectory)

    def compute_radius_of_gyration(self):
        return 10*mdt.compute_rg(self.trajectory)