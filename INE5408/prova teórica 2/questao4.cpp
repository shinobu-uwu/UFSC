/* C++ implementation of QuickSort */
#include <bits/stdc++.h>
using namespace std;

// A utility function to swap two elements
void swap(int* a, int* b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

/* Function to print an array */
void printArray(int arr[], int size)
{
	int i;
	for (i = 0; i < size; i++)
		cout << arr[i] << " ";
	cout << endl;
}

/* This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot */
int partition (int arr[], int low, int high)
{
	int pivot = arr[low]; // pivot
	int i = (low - 1); // Index of smaller element and indicates the right position of pivot found so far
    swap(&arr[high], &arr[low]);

	for (int j = low; j <= high - 1; j++)
	{
		// If current element is smaller than the pivot
		if (arr[j] < pivot)
		{
			i++; // increment index of smaller element
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
    printArray(arr, 10);
	return (i + 1);
}

/* The main function that implements QuickSort
arr[] --> Array to be sorted,
low --> Starting index,
high --> Ending index */
void quickSort(int arr[], int low, int high)
{
	if (low < high)
	{
		/* pi is partitioning index, arr[p] is now
		at right place */
		int pi = partition(arr, low, high);

		// Separately sort elements before
		// partition and after partition
		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}



// Driver Code
int main()
{
	int arr[] = {30, 20, 50, 10, 70, 80, 90, 100, 60, 40};
	quickSort(arr, 0, 9);
	cout << "Sorted array: \n";
	printArray(arr, 10);
	return 0;
}

// This code is contributed by rathbhupendra

template<typename T>
T Hash<T>::maximo() {
    // Os máximos de cada depósito
    T maximos[S];

    for (int i = 0; i < S; i++) {
        auto arvore = tabela[i];
        Node *aux = arvore.root();
        // Percorremos até o elemento mais a direita
        while (aux->right() != nullptr)
            aux = aux->right();
        maximos[i] = aux->data();
    }
    // Retorna o máximo da lista
    return std::max(maximos);
}