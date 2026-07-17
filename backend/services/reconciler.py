from services.matcher import is_match


def normalize_location(location):
    if not location:
        return ""

    location = location.lower()

    replacements = [
        "hq - ",
        "nyc office - ",
        "dc office - ",
        "conference room ",
        "room ",
    ]

    for text in replacements:
        location = location.replace(text, "")

    return location.strip()


def reconcile(crm_events, calendar_events):

    reconciled = []
    used_calendar = set()

    for crm in crm_events:

        matched_calendar = None

        for calendar in calendar_events:

            if calendar["event_id"] in used_calendar:
                continue

            if is_match(crm, calendar):
                matched_calendar = calendar
                used_calendar.add(calendar["event_id"])
                break

        crm_location = crm.get("location") or "N/A"

        calendar_location = (
            matched_calendar.get("location")
            if matched_calendar
            else "N/A"
        )

        conflict = False

        if matched_calendar:

            conflict = (
                normalize_location(crm_location)
                !=
                normalize_location(calendar_location)
            )

        reconciled.append({

            "crm_id": crm.get("crm_id"),

            "event_id":
                matched_calendar.get("event_id")
                if matched_calendar
                else None,

            "subject": crm.get("subject"),

            "client_name": crm.get("client_name") or "N/A",

            "client_company": crm.get("client_company") or "N/A",

            "meeting_date": crm.get("meeting_date"),

            "meeting_time": crm.get("meeting_time") or "N/A",

            "crm_location": crm_location,

            "calendar_location": calendar_location,

            "crm_status": crm.get("status"),

            "calendar_status":
                matched_calendar.get("status")
                if matched_calendar
                else "N/A",

            "matched": matched_calendar is not None,

            "conflict": conflict,

            "source":
                "Both"
                if matched_calendar
                else "CRM"

        })

    for calendar in calendar_events:

        if calendar["event_id"] in used_calendar:
            continue

        reconciled.append({

            "crm_id": calendar["event_id"],

            "event_id": calendar["event_id"],

            "subject": calendar.get("title"),

            "client_name": "N/A",

            "client_company": "N/A",

            "meeting_date": calendar["start_time"][:10],

            "meeting_time": calendar["start_time"][11:16],

            "crm_location": "N/A",

            "calendar_location": calendar.get("location") or "N/A",

            "crm_status": "N/A",

            "calendar_status": calendar.get("status"),

            "matched": False,

            "conflict": False,

            "source": "Calendar"

        })

    return reconciled