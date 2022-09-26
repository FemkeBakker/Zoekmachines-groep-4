from collections import defaultdict

    
    
class TermFrequency(object):
    def __init__(self, passages):
        self.num_p = len(passages)
        self.passages = passages
        self.tf = {}     

        for p_id, tokens in self.passages.items():
            tmp = {}
            for token in tokens:
                tmp[token] = tmp.get(token, 0) + 1  
                
            self.tf[p_id]=tmp
            
        
    def score(self, queries):
        num_q = len(queries)
        scores = defaultdict(dict)
    
        counter = 0
        
        for q_id, q_tokens in queries.items():
            
            counter+=1
            if counter%100==0:
                print("finished the calculation of {}th queries over {} queries".format(counter, num_q))
      
            for p_id, _ in self.passages.items():
                score=0
                for q_token in q_tokens:
                    if q_token not in self.tf[p_id]:
                        continue
                    score += self.tf[p_id][q_token]
                    
                scores[q_id][p_id]=score
        
        return scores 