

// The Dining Philosophers problem is a popular problem in process synchronization in operating systems. Implementing a solution to this problem.

#include<stdio.h>

#include<semaphore.h>

#include<pthread.h>

#include<unistd.h>

#define N 5 // Number of philosphers

#define TRUE 1  //Defining TRUE for loop

#define THINKING 0 // state of activity 
#define HUNGRY 1  // state of activity 
#define EATING 2 // state of activity 


#define LEFT (ph_num+4)%N // Left philospher
#define RIGHT (ph_num+1)%N  // right philospher


sem_t MUTEX;
sem_t S[N]; // Semophore declaration for philosphers

void take_fork(int);
void put_fork(int);
void test(int);

int count[5]; // Eat count 

int FOOD = 0; // count the food

void * philospher(void *num);

int state[N];

int phil_num[N]={0,1,2,3,4};


void put_fork(int ph_num)
{
    sem_wait(&MUTEX);
    state[ph_num] = THINKING;

    count[ph_num]++;
    FOOD++;
  
    test(LEFT);
    test(RIGHT);

	printf("The Eating Count = %d \n", FOOD);
	int i;
	for(i=0;i<5;i++){
		if(state[i]==EATING)
			printf("The Philosopher %d is EATING\n", i);
		else if(state[i]==HUNGRY)
			printf("Philosopher %d is WAITING \n", i);
		else if(state[i]==THINKING)
			printf("Philosopher %d is THINKING\n", i);
	}

    sem_post(&MUTEX);
}


void *philospher(void *num)
{   
   
    while(FOOD<6)  //considered 6 item to eat. It can be infinite using while(TRUE) or any other desired number
    {
        int *i = num;
        usleep(10000);
        take_fork(*i);
        put_fork(*i);
    }
}


void take_fork(int ph_num)
{
    sem_wait(&MUTEX);
    state[ph_num] = HUNGRY;
    test(ph_num);
    sem_post(&MUTEX);
    sem_wait(&S[ph_num]);
    usleep(10000);
}


void test(int ph_num)
{
    if (state[ph_num] == HUNGRY && state[LEFT] != EATING && state[RIGHT] != EATING)
    {
        state[ph_num] = EATING;
        usleep(20000);
        sem_post(&S[ph_num]);
    }
}


int main()
{
    int i;
    pthread_t thread_id[N];

    sem_init(&MUTEX,0,1);
    for(i=0;i<N;i++)
        sem_init(&S[i],0,0);

    for(i=0;i<N;i++)
    {
        pthread_create(&thread_id[i],NULL,philospher,&phil_num[i]);  
    }
    
    for(i=0;i<N;i++)
        pthread_join(thread_id[i],NULL);

    for(i=0;i<N;i++)
	printf(" The Philospher %d ate %d times\n",i,count[i]);
    printf("\n");
}
