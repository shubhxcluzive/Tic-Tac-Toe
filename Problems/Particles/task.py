spin = ['1/2', '1/2', '1/2', '1/2', '1', '0']
charge = ['-1/3', '2/3', '-1', '0', '0', '0']
spin1 = input()
charge1 = input()
if spin1 == spin[0] and charge1 == charge[0]:
    print("Strange Quark")
elif spin1 == spin[1] and charge1 == charge[1]:
    print("Charm Quark")
elif spin1 == spin[2] and charge1 == charge[2]:
    print("Electron Lepton")
elif spin1 == spin[3] and charge1 == charge[3]:
    print("Muon Lepton")
elif spin1 == spin[4] and charge1 == charge[4]:
    print("Photon Boson")
elif spin1 == spin[5] and charge1 == charge[5]:
    print("Higgs boson Boson")
else:
    print("wrong input, plz try again later")
