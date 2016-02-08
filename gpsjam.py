#!/usr/bin/env python3
from __future__ import division
from numpy import log10
#
from tincanradar.fwdmodel import friis
from harmonicradar.fwdmodel import noisepower

Fgps=1.575e9
Mindist_m = (20200-8.848)*1e3
Pgps = 59 #[dBm] EIRP
Grx = 0 #dBi RX antenna
Brx = 2.046e6
NF =2 #[dB]

Prxgps = Pgps - friis(Mindist_m,Fgps) + Grx #[dBm]
Pn = noisepower(NF,Brx)

Prxtot =  10*log10(10**(Prxgps/10)  + 10**(Pn/10))
