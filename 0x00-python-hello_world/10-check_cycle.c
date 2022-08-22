#include "lists.h"

/**
 * check_cycle - checks if a singly-linked list contains a cycle
 * @list: signly-linked list to be checked
 *
 * Return: 0 - if there is no cycle
 *         1 - if there is a cycle
 */
int check_cycle(listint_t *list)
{
	/* names gotten from carnot cycle hot and cold reservoirs */
	listint_t *hot, *cold;

	if (list == NULL || list->next == NULL)
		return (0);

	hot = list->next;
	cold = list->next->next;

	while (hot && cold && cold->next)
	{
		if (hot == cold)
			return (1);

		hot = hot->next;
		cold = cold->next->next;
	}

	return (0);
}
