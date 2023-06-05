#include "lists.h"
#include <stdlib.h>


/**
 * check_cycle - check if a loop is in the linked list
 * @list: poointing to the head node
 * Return: 0 if no loop else 1 if loop is found
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (slow != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
