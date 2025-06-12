import keywords as OSS

import operations as OSP
import global_ops as OSG

from constants.constant import *
from constants.pointer import *
from constants.variable import *

loaded = Variable(False)

def Compile(filename = "tests/data/source.mod"):
    # Variables
    t = filename # TODO: To devise a way to pass the file name in future
    loaded.m_value = False
    if t is not None:
        OSS.Init(t, 0)
        OSP.Module(0)

def Decode():
    OSG.Decode()

def Load():
    if not OSS.error.m_value and not loaded.m_value:
        OSG.Load()
        loaded.m_value = True

def Exec(S):
    return OSG.Exec(S)

