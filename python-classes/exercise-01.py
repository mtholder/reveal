#!/usr/bin/env python3
import random



CODE HERE
# Create a new Organism class
# create an initializer that takes a Patch 
#   instance as an argument and stores
#   it as a "patch" attribute
# Set a "num_patches_to_disperse" attribute
#   to be a positive integer (not huge, let's say < 10)
# Note that there is an add_organism method in Patch
#   as the last step in the initialize routine for 
#   the Organism, each instance should add itself
#   to its patch using this method.


EXERCISE_4 = False
#org_class_list = []

class Patch:
    """Represents a cell in the grid of the entire Landscape."""

    def __init__(self, x_pos, y_pos, landscape):
        assert x_pos >= 0
        assert y_pos >= 0
        self.x, self.y = x_pos, y_pos
        self.organisms = []
        self._grid = landscape

    def add_organism(self, org):
        self.organisms.append(org)
        org.patch = self 

    def remove_organism(self, org):
        while org in self.organisms:
            self.organisms.remove(org)
        org.patch = None

    def random_neighbor(self):
        r = random.random()
        x, y = self.x, self.y
        if r < 0.25:
            x -= 1
        elif r < 0.5:
            x += 1
        elif r < 0.75:
            y -= 1
        else:
            y += 1
        return self._grid.patch_at(x, y)
 
    def str_block(self):
        """Returns a list of strings describing the cell and the max str len."""
        num_org_str = "{}".format(len(self.organisms))
        loc_str = "@({},{})".format(self.x, self.y)
        m = max(len(num_org_str), len(loc_str))
        return [num_org_str, loc_str], m

    def get_random_org_avoiding(self, avoid_org):
        others = [org for org in self.organisms if org is not avoid_org]
        if len(others) == 0:
            return None
        return random.choice(others)


class Landscape:
    """A wrapped rectangle of patches meant to represent a spatial landscape"""

    def __init__(self, num_rows, num_columns):
        if num_columns < 0:
            raise ValueError("Expecting at least 1 column")
        if num_rows < 0:
            raise ValueError("Expecting at least 1 row")
        self.rows = []
        self._all_patches = []
        for i in range(num_rows):
            curr_row = []
            for j in range(num_columns):
                curr_row.append(Patch(i, j, self))
            self.rows.append(curr_row)
            self._all_patches.extend(curr_row)
        self.organisms = []
    
    def patch_at(self, x, y):
        if x >= self.num_rows:
            x -= self.num_rows
        if y >= self.num_columns:
            y -= self.num_columns
        return self.rows[x][y]

    @property
    def num_rows(self):
        return len(self.rows)

    @property
    def num_columns(self):
        return len(self.rows[0])

    @property
    def num_cells(self):
        return len(self._all_patches)

    def create_organisms(self, num):
        for i in range(num):
            rand_patch = random.choice(self._all_patches)
            if EXERCISE_4:
                org_class = random.choice(org_class_list)
                new_org = org_class(rand_patch)
            else:
                new_org = Organism(rand_patch)
            self.organisms.append(new_org)

    def show(self):
        print("{} organisms:".format(len(self.organisms)))
        block_mat = []
        max_len = 0
        rows_per_block = 0
        for row in self.rows:
            block_row = []
            for patch in row:
                str_block, max_l = patch.str_block()
                rows_per_block = len(str_block)
                block_row.append(str_block)
                if max_l > max_len:
                    max_len = max_l
            block_mat.append(block_row)
        max_len = max_len + 2
        nc = self.num_columns
        header_cell = "+"*max_len
        div_cell = "-"*max_len
        headers = [header_cell] * nc
        divs = [div_cell] * nc
        header = '+{}+'.format("+".join(headers))
        div = '+{}+'.format("+".join(divs))
        print(header)
        for block_row in block_mat:
            if block_row is not block_mat[0]:
                print(div)
            for ind in range(rows_per_block):
                curr_line = []
                for bc in block_row:
                    curr_str = bc[ind]
                    curr_line.append(curr_str.center(max_len))
                data = "+{}+".format("|".join(curr_line))
                print(data)
        print(header)

    def next_step(self):
        for org in self.organisms:
            do_random_organism_movement(org)
        #self.do_rand_interactions()
        #self.do_reproduction()

    def check(self):
        for o in self.organisms:
            assert o.alive
            assert o in o.patch.organisms
            for p in self._all_patches:
                if o.patch is not p:
                    try:
                        assert o not in p.organisms
                    except:
                        print(o, "is in", p)
                        raise

    def do_rand_interactions(self):
        before = list(self.organisms)
        for org in before:
            if org.alive:
                patch = org.patch
                other = patch.get_random_org_avoiding(org)
                if other is not None:
                    org.do_interaction(other)
        self.organisms = []
        for org in before:
            if org.alive:
                self.organisms.append(org)

    def do_reproduction(self):
        new_orgs = []
        for org in self.organisms:
            new_orgs.extend(org.reproduce())
        self.organisms.extend(new_orgs)

def do_random_organism_movement(organism):
    """Checks num_patches_to_disperse and makes that number of random movements."""
    dd = organism.num_patches_to_disperse
    patch = organism.patch
    for i in range(dd):
        new_patch = patch.random_neighbor()
        patch.remove_organism(organism)
        new_patch.add_organism(organism)
        patch = new_patch


def main():
    grid = Landscape(5, 5)
    grid.create_organisms(100)
    grid.show()
    for cycle in range(10):
        grid.next_step()
        print("cycle =", 1 + cycle)
        grid.show()



if __name__ == '__main__':
    main()