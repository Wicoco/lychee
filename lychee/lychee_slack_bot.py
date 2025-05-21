import os
import sys
import requests

def extract_broken_links(report_path):
    with open(report_path, encoding="utf-8") as f:
        lines = [line.strip() for line in f if "BROKEN" in line]
    return lines

def send_slack_message(webhook_url, message):
    data = {"text": message}
    requests.post(webhook_url, json=data)

if __name__ == "__main__":
    # Chemin passé en argument OU chemin par défaut dans lychee/
    if len(sys.argv) > 1:
        report_path = sys.argv[1]
    else:
        report_path = "lychee/lychee-report.txt"
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not (os.path.exists(report_path) and webhook_url):
        print("Missing report or webhook URL")
        exit(1)
    broken_links = extract_broken_links(report_path)
    if broken_links:
        message = ":warning: *Liens morts détectés par Lychee !* :warning:\n" + "\n".join(broken_links[:20])
    else:
        message = ":white_check_mark: Aucun lien mort détecté par Lychee !"
    send_slack_message(webhook_url, message)
