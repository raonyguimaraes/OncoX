from celery.decorators import task

from analyses.models import Analysis

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def chunkIt(seq, num):
  avg = len(seq) / float(num)
  out = []
  last = 0.0

  while last < len(seq):
    out.append(seq[int(last):int(last + avg)])
    last += avg

  return out

@task(name="xhmm")
def xhmm(analysis_id):
    print 'hello xhmm'
    print 'analysis_id', analysis_id
    #now make CNV identification from list of files

    analysis = Analysis.objects.get(id=analysis_id)
                
    print 'analysis', analysis
    print 'analysis type', analysis.type
    print 'analysis files', analysis.files.all()
    analyses_count = analysis.files.count()
    
    files = list(analysis.files.all())


    lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    
    # groups = lol(files, 3)
    groups = chunkIt(files, 3)

    print 'groups', groups
    # files_groups = list(chunks(files, 3))
    # print 'files_groups', files_groups
    # print 'number of groups', len(files_groups)
    # for idx, group in enumerate(files_groups):
        # print 'idx group', idx, group

    # print 'len', len(analyses)
    # for file in files:
        # print analysis.name
        # print analysis.file
        
    # print 'analyses_count', analyses_count


    # print len(analyses)
    # for analysis_file in analyses:
        # print 'analysis_file', analysis.id, analysis_file.name 

    
    
    