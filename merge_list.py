# Definition for singly-linked list.
# It's really not that optimized code just for the practice purpose
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, head1, head2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        ## in case of both head present 
        if(head1 and head2):
            if(head1.val<head2.val):
                head3=ListNode(head1.val)
                current1=head1.next
                current2=head2

            else:
                head3=ListNode(head2.val)
                current1=head1
                current2=head2.next  


            current3=head3

            while True:


                if not current1 :

                    current3.next=current2 
                    if current2.next:
                       current2 =current2.next
                    else:
                        break;

                elif not current2:

                    current3.next=current1
                    if current1.next:
                     current1=current1.next
                    else: 
                        break;

                else:

                    if(current1.val<current2.val):

                        current3.next=current1
                        current1=current1.next
                    else:
                        current3.next=current2 
                        current2=current2.next






                current3=current3.next
            return(head3)    
        ## number of possibilities when head is not present        
        elif(head1 and not head2):
               return(head1)
        elif(head2 and not head1):
               return(head2)
        elif(not head1 and not head2):
               return([]) 
         