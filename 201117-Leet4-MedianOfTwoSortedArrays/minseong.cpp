constexpr static auto __ = []() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    return 0;
};

class Solution {
public:
    int binarySearch(vector<int>& nums1, vector<int>& nums2, int target) {
        int result = 2000000;
        
        int l = min(nums1[0], nums2[0]);
        int h = max(nums1.back(), nums2.back());
        while (l <= h) {
            int m = (l + h) / 2;
            int i1 = distance(begin(nums1), lower_bound(begin(nums1), end(nums1), m));
            int i2 = distance(begin(nums2), lower_bound(begin(nums2), end(nums2), m));
            int passed = i1 + i2;
            if (passed <= target) {
                l = m + 1;
                result = min(nums1[i1], nums2[i2]);
            }
            else {
                h = m - 1;
            }
        }
        
        return result;
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        int target = (n1 + n2) / 2;
        bool isOdd = (n1 + n2) % 2;

        int ans = 0;
        int max1 = nums1.size() ? nums1.back() : -1000001;
        int max2 = nums2.size() ? nums2.back() : -1000001;
        int maxx = max(max1, max2);
        nums1.push_back(maxx + 1);
        nums2.push_back(maxx + 1);
        if (isOdd) {
            return binarySearch(nums1, nums2, target);
        }
        else {
            int mid1 = binarySearch(nums1, nums2, target);
            int mid2 = binarySearch(nums1, nums2, target - 1);
            return (mid1 + mid2) / (double)2;
        }
    }
};