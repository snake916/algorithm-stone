from manimlib import *
import networkx as nx
from .algo_vgroup import *
from .algo_node import *

class AlgoTable(AlgoVGroup):
    def __init__(self, scene, objs, **kwargs):
        self.scene = scene
        super().__init__(**kwargs)
        
        v = self
        for row in objs:
            for c in row:
                if isinstance(c, str):
                    v.add(Text(c).scale(0.3))
                else:
                    v.add(c)
        v.arrange_in_grid(n_rows=objs.shape[0])


