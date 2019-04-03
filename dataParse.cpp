/*
3/18/2019
SF_dataParse.py
Used for parsing the data from the SF election provided by Dr. Graham-Squire
formats the data better and sorts it
*/
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
# define NO_OF_CHARS 256 

using namespace std;

struct vote{
	int numVote;
	string order;
};

void dump(vector<vote>);

void format(vector<vote>&, int numBalSpot);

int vec_find(vector<vote> vec, string find);

int vec_find(vector<vote> vec, string find, int n);

void quickSort(vector<vote>&, int low, int high);

void partition(vector<vote>&, int low, int high, int &pivotpoint);

void exchange(vote&, vote&);

char *removeDups(char *str);

int main(){
	int numCan, numBalSpot, nextVote;
	vector<vote> voteOrder;
	vote tmp;
	cin >> numCan; 
	cin >> numBalSpot;
	while ( cin >> nextVote ){
		if (nextVote != -1){
			tmp.numVote = nextVote;
			cin >> tmp.order;
			char buff [tmp.order.size() + 1];
			strcpy(buff, tmp.order.c_str());
			tmp.order = removeDups(buff);
			voteOrder.push_back(tmp);
		}
	}
	format(voteOrder, numBalSpot);
	format(voteOrder, numBalSpot);
	quickSort(voteOrder, 0, voteOrder.size() );
	dump(voteOrder);
	return 0;
}

void dump(vector<vote> vec){
	int size = vec.size();
	for (int i = 0; i < size; i++){
		cout << vec[i].numVote << " " << vec[i].order << endl;
	}
}

void format(vector<vote> &vec, int numBalSpot){
	int size = vec.size(); 
	string tmp;
	for (int i = 0; i < size; i++){
		if (vec_find(vec, vec[i].order, i) != -1){
			vec[vec_find(vec, vec[i].order, i)].numVote += vec[i].numVote;
			vec.erase(vec.begin()+i);
		}
		size = vec.size();
	}
}

int vec_find(vector<vote> vec, string find){
	int size = vec.size();
	for (int i = 0; i < size; i++){
		if (vec[i].order == find){
			return i;
		} else {
			// cerr << "vec_find couldn't find requested string" << endl;
		}
	}
	return -1;
}

int vec_find(vector<vote> vec, string find, int n){
	int size = vec.size();
	for (int i = 0; i < size; i++){
		if (vec[i].order == find && i != n ){
			return i;
		} else {
			// cerr << "vec_find couldn't find requested string" << endl;
		}
	}
	return -1;
}


void quickSort(vector<vote> &vec, int low, int high){
	int pivotpoint;
	if (high > low){
		partition(vec, low, high, pivotpoint);
		quickSort(vec, low, pivotpoint - 1);
		quickSort(vec, pivotpoint + 1, high);
	}
}

void partition(vector<vote> &vec, int low, int high, int &pivotpoint){
	int j = low ;
	string pivot = vec[low].order;

	for ( int i = low; i <= high - 1; i++ ){
		if (pivot > vec[i].order){
			j++;
			exchange(vec[i], vec[j]);
		}
	}
	pivotpoint = j;
	exchange(vec[low], vec[pivotpoint]);
}

void exchange(vote &a, vote &b){
	vote temp;
	temp.numVote = a.numVote;
	temp.order = a.order;

	a.numVote = b.numVote;
	a.order = b.order;

	b.numVote = temp.numVote;
	b.order = temp.order;
}

char *removeDups(char *str) 
{ 
  bool bin_hash[NO_OF_CHARS] = {0}; 
  int ip_ind = 0, res_ind = 0; 
  char temp;     
  
  /* In place removal of duplicate characters*/
  while (*(str + ip_ind)) 
  { 
    temp = *(str + ip_ind); 
    if (bin_hash[temp] == 0) 
    { 
        bin_hash[temp] = 1; 
        *(str + res_ind) = *(str + ip_ind); 
        res_ind++; 
    } 
    ip_ind++; 
  }       
  
  /* After above step string is stringiittg. 
     Removing extra iittg after string*/
  *(str+res_ind) = '\0';    
  
  return str; 
} 