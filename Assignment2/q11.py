
import random
def biased_coin_flip(bias):
  
  random_number = random.random()

  if random_number < bias:
    return "Heads"
  else:
    return "Tails"
  


def simulate_flips(number_of_flip,bias):

  result={
      "Heads":0,
    "Tails":0
  }
  
  
  for _ in range(number_of_flip):
    flip_bias_res=biased_coin_flip(bias)
    result[flip_bias_res] += 1
    
  return result


number_of_flips = 100
bias = 0.60  # 60% chance of heads

flip_results = simulate_flips(number_of_flips, bias)

print(f"Results of {number_of_flips} biased coin flips with {bias:.2f} bias:")
print(f"Heads: {flip_results['Heads']}")
print(f"Tails: {flip_results['Tails']}")