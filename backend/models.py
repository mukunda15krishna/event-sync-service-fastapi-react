from pydantic import BaseModel
from typing import Optional


class ReconciledMeeting(BaseModel):
    crm_id: Optional[str] = None
    event_id: Optional[str] = None

    subject: str
    meeting_date: str
    meeting_time: Optional[str] = None

    client_name: Optional[str] = None
    client_company: Optional[str] = None

    crm_location: Optional[str] = None
    calendar_location: Optional[str] = None

    crm_status: Optional[str] = None
    calendar_status: Optional[str] = None

    conflict: bool = False
    source: str