import time
def main():
  for i in range(1000):
      print(i)


start_time = time.time()
main()
print(time.time() - start_time)