from __future__ import annotations

from serde import serde

from .analytics_session import AnalyticsSession


@serde(rename_all='camelcase')
class AnalyticsParticipantWithoutAttributes:
    # External contact identifier
    external_contact_id: str = ""
    # External organization identifier
    external_organization_id: str = ""
    # Reason for which participant flagged conversation
    flagged_reason: str = ""
    # Unique identifier for the participant
    participant_id: str = ""
    # A human readable name identifying the participant
    participant_name: str = ""
    # The participant's purpose
    purpose: str = ""
    # Flag determining if a screen recording was started or not
    screen_recording: bool = False
    # List of sessions associated to this participant
    sessions: list[AnalyticsSession] | None = None
    # The team ID the user is a member of
    team_id: str = ""
    # Unique identifier for the user
    user_id: str = ""
