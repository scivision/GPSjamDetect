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

  P_{rx,max} = P_{tx,eirp} - L_{friis} - L_{scintillation} - L_{obstruction} - L + G_{ant,rx} + P_{thermal} + P_{jam}

Let's assume the GPS satellite `EIRP <https://en.wikipedia.org/wiki/Equivalent_isotropically_radiated_power>`_ is `no more than 60dBm <http://www.insidegnss.com/node/2140>`_
