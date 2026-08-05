class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int area = 0;

        while(left < right){
            int height = Math.min(heights[left], heights[right]);
            int width = right - left;
            area = Math.max(area, height * width);

            if(heights[left] < heights[right]){
                left++;
            } else {
                right--;
            }
        }

        return area;
    }
}
