/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* cur = nullptr;
        ListNode* ans = nullptr;
        int upper = 0;
        
        while (l1 != nullptr || l2 != nullptr || upper) {
            if (cur == nullptr) {
                cur = new ListNode();
                ans = cur;
            }
            else {
                cur->next = new ListNode();
                cur = cur->next;
            }
            
            int num1 = 0;
            if (l1) {
                num1 = l1->val;
                l1 = l1->next;
            }
            
            int num2 = 0;
            if (l2) {
                num2 = l2->val;
                l2 = l2->next;
            }
            
            int result = num1 + num2 + upper;
            upper = result / 10;
            cur->val = result % 10;
        }
        
        return ans;
    }
};