import os
import sys
import time
import epics

# EPICS environment configuration
os.environ['EPICS_CA_ADDR_LIST']='10.41.70.1'

# use input 0 on front panel as trigger source10.41.70.1
inputSelPV = epics.PV("APTM1-EVR1:In0-Trig:Ext-Sel")
inputCodePV = epics.PV("APTM1-EVR1:In0-In0-Code:Ext-SP")

# delaygen PVs
dlygenEventPV = epics.PV("APTM1-EVR1:DlyGen0-Evt-Trig0-SP")
dlygenWidthPV = epics.PV("APTM1-EVR1:DlyGen0-Width-SP")
dlygenDelayPV =epics.PV("APTM1-EVR1:DlyGen0-Delay-SP")

#backplane PV
backplanePV = epics.PV("APTM1-EVR1:OutBack0-Src-SP")

# Configure INPUT 0 to generate event 10
inputSelPV.put("Edge")
inputCodePV.put(10)

# Configure delay generator 0 to trigger from event 10
dlygenEventPV.put(10) 

# Configure backplane to trigger from deley generator 0
backplanePV.put(0)





events = np.array([14, 127])
timestamps = np.array([0, 2])

# PVs declaration
timestampsPV = epics.PV('EVR-MTCA:SoftSeq0-Timestamp-SP')
evtcodePV = epics.PV('EVR-MTCA:SoftSeq0-EvtCode-SP')
commitPV = epics.PV('EVR-MTCA:SoftSeq0-Commit-Cmd')

# Write PVs
evtcodePV.put(events)
timestampsPV.put(timestamps)
commitPV.put(1)

