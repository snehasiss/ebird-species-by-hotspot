eBird Species by Hotspot Locations
==================================

Introduction
------------

The package helps get the list of unique species available from a particular hotspot location from eBird.
The speciality is this is not using eBird API, which restricts data beyond 30 days old. This can pull 
from the web using wget (currently) to download html and processes it to get csv containing species.

This can be used to compare with individual own world lifer species csv or location/state/territory wise
lifer species, to know what is pending to see.

Download checklist
------------------

To download a location list, first the LocID is required. For example: L1890247 is the LocID for Lingabudhi Kere 
in Mysore or L2525708 is the LocID for Hessaraghatta Lakebed in Bangalore. LocID can be obtained by browsing 
ebird.org

```
bash download.sh L2525708 blore-hessaraghatta
```

This will download html, format in csv and store in data folder.

Compare your own
----------------

Assuming that your world lifer checklist has been downloaded from ebird.org and stored in data folder. 
pending.py will produce a list of species that is available in a specific location and _not_ in your
lifer list.

```
python bin/pending.py data/lifer.csv data/L2525708-blore-hessaraghatta.csv
```

Dependency
----------

This package requires an installation of wget command for downloading html from ebird.org. (This will be 
changed to pure python way of downloading file - in the backlog)


Copyright and License
---------------------
(C) Snehasis Sinha, 2016

This software is free for use, under Apache Licence 2.0
