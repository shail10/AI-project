import hillClimb
import randomRestart
import simulatedAnealing
import utility
import time

from tabulate import tabulate


if __name__ == "__main__":
  t_test = 35
  t = t_test
  n = 10

  t_time1 = 0
  t_time2 = 0
  t_time3 = 0

  success1 = 0
  success2 = 0
  success3 = 0

  steps1 = 0
  steps2 = 0
  steps3 = 0

  while t:
    # print(t)
    board = utility.generate_board(n)
    board1 = board.copy()
    board2 = board.copy()
    board3 = board.copy()

    ## hillClimbing
    begin = time.time()
    time.sleep(0.1)
    
    flag, cnt, *_ =hillClimb.hillClimbing(n, board1, True)

    end = time.time()

    if flag:
      success1+=1
      steps1 += cnt

    t_time1 += (end-begin-0.1)*1000

    
    ## Random Restart
    begin = time.time()
    time.sleep(0.1)

    flag, cnt, *_ = randomRestart.randomRestartHillClimbing(n, board2, True)  

    end = time.time()

    if flag:
      success2 +=1
      steps2 += cnt

    t_time2 += (end-begin-0.1)* 1000


    ## Simulated Annealing
    begin = time.time()
    time.sleep(0.1)

    flag, cnt, *_ = simulatedAnealing.annealing(n, board)

    end = time.time()

    if flag:
      success3+=1
      steps3 += cnt

    t_time3 += (end-begin-0.1)* 1000

    t-=1

  # print Result

  print("Results")

  print(f"total tests = {t_test}")
  print(f"value of n = {n}")

  
  mytable = [["Simulated Annealing",success3, t_test-success3, steps3/t_test, t_time3/t_test],
		["Hill Climbing With Sideways Moves",success1, t_test-success1, steps1/t_test, t_time1/t_test],
		["Random Restart",success2, t_test-success2, steps2/t_test, t_time2/t_test]]

  # create header
  head = ["Algorithm","Total Success", "Total Faliure", "Average Steps of Success", "Average Time Taken (in ms)"]

  # display table
  print(tabulate(mytable, headers=head, tablefmt="fancy_grid"))
