#include "lists.h"
#include <stdlib.h>

/**
 * insert_note - inserts a number into a sorted singly linked list.
 * Return: the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL, *temp = NULL;
	
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head)
	{
		current = *head;
		if (number <= current->n)
		{
			new->next = current;
			*head = new;
		}
		else
		{
			while (current->next)
			{
				if (number <= current->next->n)
				{
					temp = current->next;
					current->next = new;
					new->next = temp;
					return (*head);
				}

				current = current->next;
			}
			temp = current->next;
			current->next = new;
			new->next = temp;
		}
		return (*head);

	}
	new->next = NULL;
	*head = new;
	return (*head);
}
	
