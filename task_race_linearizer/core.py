from functools import lru_cache
from .common import integer,unique_ids
STATES={'working','input_required','completed','failed','cancelled'}
def transition(state,op):
    if op=='poll':return state
    if state in ('completed','failed','cancelled'):return state
    if op in ('complete','fail','cancel'):return {'complete':'completed','fail':'failed','cancel':'cancelled'}[op]
    if op=='request_input':return 'input_required'
    if op=='resume':return 'working' if state=='input_required' else state
    raise ValueError('operation')
def run(data):
    events=data['operations'];initial=data.get('initial','working')
    if initial not in STATES or len(events)>18:raise ValueError('size_or_state')
    unique_ids(events);pred=[]
    for e in events:
        integer(e['call'],0,10**12);integer(e['return'],e['call']+1,10**12)
        if e['op'] not in ('poll','complete','fail','cancel','request_input','resume') or e['result'] not in STATES:raise ValueError('operation')
    for i,e in enumerate(events):pred.append(sum(1<<j for j,other in enumerate(events) if j!=i and other['return']<=e['call']))
    visited=[0]
    @lru_cache(None)
    def search(mask,state):
        visited[0]+=1
        if mask==(1<<len(events))-1:return ()
        for i,e in enumerate(events):
            if mask>>i&1 or pred[i]&mask!=pred[i]:continue
            next_state=transition(state,e['op'])
            if next_state!=e['result']:continue
            rest=search(mask|1<<i,next_state)
            if rest is not None:return (i,)+rest
        return None
    witness=search(0,initial)
    if witness is None:return {'linearizable':False,'order':None,'searched_states':visited[0]}
    trace=[];state=initial
    for i in witness:
        e=events[i];new=transition(state,e['op']);trace.append({'id':e['id'],'before':state,'after':new});state=new
    return {'linearizable':True,'order':[events[i]['id'] for i in witness],'trace':trace,'final_state':state,'searched_states':visited[0]}
