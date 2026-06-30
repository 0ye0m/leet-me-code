
class Solution {
public:
    int numberOfSubstrings(string s) {
        int lastA = -1, lastB = -1, lastC = -1;
        int total = 0;

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == 'a')
                lastA = i;
            else if (s[i] == 'b')
                lastB = i;
            else
                lastC = i;

            if (lastA != -1 && lastB != -1 && lastC != -1) {
                total += min({lastA, lastB, lastC}) + 1;
            }
        }

        return total;
    }
};