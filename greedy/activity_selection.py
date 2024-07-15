# input - processes - output
# sessions with start and end time sorted by end time - - the optimal selection sessions

def greedy_select_sessions(start,end):
  # define the result list and add 1st item by default
  results=[0]
  # define i=1 for start,j=0 for end
  i,j=1,0
  # loop until until the n
  while i<len(start):
    if start[i]>=end[j]:results.append(i);j=i
    i+=1
  print(results)
  #end loop and return results

if __name__=='__main__':
  start = [1,3,5,7]
  end  = [4,4,7,10]
  greedy_select_sessions(start,end)