from lxml import html
import re
import requests
from datetime import datetime 

CASE_DATE_PATTERN = r"[(A-Za-z)]*\s[\d]*,\s[\d]*"
URL = "https://egov.uscis.gov/casestatus/mycasestatus.do"
APP_RECEIPT_NUM = "appReceiptNum"
INIT_CASE_SEARCH = "initCaseSearch"
CASE_STATUS = "CHECK STATUS"
UPDATE_TEXT_XPATH = "/html/body/div[2]/form/div/div[1]/div/div/div[2]/div[3]/p/text()"
MISSING_URL_PATTEN = "','|', '"
TEXT_FILTER_PATTERN = r"['\[\]]"

def joke():
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')


def get_case_status(case_id):

    data = {APP_RECEIPT_NUM: case_id,
            INIT_CASE_SEARCH: CASE_STATUS}
    r = requests.post(URL, data=data)

    content = html.fromstring(r.content)
    text = str(content.xpath(UPDATE_TEXT_XPATH))
    if len(text) < 2:
        raise Exception("Please make sure you case id is valid")
        
    text = str(re.sub("','|', '", 'USCIS website', text))
    status_message = re.sub(r"['\[\]]", ' ', text)
    
    p = re.search(CASE_DATE_PATTERN, status_message)
    if p is not None:
        match = p.group(0)
        last_update_date = datetime.strptime(str(match), "%B %d, %Y")
        last_update_date = last_update_date.strftime('%m/%d/%Y')

        return status_message, last_update_date

    else:
        raise Exception("Please make sure you case id is valid")