FUNCTION 


compute_toxicity(drug_data):
    toxicity <- 0
    for p in P:
        for c in C:
            for i in N:
                unnormalized_toxicity <- abs(drug_data[i,c,p]) - min(drug_data[i,:,p]) / (max(drug_data[i,:,p]) - min(drug_data[i,:,p])) +  L
                
                toxicity <- toxicity + unnormalized_toxicity/len(drug_data)
    ENDFOR
        ENDFOR
            ENDFOR
    RETURN toxicity