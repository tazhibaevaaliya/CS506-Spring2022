class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon


    def dbscan(self):
        """
            returns a list of assignments. The index of the
            assignment should match the index of the data point
            in the dataset.
        """
        
        raise NotImplementedError

    def explore_and_assign_eps_neighborhood(self,P, cluster,assignment):
        neighborhood = self.epsilon_neighborhood(P)

        while(neighborhood):
             neighbor_of_P = neighborhood.pop()

             if assignment[neighbor_of_P]!=0:
                 continue

            assignment[neighbor_of_P] = cluster

            next_neightborhood = self.epsilon
