import os
import sys
from app import login

tcl_path = os.path.join(sys.base_prefix, "tcl", "tcl8.6")
tk_path = os.path.join(sys.base_prefix, "tcl", "tk8.6")

os.environ['TCL_LIBRARY'] = tcl_path
os.environ['TK_LIBRARY'] = tk_path

if __name__ == "__main__":
    
    login.ventana_inicio()
