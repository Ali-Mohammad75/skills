import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('compare_gsc', ROOT/'scripts/compare_gsc.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.meta = json.loads((ROOT/'assets/gsc-metadata.example.json').read_text())
        self.a = self.root/'before.csv'; self.b = self.root/'current.csv'
        self.a.write_text('page,clicks,impressions,position\nhttps://example.com/a,10,100,5\nhttps://example.com/b,9,900,10\n')
        self.b.write_text('page,clicks,impressions,position\nhttps://example.com/a,20,200,4\nhttps://example.com/c,2,10,1\n')
    def run_compare(self):
        return m.compare(self.a,self.b,self.meta,['page'])
    def test_weighted_metrics(self):
        r=self.run_compare()
        self.assertAlmostEqual(r['export_totals']['before']['ctr'],.019)
        self.assertAlmostEqual(r['export_totals']['before']['position'],9.5)
        self.assertEqual(r['rows'][0]['delta']['clicks'],10)
        self.assertEqual(r['rows'][0]['delta']['position'],-1)
    def test_missing_not_zero(self):
        r=self.run_compare()['rows']
        self.assertIsNone(r[1]['current']); self.assertIsNone(r[1]['delta'])
        self.assertIsNone(r[2]['before']); self.assertIsNone(r[2]['delta'])
    def test_zero_baseline(self):
        self.a.write_text('page,clicks,impressions,position\nhttps://example.com/a,0,0,\n')
        r=self.run_compare()['rows'][0]
        self.assertIsNone(r['delta']['clicks_pct'])
        self.assertIsNone(r['before']['ctr'])
    def test_duplicate_keys_rejected(self):
        with self.a.open('a') as f: f.write('https://example.com/a,10,100,5\n')
        with self.assertRaises(ValueError): self.run_compare()
    def test_scope_mismatch_rejected(self):
        self.meta['current']['property']='sc-domain:other.example'
        with self.assertRaises(ValueError): self.run_compare()
    def test_overlap_rejected(self):
        self.meta['current']['start']='2026-07-28'
        with self.assertRaises(ValueError): self.run_compare()
    def test_bad_numbers_rejected(self):
        for value in ['NaN','inf','-1','1.5','101']:
            with self.subTest(value=value):
                self.a.write_text(f'page,clicks,impressions,position\nhttps://example.com/a,{value},100,5\n')
                with self.assertRaises(ValueError): self.run_compare()
    def test_persian_key_preserved(self):
        self.meta['before']['dimensions']=self.meta['current']['dimensions']=['query']
        text='query,clicks,impressions,position\nتعمیر کولر گازی,10,100,5\n'
        self.a.write_text(text,encoding='utf-8-sig');self.b.write_text(text,encoding='utf-8')
        r=m.compare(self.a,self.b,self.meta,['query'])
        self.assertEqual(r['rows'][0]['key']['query'],'تعمیر کولر گازی')
    def test_cli_json_and_error_exit(self):
        meta=self.root/'metadata.json';meta.write_text(json.dumps(self.meta))
        cmd=[sys.executable,str(ROOT/'scripts/compare_gsc.py'),str(self.a),str(self.b),'--metadata',str(meta),'--keys','page']
        r=subprocess.run(cmd,capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr);self.assertEqual(len(json.loads(r.stdout)['rows']),3)
        self.a.write_text('wrong,header\n1,2\n')
        r=subprocess.run(cmd,capture_output=True,text=True)
        self.assertEqual(r.returncode,2);self.assertEqual(r.stdout,'')

if __name__=='__main__': unittest.main()
