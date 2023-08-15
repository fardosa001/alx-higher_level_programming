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
	unsigned int nodes;
	int *arr;
	int j;


	tmp = *head;
	if (tmp == NULL)
		return (1);

	nodes = 0;
	while (tmp != NULL)
	{
		nodes++;
		tmp = tmp->next;
	}

	arr = malloc(nodes * sizeof(int));
	if (arr == NULL)
		return (0);

	tmp = *head;
	for (j = 0; tmp != NULL; j++)
	{
		arr[j] = tmp->n;
		tmp = tmp->next;
	}

	for (j = nodes - 1; tmp != NULL; j--)
	{
		if (tmp->n != arr[j])
		{
			free(arr);
			return (0);
		}
		tmp = tmp->next;
	}
	free(arr);
	return (1);
}
