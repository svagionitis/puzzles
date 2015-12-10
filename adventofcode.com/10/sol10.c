/**
 * @file    look_and_say_seq.c
 * @author  Stavros Vagionitis
 * @date    01 Feb 2015
 * @brief   Implement the look and say sequence. More info
 *          here http://en.wikipedia.org/wiki/Look-and-say_sequence
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**
 * \brief Swap pointers
 *
 * \param   p1  [IN/OUT] First pointer
 * \param   p2  [IN/OUT] Second pointer
 */
void swap_ptr(unsigned int **p1, unsigned int **p2)
{
    if (!p1 && !*p1)
        return;

    if (!p2 && !*p2)
        return;

    unsigned int *tmp = *p2;
    *p2 = *p1;
    *p1 = tmp;
}

/**
 * \brief Update the sequence giving the previous sequence.
 *
 * \param   seq             [IN] The previous sequence
 * \param   sizeof_seq      [IN] The size of the previous sequence.
 * \param   new_seq         [OUT] The new sequence
 * \param   sizeof_new_seq  [OUT] The size of the new sequence.
 * \return  1 if everything is ok, 0 if not.
 */
char update_seq(const unsigned int *seq, const unsigned int sizeof_seq, unsigned int **new_seq, unsigned int *sizeof_new_seq)
{
    if(*new_seq)
        *new_seq = NULL;

    *sizeof_new_seq = 0;

    if (seq == NULL)
    {
        fprintf(stderr, "%s:%d seq is NULL\n", __func__, __LINE__);
        return 0;
    }


    unsigned int *tmp = NULL;
    unsigned int counter = 0, i = 0;
    for (i = 0;i<sizeof_seq;i++)
    {
        tmp = NULL;

        if (i == 0)
            counter++;

        if (i > 0)
        {
            // If the current digit is the same
            // with the previous add it to the
            // counter.
            if (seq[i-1] == seq[i])
                counter++;
            else
            {
                // If the current digit is not the same
                // with the previous, then allocate two
                // places in the new sequence, one for the
                // counter and the other for the previous digit.
                *sizeof_new_seq += 2;

                tmp = realloc(*new_seq, *sizeof_new_seq * sizeof(unsigned int));
                if (tmp != NULL)
                    *new_seq = tmp;
                else
                {
                    fprintf(stderr, "%s:%d Mem Alloc failed\n", __func__, __LINE__);

                    if (*new_seq)
                        free(*new_seq);

                    return 0;
                }

                (*new_seq)[*sizeof_new_seq - 2] = counter;
                (*new_seq)[*sizeof_new_seq - 1] = seq[i-1];

                // Start counter from 1 for
                // counting the current digit.
                counter = 1;
            }
        }

        // The last number in sequence.
        if (i == sizeof_seq - 1)
        {
            *sizeof_new_seq += 2;

            tmp = realloc(*new_seq, *sizeof_new_seq * sizeof(unsigned int));
            if (tmp != NULL)
                *new_seq = tmp;
            else
            {
                fprintf(stderr, "%s:%d Mem Alloc failed\n", __func__, __LINE__);

                if (*new_seq)
                    free(*new_seq);

                return 0;
            }

            (*new_seq)[*sizeof_new_seq - 2] = counter;
            (*new_seq)[*sizeof_new_seq - 1] = seq[i];
        }
    }

    return 1;
}

/**
 * \brief   Print the sequence numbers in a line.
 *
 * \param   seq         [IN] The sequence itself.
 * \param   size_seq    [IN] The size of the sequence.
 * \return  1 if everything is ok, 0 if not.
 */
char print_seq(const unsigned int *seq, const unsigned int size_seq)
{
    unsigned int i = 0;

    if (seq == NULL)
    {
        fprintf(stderr, "%s:%d seq is NULL\n", __func__, __LINE__);
        return 0;
    }

    for (i = 0;i<size_seq;i++)
    {
        if (i != size_seq-1)
            fprintf(stdout, "%u", seq[i]);
        else
            fprintf(stdout, "%u -- %u\n", seq[i], size_seq);
    }

    return 1;
}

/**
 * \brief   Count digits of an unsigned integer
 *
 * \param   num         [IN] The number to count the digits
 * \return  the number of digits.
 */
unsigned int count_digits(const unsigned int num)
{
    unsigned int c = 0;
    unsigned int n = num;

    while(n)
    {
        n/=10;
        c++;
    }

    return c;
}

void usage(char *argv0)
{
    fprintf(stdout, "%s [starting value] [iterations]\n", argv0);
    exit(0);
}

int main(int argc, char *argv[])
{
    unsigned int start = 0;
    unsigned int total_iter = 0;

    if (argc != 3)
        usage(argv[0]);

    if (argv[1])
        start = (unsigned int)atoi(argv[1]);
    else
        usage(argv[0]);

    if (argv[2])
        total_iter = (unsigned int)atoi(argv[2]);
    else
        usage(argv[0]);


    // Current sequence.
    unsigned int *seq = NULL;
    unsigned int seq_size = count_digits(start);

    seq = malloc(seq_size * sizeof(unsigned int));

    // Convert the starting number in a number sequence
    int d = 0;
    for(d = seq_size - 1; d >= 0;d--)
    {
        seq[d] = start % 10;
        start /= 10;
    }

    // New sequence.
    unsigned int *new_seq = NULL;
    unsigned int new_seq_size = 0;

    unsigned int i = 0;
    for (i = 0;i<total_iter;i++)
    {

        update_seq(seq, seq_size, &new_seq, &new_seq_size);

        if (i == total_iter - 1)
            print_seq(new_seq, new_seq_size);

        seq_size = new_seq_size;
        new_seq_size = 0;

        swap_ptr(&seq, &new_seq);

        if (new_seq)
            free(new_seq);
    }

    if (seq)
        free(seq);

    return 0;
}
