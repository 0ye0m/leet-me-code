class Solution {
    public int numberOfSpecialChars(String word) {
        HashSet<Character>lower = new HashSet<>();
        HashSet<Character>upper = new HashSet<>();
        HashSet<Character>invalid = new HashSet<>();
        
        for(char ch:word.toCharArray()){
            if(Character.isLowerCase(ch)){
                if(upper.contains(Character.toUpperCase(ch))){
                    invalid.add(ch);
                }
                lower.add(ch);
            }
            else{
                upper.add(ch);
            }

        }
        int ans=0;
        for(char ch:lower){
            if(upper.contains(Character.toUpperCase(ch)) && !invalid.contains(ch)){
                ans++;
            }
        }
        return ans;
    }
}