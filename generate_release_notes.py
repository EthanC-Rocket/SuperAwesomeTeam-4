import os
import re
from datetime import datetime

RELEASE_NOTES_FILE = 'RELEASE_NOTES.md'

CATEGORY_PATTERNS = {
    'Features': re.compile(r'\b(feature|add(ed)?|implement(ed)?|new)\b', re.IGNORECASE),
    'Fixes': re.compile(r'\b(fix(ed)?|bug|resolve(d)?|correct(ed)?)\b', re.IGNORECASE),
    'Improvements': re.compile(r'\b(refactor(ed)?|improve(d)?|optimi(s|z)ed?|update(d)?|enhance(d)?)\b', re.IGNORECASE),
    'Documentation': re.compile(r'\b(doc(s|umentation)?|readme|comment(s)?)\b', re.IGNORECASE)
}

def get_commit_history():
    # Get commit messages from git log
    stream = os.popen('git log --pretty=format:"%s"')
    commits = stream.read().strip().split('\n')
    return commits

def categorize_commits(commits):
    categorized = {cat: [] for cat in CATEGORY_PATTERNS}
    for msg in commits:
        matched = False
        for cat, pattern in CATEGORY_PATTERNS.items():
            if pattern.search(msg):
                categorized[cat].append(msg)
                matched = True
                break
        if not matched:
            categorized.setdefault('Other', []).append(msg)
    return categorized

def generate_release_notes(categorized, version=None):
    now = datetime.now().strftime('%B %d, %Y')
    version = version or f"Unreleased ({now})"
    lines = [f"# 📝 Release Notes\n", f"## {version}\n"]
    for cat in ['Features', 'Fixes', 'Improvements', 'Documentation', 'Other']:
        items = categorized.get(cat, [])
        if items:
            lines.append(f"### {cat}\n")
            for item in items:
                lines.append(f"- {item}")
            lines.append("")
    return '\n'.join(lines)

def main():
    commits = get_commit_history()
    categorized = categorize_commits(commits)
    notes = generate_release_notes(categorized)
    with open(RELEASE_NOTES_FILE, 'w', encoding='utf-8') as f:
        f.write(notes)
    print(f"Release notes written to {RELEASE_NOTES_FILE}")

if __name__ == '__main__':
    main()
