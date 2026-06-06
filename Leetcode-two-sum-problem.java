/** Initial 89ms Runtime Attempt */
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            for(int j = 1; j < nums.length; j++){
                if(((nums[i] + nums[j]) == target) && (i != j)){
                    return new int[] {i,j};
                }
            }
        }
        return null;
    }
}
/** 
# Description:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
*/

/** Best 2ms Runtime Solution*/
class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap<Integer,Integer> num_to_index=new HashMap<>();
       int n=nums.length;
       for(int i=0;i<n;i++){
       int comp=target - nums[i];
       if(num_to_index.containsKey(comp)){
        return new int[]{num_to_index.get(comp),i};
       } 
       num_to_index.put(nums[i],i);

       }
       return new int[]{};
}
}
# By using a HashMap where you maintain a memory of seen values, you can use the complement of the target and current value to search the HashMap for a match.
# A match means we then take the index of the current value and the complements index from the num_to_index HashMap ("Seen values" HashMap) and return a tuple of their indexes.
# This solution is very similar to the python solution we got to see prior.