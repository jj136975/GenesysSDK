from __future__ import annotations

from typing import Protocol
from serde import serde


@serde(rename_all='camelcase')
class AdjustableLiveSpeakerDetection:
    # The name of the event that triggered the ALSD evaluation (e.g., line.connect, speech.generic).
    event_name: str = ""
    # The output of the ALSD detector, evaluating whether there is likely a person on the call based on the above inputs, and if so, a person is detected early (person disposition name and speech.person analyzer result) and the associated action taken (e.g., speech.person postconnect entry in the disposition table has the action to transfer to a queue).
    is_person_likely: bool = False
    # Protocol line connect received (answered by a person, machine, busy, fax).
    line_connected: bool = False
    # Modes to tune between speed to live speaker detection vs accuracy.
    mode: str = ""
    # ISO 8601 formatted relative duration (e.g., PT30.8427419S for 30.8 seconds), calculated on line connect.
    preconnect_duration: str = ""
    # Number of tone.ring.* analyzer events detected during the call (expected mostly during pre-connect but the last ringback tone detection could potentially complete after line connect, which will increment totalRingbacks still).
    total_ringbacks: int = 0


@serde(rename_all='camelcase')
class DispositionParameters:
    # ALSD evaluation inputs and output (isPersonalLikely) of the ALSD detector the last time it ran on the call (could be multiple times)
    adjustable_live_speaker_detection: AdjustableLiveSpeakerDetection | None = None
