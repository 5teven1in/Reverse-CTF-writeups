import angr
import claripy

def add_base(addr):
    return addr + 0

flag = claripy.BVS('flag', 100 * 8)
target = add_base(0x400231)

project = angr.Project("./bin3", auto_load_libs = False)

state = project.factory.entry_state(stdin = flag)

'''
for c, val in zip(flag.chop(8), b"AIS3{"):
    state.solver.add(c == val)
'''

sm = project.factory.simulation_manager(state)
sm.explore(find = target)

found = sm.found[0]
text = found.posix.dumps(0)

print(repr(text))
