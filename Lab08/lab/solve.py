import angr
import claripy
import sys

main_addr = 0x4011a9
find_addr = 0x401371
avoid_addr = 0x40134d


def handle_scanf_real_input(raw_input):
    idx = 0
    for c in raw_input:
        if c == ord('\n') or c == ord('\0'):
            break
        idx += 1
    return raw_input[:idx]


class my_scanf(angr.SimProcedure):
    def run(self, format_string, dest):
        simfd = self.state.posix.get_fd(sys.stdin.fileno())
        data, ret_size = simfd.read_data(0x4)
        self.state.memory.store(dest, data)
        return ret_size


proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})
proj.hook_symbol('__isoc99_scanf', my_scanf(), replace=True)

state = proj.factory.blank_state(addr=main_addr)

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=find_addr, avoid=avoid_addr)
if simgr.found:
    _input = simgr.found[0].posix.dumps(sys.stdin.fileno())
    print(_input)
    print(handle_scanf_real_input(_input))

    with open(file='solve_input', mode='w') as f:
        for i in range(15):
            _input = simgr.found[0].posix.dumps(
                sys.stdin.fileno())[i*0x4:(i+1)*0x4]
            print(f'x{i}: ', int.from_bytes(handle_scanf_real_input(
                _input), byteorder='little', signed=True))
            f.write(str(int.from_bytes(handle_scanf_real_input(
                _input), byteorder='little', signed=True)))
            f.write('\n')
else:
    print('Failed')
