from vbeam.core import ElementGeometry, TransmittedWavefront, WaveData
from vbeam.fastmath import numpy as np
from vbeam.fastmath.traceable import traceable_dataclass
from vbeam.util.coordinate_systems import az_el_to_cartesian


@traceable_dataclass()
class PlaneWavefront(TransmittedWavefront):
    def __call__(
        self,
        sender: ElementGeometry,
        point_position: np.ndarray,
        wave_data: WaveData,
    ) -> float:
        diff = point_position - sender.position
        wave_direction = az_el_to_cartesian(
            azimuth=wave_data.azimuth, elevation=wave_data.elevation
        )
        return (
            diff[0] * wave_direction[0]
            + diff[1] * wave_direction[1]
            + diff[2] * wave_direction[2]
        )
