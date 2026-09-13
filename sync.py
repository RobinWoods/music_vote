import os, json, re, requests
from imap_tools import MailBox, AND

MARK = "[PLANNER-SYNC]"

def create_issue(title, body):
    r = requests.post(
        f"https://api.github.com/repos/{os.environ['GH_REPO']}/issues",
        headers={"Authorization": f"Bearer {os.environ['GH_TOKEN']}",
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28"},
        json={"title": title, "body": body})
    r.raise_for_status()
    return r.json()["html_url"]

with MailBox(os.environ["MAIL_SERVER"]).login(
        os.environ["MAIL_USER"], os.environ["MAIL_PASS"]) as mb:
    all_msgs = list(mb.fetch(AND(seen=False), limit=20))
    print(f"Mails non-lus trouvés : {len(all_msgs)}")
    for msg in all_msgs:
        print("---")
        print("SUBJECT:", repr(msg.subject))
        print("BODY   :", repr((msg.text or "")[:300]))
