class Solution {
    int n;
    vector<vector<int>> adj;
    // dp[i][j][k] mean the max sum of (ith node subtree) with at least j times no inverse
    // k = 0 => min , k = 1 => max
    vector<vector<vector<long long>>> dp;
public:
    long long subtreeInversionSum(vector<vector<int>>& edges, vector<int>& nums, int k) {
        n = nums.size();
        adj.resize(n);
        for(auto& e : edges){
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        dp.resize(n, vector<vector<long long>>(k, vector<long long>(2)));
        dfs(0, -1, k, nums);
        return dp[0][0][1];
    }
    void dfs(int cur, int parent, int k, vector<int>& nums){
        if(cur != 0 && adj[cur].size() == 1){ // leaf, base case
            dp[cur][0][0] = min(-nums[cur], nums[cur]);
            dp[cur][0][1] = max(-nums[cur], nums[cur]);
            for(int j=0; j<2; ++j){
                for(int i=1; i<k; ++i) dp[cur][i][j] = nums[cur];
            }
            return;
        }
        // postorder
        for(auto child : adj[cur]){
            if(child != parent){
                dfs(child, cur, k, nums);
            }
        }
        // for max
        for(int i=1; i<k; ++i){
            dp[cur][i][1] = nums[cur];
            for(auto child : adj[cur]){
                if(child != parent){
                    dp[cur][i][1] += dp[child][i-1][1];
                }
            }
        }
        // for min
        for(int i=1; i<k; ++i){
            dp[cur][i][0] = nums[cur];
            for(auto child : adj[cur]){
                if(child != parent){
                    dp[cur][i][0] += dp[child][i-1][0];
                }
            }
        }
        // for at least 0 distance
        long long noinv[2] = {nums[cur], nums[cur]};
        long long inv[2] = {-nums[cur], -nums[cur]};
        for(auto child : adj[cur]){
            if(child != parent){
                noinv[0] += dp[child][0][1];
                noinv[1] += dp[child][0][0];
                inv[0] -= dp[child][k-1][1];
                inv[1] -= dp[child][k-1][0]; 
            }
        }
        dp[cur][0][1] = max(max(noinv[0], noinv[1]), max(inv[0], inv[1]));
        dp[cur][0][0] = min(min(noinv[0], noinv[1]), min(inv[0], inv[1]));
    }
};