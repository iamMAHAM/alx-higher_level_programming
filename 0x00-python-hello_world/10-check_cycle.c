#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head of linked list
 * Return: 1 if cycled, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *next_list;

	if (!list)
	{
		return (0);
	}
	head = list;
	next_list = list->next;
	while (next_list && head && next_list->next)
	{
		if (head == next_list)
		{
			return (1);
		}
		head = head->next;
		next_list = next_list->next->next;
	}
	return (0);
}
