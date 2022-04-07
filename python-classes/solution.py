class Organism:
    def __init__(self, patch):
        self.patch = patch
        if patch is not None:
            patch.add_organism(self)
        self.num_patches_to_disperse = 2
        # For exercise 2 add this:
        self.alive = True
        self.energy = random.random()

    # For exercise 2 add this:
    def do_interaction(self, other):
        if self.energy > other.energy:
            self.energy += other.energy/2
            other.die()
    
    def die(self):
        if self.patch:
            self.patch.remove_organism(self)
        self.alive = False
    # For exercise 3 add this:
    def reproduce(self):
        children = []
        if self.energy > 0.2:
            self.energy -= 0.2 
            child = self.__class__(self.patch)
            children.append(child)
        return children

