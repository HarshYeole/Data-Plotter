import os
import pyautogui as p
import sys


# Update Device List
def getPorts():
    if os.name == 'nt':  # sys.platform == 'win32':
        from tools.list_ports_windows import comports
        hits = 0
        comPortList = []
        iterator = sorted(comports())

        for n, (port, desc, hwid) in enumerate(iterator, 1):
            portName = "{}".format(port)
            # sys.stdout.write(portName)
            comPortList.append(portName)
            hits += 1

        if hits == 0:
            # sys.stderr.write("no ports found\n")
            return []
        return comPortList


# Add Oscilloscope
def getOscilloscope():
    address = p.password(text="Only IP", mask="", default="10.65.2.17")  # 'TCPIP::10.65.1.116::inst0::INSTR'
    try:
        instr = RsInstrument("TCPIP::" + address + "::inst0::INSTR", True, False)
        return instr
    except:
        sys.stderr.write("Couldn't connect...")
        return []