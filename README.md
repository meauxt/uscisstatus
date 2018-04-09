# USCIS Status Checker
A Python package that let you scrape the USCIS website and get the latest status on case

## Usage :
import uscisstatus

uscistatus.get_case_status("CASE_ID")

the get_case_status() will return a dictionary with the following values :
date : the date that the status updated
status : the status message  