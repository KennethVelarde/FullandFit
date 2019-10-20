# Test file for the 01 knapsack problem with the following alterations
# each item has infinite supply


#
# int findMaxValue(int weight[],int values[],int items[],int n,int capacity) {
#    // temporary array where index 'j' denotes max value that can be fitted
#    // in a knapsack of weight 'j'
#    int knapsack[capacity+1];
#    knapsack[0] = 0;
#    items[0] = -1;
#    int i,j;
#    for(j=1;j<=capacity;j++) {
#       items[j] = items[j-1];
#       // as per our recursive formula,
#       // iterate over all weights w(0)...w(n-1)
#       // and find max value that can be fitted in knapsack of weight 'j'
#       int max = knapsack[j-1];
#       for(i=0;i<n;i++) {
#          int x = j-weight[i];
#          if(x >= 0 && (knapsack[x] + values[i]) > max) {
#             max = knapsack[x] + values[i];
#             items[j] = i;
#          }
#          knapsack[j] = max;
#       }
#    }
#    return knapsack[capacity];
# }

def unbounded_knapsack(v, w, cap):
    n = len(v)
    sack = [0] * (cap + 1)
    items = [-1] * (cap + 1)

    for j in range(1, cap + 1):
        items[j] = items[j - 1]
        max = sack[j - 1]
        for i in range(n):
            x = j - w[i]
            if x >= 0 and sack[x] + v[i] > max:
                max = sack[x] + v[i]
                items[j] = i
            sack[j] = max
    return sack[cap], items[cap]

if __name__ == "__main__":
    v = [600, 1200, 760, 400, 1200]
    w = [599, 899, 499, 299, 999]
    c = 10000

    sack, items= unbounded_knapsack(v, w, c)

    print(sack)
    print(items)