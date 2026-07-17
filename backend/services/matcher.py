def is_match(crm, calendar):

    crm_date = crm.get("meeting_date", "")
    cal_date = calendar.get("start_time", "")[:10]

    crm_subject = crm.get("subject", "").lower()
    cal_title = calendar.get("title", "").lower()

    if crm_date == cal_date and crm_subject in cal_title:
        return True

    return False