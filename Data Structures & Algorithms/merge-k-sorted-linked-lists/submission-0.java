/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0){
            return null;
        }

        ListNode head = null;

        for(int i = 0; i < lists.length; i++){
            head = mergeLists(head, lists[i]);
        }

        return head;
    }

    public ListNode mergeLists(ListNode l1, ListNode l2){
        ListNode head = new ListNode();
        ListNode curr = head;

        while(l1 != null && l2 != null){
            if(l1.val < l2.val){
                curr.val = l1.val;
                l1 = l1.next;
            } else {
                curr.val = l2.val;
                l2 = l2.next;
            }

            curr.next = new ListNode();
            curr = curr.next;
        }

        while(l1 != null){
            curr.val = l1.val;
            l1 = l1.next;
            if(l1 != null){
                curr.next = new ListNode();
                curr = curr.next;
            }
        }

        while(l2 != null){
            curr.val = l2.val;
            l2 = l2.next;
            if(l2 != null){
                curr.next = new ListNode();
                curr = curr.next;
            }
        }

        return head;
    }
}
