#!/usr/bin/env python3
"""Opt-in HTTP availability checks. Does not assert paper metadata correctness."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from build import ROOT, read_sources


def check(url):
    try:
        req=Request(url,headers={'User-Agent':'Mozilla/5.0 (research-map-link-check)'})
        with urlopen(req,timeout=20) as r:
            sample=r.read(256000).decode('utf-8',errors='replace')
            import re
            title=re.search(r'<title[^>]*>(.*?)</title>',sample,re.I|re.S)
            return {'url':url,'final_url':r.url,'http_status':r.status,'result':'reachable','page_title':re.sub(r'\s+',' ',title[1]).strip() if title else None}
    except HTTPError as e:
        return {'url':url,'http_status':e.code,'result':'needs_review','reason':'HTTP response requires manual review'}
    except Exception as e:
        return {'url':url,'http_status':None,'result':'needs_review','reason':type(e).__name__}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    papers,_,_=read_sources()
    urls=sorted({u for p in papers for u in [*p['links'].values(),p['publication']['source_url'],p['code']['url'],p['public_note']] if u})
    with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(check,urls))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps({'meaning':'HTTP availability only; not a content review','results':results},ensure_ascii=False,indent=2)+'\n')
    print(f"Checked {len(urls)} URLs: {sum(r['result']=='reachable' for r in results)} reachable, {sum(r['result']=='needs_review' for r in results)} need review")
