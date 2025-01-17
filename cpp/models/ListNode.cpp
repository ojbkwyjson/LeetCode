//
// Created by 曲本豪 on 2024/5/21.
//

#include "ListNode.h"

ListNode *IntArrayToListNode(std::vector<int> &arr) {
    auto dummy = new ListNode(), p = dummy;
    for (auto val : arr) {
        p->next = new ListNode(val);
        p = p->next;
    }
    return dummy->next;
}

std::vector<int> &ListNodeToIntArray(ListNode *head) {
    auto *arr = new std::vector<int>();
    while (head != nullptr) {
        arr->push_back(head->val);
        head = head->next;
    }
    return *arr;
}

ListNode *IntArrayToListNodeCycle(std::vector<int> &arr, int pos) {
    auto dummy = new ListNode(), p = dummy;
    ListNode *cycle = nullptr;
    for (int i = 0; i < static_cast<int>(arr.size()); i++) {
        p->next = new ListNode(arr[i]);
        p = p->next;
        if (i == pos) {
            cycle = p;
        }
    }
    p->next = cycle;
    return dummy->next;
}

std::tuple<ListNode *, ListNode *>
IntArrayToIntersectionListNode(std::vector<int> &arr1, std::vector<int> &arr2, int iv, int idxA, int idxB) {
    auto headA = IntArrayToListNode(arr1);
    if (iv == 0 || idxA == static_cast<int>(arr1.size()) || idxB == static_cast<int>(arr2.size())) {
        return {headA, IntArrayToListNode(arr2)};
    }
    auto pa = headA;
    for (int i = 0; i < idxA; i++) {
        pa = pa->next;
    }
    auto headB = idxB == 0 ? pa : new ListNode(arr2[0]);
    auto pb = headB;
    for (int i = 1; i < idxB - 1; i++) {
        pb->next = new ListNode(arr2[i]);
        pb = pb->next;
    }
    pb->next = pa;
    return {headA, headB};
}