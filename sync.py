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
    # ne lit que les non-lus marqués ; les marque lus après traitement
    for msg in mb.fetch(AND(seen=False, subject=MARK)):
        m = re.search(r"---PLANNERDATA---\s*(\{.*?\})\s*---END---",
                      msg.text or "", re.S)
        if not m:
            continue
        data = json.loads(m.group(1))
        url = create_issue(data["title"], data.get("body", "") +
                            f"\n\n_Planner task: {data['taskId']}_")
        print("Créée:", url)
        mb.flag(msg.uid, ['\\Seen'], True)   # marque lu = traité
