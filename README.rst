====================
GPS Jammer Detection
====================
sub-$100 methods of finding GPS jammers via hobbyist &amp; crowdsourced methods

Elementary Detection Candidates
===============================
Since we know the minimum distance between the ground and GPS to be:

.. math::

  R_{min} = 20200-8.848 = 20191.152 \textrm{[km]}

We can say that the minimum Friis path loss is:

.. math::

  L_{friis} = 20 \log_{10}\left(\frac{4\pi}{c}df\right)

Which is the largest loss for normal GPS scenarios. The received power by the GPS receiver will be no greater than:

.. math::

  P_{rx,max} = P_{tx,eirp} - L_{friis} - L_{scintillation} - L_{obstruction} - L + G_{ant,rx} + P_{thermal} + P_{multipath} + P_{jam}

Multipath can increase or decrease the signal amplitude. In general multipath has random phase, based on the environment and platform motion. Let's neglect multipath and scintillation (although they're very important in certain aspects of GPS work).
Let's further assume we're outside in the desert, so there's no obstruction loss. Let's assume net antenna system gain is 0dBi.

.. math::

  P_{rx,max}' = P_{tx,eirp} - L{friis} + P_{thermal} = -109 dBm

where :math:`P_{rx,gps} = -123` dBm, with a 2dB system noise figure in a 2MHz RX bandwidth.

Could we find a way to reject occasional impulses of increased signal strength, yet note signal levels of abnormally high power as interference or jamming?

Let's assume the GPS satellite `EIRP <https://en.wikipedia.org/wiki/Equivalent_isotropically_radiated_power>`_ is `no more than 60dBm <http://www.insidegnss.com/node/2140>`_.

We also note from the available trade and journal literature that chirp jammers are the most popular type of GPS jamming.

This makes one think of the chirplet transform as a candidate for detecting jammers at a distance, along with the usual CW tone extraction (subspace methods) and noise jamming (power threshold) techniques.
