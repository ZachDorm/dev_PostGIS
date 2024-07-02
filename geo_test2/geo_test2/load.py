from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import States

states_mapping = {
    "NAME":"NAME",
    "STUSPS":"STUSPS",
    "mpoly" :"MULTIPOLYGON",
}

#world_shp = Path(__file__).resolve().parent / "data" / "TM_WORLD_BORDERS-0.3.shp"
states_shp = "C:/data/cb_2018_us_state_20m.shp"

def run(verbose=True):
    lm = LayerMapping(States, states_shp, states_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
