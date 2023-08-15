#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	unsigned int nodes, j = 0;
	int arr[1024];

	tmp = *head;
	if (tmp == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	nodes = 0;
	while (tmp)
	{
		nodes += 1;
		tmp = tmp->next;
	}
	if (nodes == 1)
		return (1);

	tmp = *head;
	while (tmp)
	{
		arr[j] = tmp->n;
		tmp = tmp->next;
		j++;
	}
	j = 0;
	for (j = 0; j < (nodes / 2); j++)
	{
		if (arr[j] != arr[nodes - j - 1])
			return (0);
	}
	return (1);
}
