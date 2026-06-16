class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        sort(tasks.begin(),tasks.end(),[](vector<int>t1,vector<int>t2){
            return t1[1]-t1[0] > t2[1]-t2[0];
        });

        // for(auto t : tasks){
        //     cout<<t[0]<<" "<<t[1]<<endl;
        // }
        int initial = 0, curr = 0;

        for(auto task : tasks){
            int required = task[1]-curr;

            if(required > 0) {
                curr = task[1];
                initial += required;
            }

            curr -= task[0];
        }

        return initial;
    }
};