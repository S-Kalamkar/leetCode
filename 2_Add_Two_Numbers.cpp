#include <iostream>
using namespace std;
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
{
    ListNode *head = nullptr, *curr = nullptr, *ptr = nullptr;
    bool carry = false;
    while (l1 && l2)
    {
        ptr = new ListNode;
        ptr->val = l1->val + l2->val;
        l1 = l1->next;
        l2 = l2->next;
        if (carry)
            ptr->val += 1;
        carry = false;
        if (ptr->val >= 10)
        {
            ptr->val -= 10;
            carry = true;
        }
        ptr->next = nullptr;

        if (!head)
        {
            head = ptr;
            curr = head;
        }
        else
        {
            curr->next = ptr;
            curr = curr->next;
        }
    }

    while (l1)
    {
        ptr = new ListNode;
        ptr->val = l1->val;
        l1 = l1->next;
        if (carry)
            ptr->val += 1;
        carry = false;
        if (ptr->val >= 10)
        {
            ptr->val -= 10;
            carry = true;
        }
        ptr->next = nullptr;

        if (!head)
        {
            head = ptr;
            curr = head;
        }
        else
        {
            curr->next = ptr;
            curr = curr->next;
        }
    }

    while (l2)
    {
        ptr = new ListNode;
        ptr->val = l2->val;
        l2 = l2->next;
        if (carry)
            ptr->val += 1;
        carry = false;
        if (ptr->val >= 10)
        {
            ptr->val -= 10;
            carry = true;
        }
        ptr->next = nullptr;

        if (!head)
        {
            head = ptr;
            curr = head;
        }
        else
        {
            curr->next = ptr;
            curr = curr->next;
        }
    }

    if (carry)
    {
        ptr = new ListNode;
        ptr->val = 1;
        curr->next = ptr;
        curr = curr->next;
    }
    return head;
}

int main()
{
    ListNode *l1 = nullptr, *l2 = nullptr, *ptr = nullptr;
    int n, num = 0;
    cout << "Enter num of digits for num 1" << endl;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "enter digit " << i << endl;
        cin >> num;
        ptr = new ListNode(num);
        if (!l1)
            l1 = ptr;
        else
        {
            ptr->next = l1;
            l1 = ptr;
        }
        ptr = nullptr;
    }

    cout << "Enter num of digits for num 2" << endl;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cout << "enter digit " << i << endl;
        cin >> num;
        ptr = new ListNode(num);
        if (!l2)
            l2 = ptr;
        else
        {
            ptr->next = l2;
            l2 = ptr;
        }
        ptr = nullptr;
    }

    ptr = addTwoNumbers(l1, l2);
    while (ptr)
    {
        cout << ptr->val;
        ptr = ptr->next;
    }
}