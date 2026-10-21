import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build import ROOT, read_sources, render, write_outputs, BEGIN, END
from export_public import export
from validate import validate_data, validate_links


class ResearchMapTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def tearDown(self):self.tmp.cleanup()
    def edit(self,fn):
        path=self.root/'data/papers.json';papers=json.loads(path.read_text());fn(papers);path.write_text(json.dumps(papers))
    def test_counts_and_references(self):
        self.assertEqual(validate_data(self.root),30)
        self.assertGreater(validate_links(self.root),100)
    def test_public_pages_are_english(self):
        for path, text in render(self.root).items():
            self.assertNotRegex(text, r'[\u3400-\u9fff]', path)
        self.assertNotIn('user_reading', (self.root/'data/papers.json').read_text())
    def test_missing_illustration_rejected(self):
        (self.root/'assets/research-map.svg').unlink()
        with self.assertRaisesRegex(ValueError, 'Missing local link'):
            validate_links(self.root)
    def test_bibliography_identity_and_author_validation(self):
        from build import bibliography
        papers,_,_=read_sources(self.root)
        text=bibliography(papers)
        import re
        self.assertEqual(set(re.findall(r'^@\w+\{([^,]+),',text,re.M)),{p['id'] for p in papers})
        self.assertIn('Thomas Kipf and Ethan Fetaya',text)
        self.assertIn('@inproceedings{context-diversity,',text)
        self.edit(lambda p:p[0]['bibliography'].update(authors=[]))
        with self.assertRaisesRegex(ValueError,'Missing verified authors'):validate_data(self.root)
    def test_unmarked_bibliography_not_overwritten(self):
        path=self.root/'references.bib';path.write_text('Manual bibliography')
        with self.assertRaisesRegex(ValueError,'Refusing to overwrite unmarked bibliography'):write_outputs(self.root)
        self.assertEqual(path.read_text(),'Manual bibliography')
    def test_duplicate_alias_rejected(self):
        self.edit(lambda p:p[0]['aliases'].append(p[1]['canonical_title']))
        with self.assertRaisesRegex(ValueError,'Duplicate title'):validate_data(self.root)
    def test_duplicate_arxiv_rejected(self):
        self.edit(lambda p:p[0].update(arxiv_id=p[1]['arxiv_id']))
        with self.assertRaisesRegex(ValueError,'Duplicate arXiv'):validate_data(self.root)
    def test_invalid_cross_reference_rejected(self):
        self.edit(lambda p:p[0]['secondary_modules'].append(p[0]['primary_module']))
        with self.assertRaisesRegex(ValueError,'cross references'):validate_data(self.root)
    def test_build_idempotent_and_manual_text_preserved(self):
        path=self.root/'README.md';path.write_text('Manual introduction\n'+path.read_text()+'\nManual footer\n')
        before=path.read_bytes();write_outputs(self.root);write_outputs(self.root)
        self.assertEqual(before,path.read_bytes())
        self.assertEqual(write_outputs(self.root,check=True),[])
    def test_unmarked_file_not_overwritten(self):
        path=self.root/'README.md';path.write_text('Manual content')
        with self.assertRaisesRegex(ValueError,'Refusing'):write_outputs(self.root)
        self.assertEqual(path.read_text(),'Manual content')
    def test_private_fields_and_unlisted_files_not_exported(self):
        secret='TEST_PRIVATE_SENTINEL_93810'
        self.edit(lambda p:p[0].update(user_reading={'status':'untracked','private_url':'https://private.feishu.cn/doc/'+secret},private_note=secret))
        (self.root/'local_state.json').write_text(secret)
        (self.root/'private').mkdir(exist_ok=True);(self.root/'private/idea.md').write_text(secret)
        (self.root/'public_notes').mkdir(exist_ok=True);(self.root/'public_notes/unlisted.md').write_text(secret)
        out=Path(self.tmp.name)/'public';files=export(self.root,out)
        self.assertEqual(len(files),21)
        self.assertNotIn(secret,'\n'.join(p.read_text() for p in out.rglob('*') if p.is_file()))
        self.assertFalse((out/'data').exists())
    def test_manifest_rejects_path_escape(self):
        (self.root/'publish-manifest.json').write_text(json.dumps({'notes':[{'title':'x','path':'public_notes/../local_state.json'}]}))
        with self.assertRaises(ValueError):render(self.root)
    def test_manifest_rejects_symlink_escape(self):
        outside=Path(self.tmp.name)/'private.md';outside.write_text('TEST_SECRET')
        (self.root/'public_notes').mkdir(exist_ok=True);(self.root/'public_notes/linked.md').symlink_to(outside)
        (self.root/'publish-manifest.json').write_text(json.dumps({'notes':[{'title':'x','path':'public_notes/linked.md'}]}))
        with self.assertRaises(ValueError):render(self.root)
    def test_private_url_in_public_field_rejected(self):
        self.edit(lambda p:p[0].update(public_note='https://private.feishu.cn/doc/test'))
        with self.assertRaisesRegex(ValueError,'Private'):validate_data(self.root)
    def test_verified_run_requires_receipt(self):
        self.edit(lambda p:p[0].update(reproduction={'status':'verified'}))
        with self.assertRaisesRegex(ValueError,'evidence'):validate_data(self.root)
    def test_export_refuses_nonempty_destination(self):
        out=Path(self.tmp.name)/'public';out.mkdir();(out/'private.md').write_text('TEST_SECRET')
        with self.assertRaises(ValueError):export(self.root,out)


if __name__=='__main__':unittest.main()
