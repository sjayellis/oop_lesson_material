from trajectoryadapter import TrajectoryAdapter
#from mdanalysis_adapter import MDAnalysisAdapter
#from mdtraj_adapter import MDTrajAdapter

class MDFactory:
    _toolkits = {}

    def register(self, toolkit_name, toolkit_class):
        if not issubclass(toolkit_class, TrajectoryAdapter):
            raise TypeError(f'{toolkit_class} is not a TrajectoryAdapter')
        self._toolkits[toolkit_name] = toolkit_class

    def md_factory(self, md_toolkit, filename):
        #toolkits = {'MDTraj': MDTrajAdapter, 'MDAnalysis': MDAnalysisAdapter}

        if md_toolkit not in self._toolkits.keys():
                raise TypeError('Toolkit not found.')
        toolkit_class = self._toolkits[md_toolkit]
        return toolkit_class(filename)