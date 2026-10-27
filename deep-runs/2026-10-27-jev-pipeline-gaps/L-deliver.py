import yaml,glob,collections,os,statistics
F=['severity','occurrence','detectability','cost_to_address']
scores=collections.defaultdict(lambda: collections.defaultdict(list))
for f in glob.glob('K-scores-*-run*.yaml'):
    for e in yaml.safe_load(open(f)) or []:
        for k in F:
            if e.get(k) is not None: scores[e['id']][k].append(float(e[k]))
leaves={}
for n in range(1,10):
    p=f'I-verified-{n}.yaml'
    if not os.path.exists(p): p=f'G-merged-{n}.yaml'
    if not os.path.exists(p): continue
    for it in yaml.safe_load(open(p)):
        if isinstance(it,dict) and 'id' in it: it['bucket']=n; leaves[it['id']]=it
if os.path.exists('G-crossdupes.yaml'):
    cd=yaml.safe_load(open('G-crossdupes.yaml')) or {}
    for c in cd.get('duplicates',[]) or []:
        s=c['survivor']
        for m in c['merged']:
            if m in leaves and s in leaves:
                leaves[s]['also_from']=list(leaves[s].get('also_from') or [])+[m]+list(leaves[m].get('also_from') or []); del leaves[m]
    for c in cd.get('variants',[]) or []:
        for v in c['variants']:
            if v in leaves and not leaves[v].get('variants_of'): leaves[v]['variants_of']=c['of']
verd={}
for f in sorted(glob.glob('J-verdicts-*.yaml')):
    j=os.path.basename(f)[11:-5]
    for e in yaml.safe_load(open(f)): verd.setdefault(e['id'],{})[j]=e
for i,it in leaves.items():
    m={k:statistics.median(v) for k,v in scores.get(i,{}).items() if v}
    it['scores']=m if len(m)==4 else None
    it['priority']=m['severity']*m['occurrence']*m['detectability'] if it['scores'] else 0
def vcell(i):
    v=verd.get(i)
    if not v: return ''
    vs=[x['verdict'] for x in v.values()]
    return vs[0] if len(set(vs))==1 else 'split: '+', '.join(f'{k}={x["verdict"]}' for k,x in v.items())
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
R=sorted(leaves.values(),key=lambda x:(-x['priority'],x['scores']['cost_to_address'] if x['scores'] else 9))
yaml.safe_dump(R,open('K-ranked-all.yaml','w'),sort_keys=False,allow_unicode=True,width=120)
g=collections.Counter(x.get('grounded') for x in R)
spec=[x['id'] for x in R if x.get('already_specified')]
rows=[x for x in R if not x.get('already_specified')]
persp=collections.Counter(x['id'].rsplit('-',1)[0] for x in R)
KEYS=['stage','data-element','session-shape','studio-question-type','correctness-failure','processing-status']
with open('leaves.md','w') as f:
    f.write('# JEV pipeline (video -> transcript -> fixed MCQ -> answers table -> chatbot): gaps, full mode\n\n')
    f.write(f"{len(R)} leaves after merge ({len(rows)} in table; already specified: {len(spec)}). Grounded in spec.md: {g.get('quote',0)} quote / {g.get('inferred',0)} inferred / {g.get('speculative',0)} speculative. Priority = severity x occurrence x detectability (FMEA), median of 3 independent scorings; cost = cost to address (1 prompt line .. 5 new subsystem). Verdict = contest judges on the top 25.\n\n")
    f.write('| # | id | title | cell | grounded | evidence | S | O | D | cost | priority | verdict | dup | proposed |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n')
    for n,x in enumerate(rows,1):
        s=x.get('scores') or {}; cell=x.get('cell') or {}
        cs=[]
        for k in KEYS:
            if k in cell:
                v=cell[k]; cs.append(','.join(map(str,v)) if isinstance(v,list) else str(v))
        ev=str(x.get('evidence') or 'none')[:70]
        f.write(f"| {n} | {x['id']} | {esc(x['title'])} | {esc('; '.join(cs[:4]))} | {x.get('grounded','')} | {esc(ev)} | {s.get('severity','')} | {s.get('occurrence','')} | {s.get('detectability','')} | {s.get('cost_to_address','')} | {int(x.get('priority',0))} | {vcell(x['id'])} | {len(x.get('also_from') or [])} | {esc(str(x.get('proposed',''))[:140])} |\n")
    if os.path.exists('H-audit-1.yaml'):
        H=yaml.safe_load(open('H-audit-1.yaml'))
        f.write('\n## Audit: expert-missing items\n')
        for e in H.get('expert_missing',[]) or []: f.write(f'- {esc(e)}\n')
        f.write('\n## Audit: mode-collapse clusters\n')
        for c in H.get('mode_collapse',[]) or []: f.write(f"- {esc(c.get('theme'))} (about {c.get('approx_count')}; e.g. {', '.join((c.get('example_ids') or [])[:4])})\n")
    f.write('\n## Run stats\n')
    f.write(f"- perspectives: 23 (18 written, 5 added by the critique stage)\n- axes: 20, values: 260 (critique added 6 axes)\n- raw leaves: 848; surviving after merge and cross-bucket dedupe: {len(R)}\n- scoring: 3 runs per leaf, medians by script; contest on top 25 with 2 judges\n- leaves per perspective (surviving): " + ', '.join(f'{k} {v}' for k,v in persp.most_common()) + '\n')
print('rows',len(rows),'scored',sum(1 for x in R if x['scores']),'verdict files',len(glob.glob('J-verdicts-*.yaml')))
