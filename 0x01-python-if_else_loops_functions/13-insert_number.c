#include "lists.h"
#include <stdlib.h>
#include <stdio.h>


/***
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head node
 * @number: number to insert
 * Return: inserted node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL && (*head)->n >=  new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < new_node->n)
			current = current->next;
		new_node->next = current->next;
		current->next = new_node;
	}
	return (*head);
}
