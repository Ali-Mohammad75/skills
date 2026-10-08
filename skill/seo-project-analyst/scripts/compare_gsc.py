#!/usr/bin/env python3
"""Compare strict normalized GSC CSV snapshots; stdlib only, no network writes."""
import argparse
import csv
from datetime import date
import json
import math
from pathlib import Path
import sys


def read_rows(path, keys):
    data = {}
    with open(path, encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        required = set(keys) | {'clicks', 'impressions', 'position'}
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError('CSV headers must exist and be unique')
        if not required.issubset(reader.fieldnames):
            raise ValueError('Missing columns: ' + ', '.join(sorted(required - set(reader.fieldnames))))
        for line, row in enumerate(reader, 2):
            if None in row or any(v is None for v in row.values()):
                raise ValueError(f'CSV row {line}: wrong column count')
            key = tuple(row[k] for k in keys)
            if any(not k.strip() for k in key) or key in data:
                raise ValueError(f'CSV row {line}: empty or duplicate dimension key')
            try:
                clicks = float(row['clicks'])
                impressions = float(row['impressions'])
                position = float(row['position']) if row['position'].strip() else None
            except (ValueError, TypeError) as exc:
                raise ValueError(f'CSV row {line}: use plain decimal numeric values') from exc
            if not all(math.isfinite(x) and x >= 0 and x.is_integer() for x in (clicks, impressions)):
                raise ValueError(f'CSV row {line}: counts must be finite nonnegative integers')
            if clicks > impressions:
                raise ValueError(f'CSV row {line}: clicks exceed impressions')
            if position is not None and (not math.isfinite(position) or position < 0):
                raise ValueError(f'CSV row {line}: invalid position')
            if impressions and (position is None or position < 1):
                raise ValueError(f'CSV row {line}: positive impressions require position >= 1')
            data[key] = {'clicks': int(clicks), 'impressions': int(impressions),
                         'ctr': clicks / impressions if impressions else None,
                         'position': position if impressions else None}
    return data


def validate_meta(meta, keys):
    scope = ('property', 'search_type', 'filters', 'dimensions', 'timezone')
    for period in ('before', 'current'):
        m = meta[period]
        for field in scope + ('start', 'end', 'coverage'):
            if field not in m:
                raise ValueError(f'{period}: missing metadata {field}')
        if m['dimensions'] != keys or m['coverage'] not in ('complete', 'limited', 'unknown'):
            raise ValueError(f'{period}: invalid dimensions or coverage')
        if not isinstance(m['filters'], dict):
            raise ValueError(f'{period}: filters must be an object')
        if not all(isinstance(m[f], str) and m[f].strip() for f in ('property', 'search_type', 'timezone')):
            raise ValueError(f'{period}: scope fields must be nonempty strings')
        if m['search_type'].lower() == 'discover':
            raise ValueError('Discover has no compatible average position; use its own report')
    if any(meta['before'][k] != meta['current'][k] for k in scope):
        raise ValueError('Period scope mismatch: property/type/filters/dimensions/timezone')
    b0, b1, c0, c1 = [date.fromisoformat(meta[p][f]) for p, f in
                      [('before','start'), ('before','end'), ('current','start'), ('current','end')]]
    if b1 < b0 or c1 < c0 or c0 <= b1 or (b1-b0) != (c1-c0):
        raise ValueError('Use equal-length, ordered, nonoverlapping periods')
    return (b1-b0).days + 1


def compare(before_path, current_path, meta, keys):
    days = validate_meta(meta, keys)
    before, current = read_rows(before_path, keys), read_rows(current_path, keys)
    rows = []
    for key in sorted(before.keys() | current.keys()):
        b, c = before.get(key), current.get(key)
        delta = None
        if b is not None and c is not None:
            delta = {'clicks': c['clicks']-b['clicks'], 'impressions': c['impressions']-b['impressions'],
                     'clicks_pct': (c['clicks']/b['clicks']-1)*100 if b['clicks'] else None,
                     'ctr_percentage_points': (c['ctr']-b['ctr'])*100 if c['ctr'] is not None and b['ctr'] is not None else None,
                     'position': c['position']-b['position'] if c['position'] is not None and b['position'] is not None else None}
        rows.append({'key': dict(zip(keys,key)), 'before': b, 'current': c, 'delta': delta,
                     'presence': 'both' if b is not None and c is not None else 'before_only' if b is not None else 'current_only'})
    def totals(data):
        clicks = sum(r['clicks'] for r in data.values())
        impressions = sum(r['impressions'] for r in data.values())
        return {'clicks': clicks, 'impressions': impressions,
                'ctr': clicks/impressions if impressions else None,
                'position': sum((r['position'] or 0)*r['impressions'] for r in data.values())/impressions if impressions else None,
                'rows': len(data)}
    return {'metadata': meta, 'days_per_period': days,
            'inputs': {'before': Path(before_path).name, 'current': Path(current_path).name},
            'limitations': ['Totals are export-row aggregates, not guaranteed property totals.',
                           'Missing rows remain unknown, even when coverage is declared complete.',
                           'Changes are descriptive, not causal; position delta below zero means improvement.',
                           'CTR is a fraction; CTR delta is in percentage points. No automatic pruning decisions.'],
            'export_totals': {'before': totals(before), 'current': totals(current)}, 'rows': rows}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('before')
    p.add_argument('current')
    p.add_argument('--metadata', required=True)
    p.add_argument('--keys', nargs='+', required=True, choices=('page','query','country','device','date','search_appearance'))
    args = p.parse_args()
    try:
        if len(args.keys) != len(set(args.keys)) or 'date' in args.keys:
            raise ValueError('Use unique comparison dimensions without date; aggregate periods first')
        meta = json.loads(Path(args.metadata).read_text(encoding='utf-8'))
        result = compare(args.before, args.current, meta, args.keys)
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    except (OSError, ValueError, KeyError, TypeError, csv.Error) as exc:
        print('Input error: ' + str(exc), file=sys.stderr)
        return 2
    return 0

if __name__ == '__main__':
    sys.exit(main())
