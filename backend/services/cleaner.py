from services.matcher import is_match


def reconcile(crm_data, calendar_data):
    result = []

    for crm in crm_data:

        matched = None

        for cal in calendar_data:

            if is_match(crm, cal):
                matched = cal
                break

        result.append({
            "crm": crm,
            "calendar": matched,
            "matched": matched is not None
        })

    return result