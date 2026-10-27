import yaml,glob,collections,os,statistics
F=['impact','confidence','fit','cost','query_speed']
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
    for c in cd.get('contested',[]) or []:
        if c['positive'] in leaves: leaves[c['positive']]['contested_by']=list(leaves[c['positive']].get('contested_by') or [])+list(c['refusals'])
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
    it['priority']=m['impact']*m['confidence']*m['query_speed'] if it['scores'] else 0
def vcell(i):
    v=verd.get(i)
    if not v: return ''
    vs=[x['verdict'] for x in v.values()]
    return vs[0] if len(set(vs))==1 else 'split: '+', '.join(f'{k}={x["verdict"]}' for k,x in v.items())
def esc(s): return str(s).replace('|','\\|').replace('\n',' ')
def isref(x): return bool(x.get('refusal')) or str(x.get('title','')).upper().startswith('REFUSED') or str(x.get('willingness','')).lower() in ('1','low')
R=sorted(leaves.values(),key=lambda x:(-x['priority'],x['scores']['cost'] if x['scores'] else 9,-(x['scores']['fit'] if x['scores'] else 0)))
yaml.safe_dump(R,open('K-ranked-all.yaml','w'),sort_keys=False,allow_unicode=True,width=120)
pos=[x for x in R if not isref(x)]; ref=[x for x in R if isref(x)]
g=collections.Counter(x.get('grounded') for x in R)
parts=collections.Counter(str(x.get('part','')) for x in pos)
with open('options.md','w') as f:
    f.write('# JEV architecture: how to store, query and generate questions so any studio question is answerable fast (ideate, full mode)\n\n')
    f.write(f"{len(R)} options after merge: {len(pos)} positive, {len(ref)} refusals (a persona said no; kept as signal). Grounded in spec/memo: {g.get('quote',0)} quote / {g.get('inferred',0)} inferred / {g.get('speculative',0)} speculative. Priority = impact x confidence x query_speed, median of 3 independent scorings; fit (5 = reuses the existing pipeline) and cost (1 = weeks .. 5 = multi-quarter) shown. Verdict = contest judges on the top 25.\n\n")
    f.write('Positive options by part: ' + ', '.join(f'{k} {v}' for k,v in parts.most_common()) + '\n\n')
    f.write('## Positive options, ranked\n\n| # | id | option | part | mechanism | grounded | I | C | fit | cost | Q | priority | verdict | contested by | variants of | better than fixed table |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n')
    for n,x in enumerate(pos,1):
        s=x.get('scores') or {}
        f.write(f"| {n} | {x['id']} | {esc(x['title'])} | {esc(str(x.get('part','')))} | {esc(str(x.get('mechanism',''))[:140])} | {x.get('grounded','')} | {s.get('impact','')} | {s.get('confidence','')} | {s.get('fit','')} | {s.get('cost','')} | {s.get('query_speed','')} | {int(x.get('priority',0))} | {vcell(x['id'])} | {esc(','.join(x.get('contested_by') or []))} | {x.get('variants_of','') or ''} | {esc(str(x.get('better_than_fixed_table',''))[:120])} |\n")
    f.write('\n## Refusals (what a persona said NOT to build, and why)\n\n| id | option | persona | why not |\n|---|---|---|---|\n')
    for x in ref:
        f.write(f"| {x['id']} | {esc(x['title'])} | {esc(str(x.get('perspective') or x['id'].rsplit('-',1)[0]))} | {esc(str(x.get('consequence',''))[:160])} |\n")
    if os.path.exists('H-audit-1.yaml'):
        H=yaml.safe_load(open('H-audit-1.yaml'))
        f.write('\n## Audit: mode-collapse clusters\n')
        for c in H.get('mode_collapse',[]) or []: f.write(f"- {esc(c.get('theme'))} (about {c.get('approx_count')}; e.g. {', '.join((c.get('example_ids') or [])[:4])})\n")
        f.write('\n## Audit: contested themes\n')
        for c in H.get('contested_themes',[]) or []: f.write(f"- {esc(c.get('theme'))}: {esc(c.get('disagreement'))}\n")
        f.write('\n## Audit: expert-missing options\n')
        for e in H.get('expert_missing',[]) or []: f.write(f'- {esc(e)}\n')
    f.write('\n## Run stats\n')
    f.write(f"- perspectives: 30 (18 written, 12 added by the critique stage: observability, call-centre analytics, UXR repository vendor, clinical abstraction, e-discovery, video search, studio data team, studio security, publisher, platform owner, playtest ops, GUR lead)\n- axes: 22 solution-space axes, 312 values (critique added 10 axes)\n- raw options: 998 from 30 perspectives; 868 after in-bucket merge; 835 after cross-bucket dedupe; +69 from the audit fill (non-tutorial play structure and expert-missing items) = {len(R)}\n- framing check: the audit found 86% of options used a tutorial example; the fill required non-tutorial examples\n- scoring: 3 runs per option, medians by script; contest on top 25 with 2 judges\n")
print('options',len(R),'positive',len(pos),'refusals',len(ref),'scored',sum(1 for x in R if x['scores']),'verdict files',len(glob.glob('J-verdicts-*.yaml')))
