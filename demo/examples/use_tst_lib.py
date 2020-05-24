

import sys
from examples import hello_mod as h

sys.path.append(r'.\mylib')
print(sys.path)

import tst_lib as t

print(f"value of a in hello_mod:{h.a}")
print(f"value of x in use_tst_lib:{t.x}")

