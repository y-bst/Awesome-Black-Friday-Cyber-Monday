import yaml,glob,collections,os,statistics
F=['impact','confidence','willingness','cost','moat']
scores=collections.defaultdict(lambda: collections.defaultdict(list))
for f in glob.glob('K-scores-*-run*.yaml'):
    for e in yaml.safe_load(open(f)) or []:
        for k in F:
            if e.get(k) is not None: scores[e['id']][k].append(float(e[k]))
leaves={}
for n in range(1,8):
    p=f'I-verified-{n}.yaml'
    if not os.path.exists(p): p=f'G-merged-{n}.yaml'
    for it in yaml.safe_load(open(p)):
        if isinstance(it,dict) and 'id' in it: it['bucket']=n; leaves[it['id']]=it
# cross-bucket dedupe
if os.path.exists('G-crossdupes.yaml'):
    cd=yaml.safe_load(open('G-crossdupes.yaml')) or {}
    for c in cd.get('duplicates',[]) or []:
        s=c['survivor']
        for m in c['merged']:
            if m in leaves and s in leaves:
                leaves[s].setdefault('also_from',[]); leaves[s]['also_from']=list(leaves[s]['also_from'] or [])+[m]+list(leaves[m].get('also_from') or [])
                del leaves[m]
    for c in cd.get('contested',[]) or []:
        if c['positive'] in leaves:
            leaves[c['positive']].setdefault('contested_by',[]); leaves[c['positive']]['contested_by']=list(leaves[c['positive']]['contested_by'] or [])+list(c['refusals'])
    for c in cd.get('variants',[]) or []:
        for v in c['variants']:
            if v in leaves and not leaves[v].get('variants_of'): leaves[v]['variants_of']=c['of']
verd={}
for f in sorted(glob.glob('J-verdicts-*.yaml')):
    j=os.path.basename(f)[11:-5]
    for e in yaml.safe_load(open(f)): verd.setdefault(e['id'],{})[j]=e
for i,it in leaves.items():
    m={k:statistics.median(v) for k,v in scores.get(i,{}).items() if v}
    it['scores']=m if len(m)==5 else None
    it['priority']=m['impact']*m['confidence']*m['willingness'] if it['scores'] else 0
def vcell(i):
    v=verd.get(i)
    if not v: return ''
    vs=[x['verdict'] for x in v.values()]
    return vs[0] if len(set(vs))==1 else 'split: '+', '.join(f'{k}={x["verdict"]}' for k,x in v.items())
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
R=sorted(leaves.values(),key=lambda x:(-x['priority'],x['scores']['cost'] if x['scores'] else 9,-(x['scores']['moat'] if x['scores'] else 0)))
pos=[x for x in R if not x.get('refusal')]
ref=[x for x in R if x.get('refusal')]
g=collections.Counter(x.get('grounded') for x in R)
offered=[x['id'] for x in R if x.get('already_offered')]
with open('options.md','w') as f:
    f.write('# AI analysis of gameplay video: options a gaming company would pay for (ideate, full mode)\n\n')
    f.write(f"{len(R)} options after merge: {len(pos)} positive, {len(ref)} refusals (a buyer persona said no; kept as signal). Grounded in the research notes: {g.get('quote',0)} quote / {g.get('inferred',0)} inferred / {g.get('speculative',0)} speculative. Already offered by a named vendor: {len(offered)}. Priority = impact x confidence x willingness-to-pay, median of 3 independent scorings; cost and moat shown. Verdict = contest judges on the top 25.\n\n")
    f.write('## Positive options, ranked\n\n| # | id | option | buyer | input | grounded | I | C | W | cost | moat | priority | verdict | contested by | variants of | offered by | why existing tools cannot |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n')
    for n,x in enumerate(pos,1):
        s=x.get('scores') or {}
        f.write(f"| {n} | {x['id']} | {esc(x['title'])} | {esc(str(x.get('buyer',''))[:60])} | {esc(str(x.get('input',''))[:60])} | {x.get('grounded','')} | {s.get('impact','')} | {s.get('confidence','')} | {s.get('willingness','')} | {s.get('cost','')} | {s.get('moat','')} | {int(x.get('priority',0))} | {vcell(x['id'])} | {esc(','.join(x.get('contested_by') or []))} | {x.get('variants_of','') or ''} | {esc(x.get('already_offered_by','') or '')} | {esc(str(x.get('why_existing_tools_cannot',''))[:120])} |\n")
    f.write('\n## Refusals (what buyers said they would NOT pay for, and why)\n\n| id | option | persona | why not |\n|---|---|---|---|\n')
    for x in ref:
        f.write(f"| {x['id']} | {esc(x['title'])} | {esc(str(x.get('perspective') or x['id'].rsplit('-',1)[0]))} | {esc(str(x.get('consequence',''))[:160])} |\n")
    if os.path.exists('H-audit-1.yaml'):
        H=yaml.safe_load(open('H-audit-1.yaml'))
        f.write('\n## Audit: mode-collapse clusters (many perspectives proposed the same thing)\n')
        for c in H.get('mode_collapse',[]) or []: f.write(f"- {esc(c.get('theme'))} (about {c.get('approx_count')}; e.g. {', '.join(c.get('example_ids',[])[:4])})\n")
        f.write('\n## Audit: contested themes\n')
        for c in H.get('contested_themes',[]) or []: f.write(f"- {esc(c.get('theme'))}: {esc(c.get('disagreement'))}\n")
        f.write('\n## Audit: expert-missing options\n')
        for e in H.get('expert_missing',[]) or []: f.write(f'- {esc(e)}\n')
    f.write('\n## Run stats\n')
    f.write(f"- perspectives: 35 (20 written, 15 added by the critique stage, including the deal-blockers and external buyers)\n- axes: 17 solution-space axes, 227 values\n- research notes: 4, ~13,700 words, ~300 cited URLs (search-extract based; vendor pages were unreachable from the sandbox)\n- raw options: 997 + 71 targeted fill; merged inside buckets: 943 + 70; after cross-bucket dedupe: {len(R)}\n- scoring: 3 runs per option, medians by script\n")
print('options',len(R),'positive',len(pos),'refusals',len(ref),'scored',sum(1 for x in R if x['scores']),'verdict files',len(glob.glob('J-verdicts-*.yaml')))
