#import mdtraj as mdt
#import MDAnalysis as mda
import numpy as np
from mdtraj_adapter import MDTrajAdapter


#trajectory = mdt.load_pdb('protein.pdb')
#universe = mda.Universe('protein.pdb')

#print(f'Center of mass: \n{mdt.compute_center_of_mass(trajectory)}')
#print(f'Radius of Gyration: \n{mdt.compute_rg(trajectory)}')
#mass_by_frame = np.ndarray(shape=(len(universe.trajectory), 3))
#for ts in universe.trajectory:
#    mass_by_frame[ts.frame] = universe.atoms.center_of_mass(compound="segments")

#print(f'Center of mass: \n{mass_by_frame}')

md_toolkit = MDTrajAdapter('protein.pdb')
print(f'Center of mass: \n{md_toolkit.compute_center_of_mass()}')
print(f'Center of mass: \n{md_toolkit.compute_radius_of_gyration()}')