import yaml,glob,collections,os
R=yaml.safe_load(open('K-ranked-all.yaml'))
verd={}
for f in sorted(glob.glob('J-verdicts-*.yaml')):
    j=os.path.basename(f)[11:-5]
    for e in yaml.safe_load(open(f)): verd.setdefault(e['id'],{})[j]=e
def vcell(i):
    v=verd.get(i)
    if not v: return ''
    vs=[x['verdict'] for x in v.values()]
    if len(set(vs))==1: return f"{vs[0]} ({'/'.join(f'{x['confidence']:.1f}' for x in v.values())})"
    return 'split: '+', '.join(f'{k}={x["verdict"]}' for k,x in v.items())
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
g=collections.Counter(x.get('grounded') for x in R)
spec=[x['id'] for x in R if x.get('already_specified')]
rows=[x for x in R if not x.get('already_specified')]
persp=collections.Counter(x['id'].rsplit('-',1)[0] for x in R)
with open('leaves.md','w') as f:
    f.write('# User Test agent page — gaps (full mode)\n\n')
    f.write(f"{len(R)} leaves after merge ({len(rows)} in table; already specified: {len(spec)} {spec}). Grounded: {g.get('quote',0)} quote / {g.get('inferred',0)} inferred / {g.get('speculative',0)} speculative. Priority = severity x occurrence x detectability, median of 3 independent scorings. Verdict = contest judges on the top 25 (keep / defer / accept / reject).\n\n")
    f.write('| # | id | title | cell | grounded | evidence | S | O | D | cost | priority | verdict | also_from | proposed |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n')
    for n,x in enumerate(rows,1):
        s=x.get('scores') or {}
        cell=x.get('cell') or {}
        keys=['surface','mode','run-status','videos-selected','video-state','action']
        cs=[]
        for k in keys:
            if k in cell:
                v=cell[k]; cs.append(','.join(map(str,v)) if isinstance(v,list) else str(v))
        for k,v in cell.items():
            if k not in keys and 'off-axis' in k: cs.append(f"{k.split(' ')[0]}={v}")
        ev=x.get('evidence') or 'none'; ev=str(ev)[:70]
        f.write(f"| {n} | {x['id']} | {esc(x['title'])} | {esc('; '.join(cs[:4]))} | {x.get('grounded','')} | {esc(ev)} | {s.get('severity','')} | {s.get('occurrence','')} | {s.get('detectability','')} | {s.get('cost_to_address','')} | {int(x.get('priority',0))} | {vcell(x['id'])} | {len(x.get('also_from') or [])} | {esc(str(x.get('proposed',''))[:140])} |\n")
    f.write('\n## Check against known misses\n')
    f.write('- miss-001 (white play icon on white thumbnail): equivalents are lowvision-25 (status badges distinguished by hue only) and the low-vision leaves on selected-state overlays over white thumbnails; see ids starting `lowvision-`.\n')
    f.write('- miss-002 (batch with some failures, no partial state): equivalents are backend-3 (one silent video in a 20-video report), consumer-11 (report with 2 of 8 unusable exported as complete), contract-4 (denominator after an unusable video), and the qa-lead per-video-outcome leaves.\n')
    f.write('\n## Audit: expert-missing items (from H-audit-1.yaml, now covered by the fill where noted)\n')
    H=yaml.safe_load(open('H-audit-1.yaml'))
    for e in H.get('expert_missing',[]): f.write(f'- {e}\n')
    f.write('\n## Run stats\n')
    f.write(f"- perspectives run: 29 of 29 (20 written, 9 added by the critique stage)\n- axes: 18, values: 257 (6 axes and 85 values added by the critique)\n- raw leaves: 1225 first pass + 155 targeted fill = 1380\n- contract rejections: 0\n- duplicates: 381 in-bucket + 48 cross-bucket + 11 in fill = 440\n- surviving: {len(R)}\n- fill yield: 144 new / 796 = 0.18 (audit estimated 0.08)\n- scoring: 3 runs per leaf, median; 10 of 3184 first-pass field scores had spread >= 3\n- top-25 contest: 2 judges\n- leaves per perspective (surviving): " + ', '.join(f'{k} {v}' for k,v in persp.most_common()) + '\n')
print('rows',len(rows),'verdict files',len(glob.glob('J-verdicts-*.yaml')))
