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
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return null;
        }
        ListNode newHead = new ListNode();

        while(head != null){
            newHead.val = head.val;
            ListNode newNode = new ListNode();
            newNode.next = newHead;
            newHead = newNode;
            head = head.next;
        }

        newHead = newHead.next;
        return newHead;
    }
}
