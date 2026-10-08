#!/usr/bin/env python3
"""Validate relative resource links and portable package structure; stdlib only."""
from pathlib import Path
import json
import re
import sys

root=Path(__file__).resolve().parents[1]
errors=[]
required=['SKILL.md','agents/openai.yaml','VERSION','README.md','README.fa.md','THIRD_PARTY_NOTICES.md']
for name in required:
    if not (root/name).is_file(): errors.append('Missing '+name)
text=(root/'SKILL.md').read_text()
if not text.startswith('---\n') or len(text.split('---',2))<3: errors.append('Missing frontmatter')
else:
    front=text.split('---',2)[1]
    if not re.search(r'^name: seo-project-analyst$',front,re.M): errors.append('Incorrect skill name')
    if not re.search(r'^description: .+',front,re.M): errors.append('Missing description')
for path in root.rglob('*.md'):
    body=path.read_text()
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',body):
        if '://' in target or target.startswith('#'): continue
        resolved=(path.parent/target.split('#')[0]).resolve()
        if not resolved.is_relative_to(root): errors.append('Nonportable link '+str(path.relative_to(root))+': '+target)
        elif not resolved.exists(): errors.append('Broken link '+str(path.relative_to(root))+': '+target)
for path in root.rglob('*.json'):
    try: json.loads(path.read_text())
    except ValueError as exc: errors.append(str(path.relative_to(root))+': '+str(exc))
if errors:
    print('\n'.join(errors));sys.exit(1)
print('Package structure, JSON and relative links validated')
