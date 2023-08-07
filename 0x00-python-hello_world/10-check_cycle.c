#include "lists.h"
#include <stdio.h>

/**
 * check_cycle -  checks if a singly linked list has a cycle in it
 * @list: lists to be checked 
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *high = list;
	listint_t *low = list;

	while (1)
	{
		if (high->next != NULL && high->next->next != NULL)
		{
			high = high->next->next;
			low = low->next;

			if (high == low)
				return (1);
		}
		else
			return (0);
	}
}

