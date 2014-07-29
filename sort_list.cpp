/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *sortList(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        return merge_sort(head);
    }
    
    ListNode* merge_sort(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        ListNode* middle = getMiddle(head);
        ListNode* sHalf = middle->next;
        
        middle->next = NULL;
        return merge(merge_sort(head), merge_sort(sHalf));
    }
    
    ListNode* merge(ListNode* left, ListNode* right) {
        ListNode* dummy = new ListNode(0);
        ListNode* head = dummy;
        
        while (left != NULL && right != NULL) {
            if (left->val < right->val) {
                dummy->next = left;
                left = left->next;
            } else {
                dummy->next = right;
                right = right->next;
            }
            dummy = dummy->next;
        }
        
        dummy->next = (right == NULL)?left:right;
        return head->next;
    }
    
    ListNode* getMiddle(ListNode* head) {
        if (head == NULL) {
            return head;
        }
        ListNode* a = head;
        ListNode* b = head;
        while(a->next != NULL && b->next != NULL && b->next->next != NULL) {
            a = a->next;
            b = b->next->next;
        }
        return a;
    }
};
