# Given an integer array nums, find the contiguous subarray
#  (containing at least one number) which has the largest sum and return its sum.

def maxSubarray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    return max(nums)
    # Kadane's Algorithm, runtime: o(n)

# print( maxSubarray( [-32,-54,-36,62,20,76,-1,-86,-13,38,-58,-77,17,38,-17,43,32,-88,-19,-70,95,0,-64,75,15,-87,-26,69,-95,-65,-18,-28,-43,22,-88,54,-25,-13,67,61,-74,-91,60,42,24,-80,-15,-44,-91,42,-38,-96,-58,-3,55,33,-13,-71,2,-9,-60,60,39,-26,-41,50,-72,33,-62,94,-28,-37,79,-68,81,3,-71,-57,35,-63,61,96,-83,-97,-29,48,35,57,76,-86,-52,92,50,86,-34,85,14,-30,18,51,-36,66,90,-79,75,48,0,-96,67,-64,-83,28,-91,-90,30,-44,57,-58,-87,10,-68,-63,-21,81,-76,45,66,14,-85,-39,-58,-44,-95,-68,-47,79,56,52,59,23,64,75,-49,50,61,57,-94,-5,98,95,81,-70,-68,-40,87,-68,-95,30,45,96,90,86,-71,94,94,-19,50,27,-90,9,-50,51,-39,-23,-22,-78,-66,-17,-7,-68,-22,-26,-62,-13,34,-75,18,38,54,-36,11,22,-73,39,-7,98,96,-56,25,83,52,75,34,-86,-48,-88,-88,-14,-29,5,-6,26,78,9,-87,12,10,30,-72,-58,70,15,63,97,-68,-67,95,-72,-24,20,-89,-94,-28,21,-81,1,32,-93,63,80,11,-43,6,-33,42,18,78,-47,-75,82,-6,95,-25,-66,69,6,-57,41,10,19,-62,21,1,10,-81,19,-89,28,2,73,8,-86,-93,-86,-20,49,8,-65,78,32,94,-51,27,-31,-41,-27,51,1,-86,-39,96,-48,58,-3,38,77,92,25,5,-5,-25,89,-15,-42,79,41,83,-13,52,61,-81,23,86,23,68,-55,72,19,23,86,80,19,-85,38,93,29,-8,85,-46,73,-43,5,62,41,62,41,-41,23,-72,-88,-39,-76,34,-52,23,-20,-31,-5,98,91,-19,78,-12,-28,-6,-19,-99,85,-34,-69,59,0,12,-2,-82,-25,-60,-23,74,-56,-35,-65,-33,75,-18,89,-45,51,-38,-46,19,42,-91,-93,91,-21,-13,91,-35,30,99,-99,-70,11,-2,-53,62,14,0,36,58,64,48,-98,40,-70,68,71,57,-70,-75,-23,48,-89,-17,39,-11,70,8,30,-23,-16,7,6,94,82,29,34,-4,-70,-53,-69,70,94,-67,-13,-98,77,-41,58,-93,-40,-88,31,-30,-5,-29,36,-58,55,-34,18,-84,73,-99,86,32,29,20,-72,35,67,-64,6,38,-55,92,39,-78,-72,-2,-95,-12,9,35,34,80,82,-30,-78,14,13,16,29,-37,16,16,94,-54,-87,98,57,56,-66,-37,-5,-22,-44,-66,-24,-17,8,-20,47,94,92,-18,51,74,28,50,-11,-59,-34,94,-20,59,10,-26,-95,23,-27,61,-21,-17,-98,50,38,-66,84,-86,-7,-31,-6,-59,-60,-14,22,91,-63,-73,41,2,-32,83,-3,47,42,83,98,23,6,-52,-38,62,30,-37,12,-32,-4,-27,-18,88,19,52,-94,58,-85,4,26,-72,31,-56,30,75,-72,-73,-1,69,-90,-3,-30,-7,44,31,-68,-48,70,20,19,-57,93,77,-92,12,29,-86,-53,20,17,73,48,-75,-83,-22,76,-79,-19,-24,67,-33,49,-63,36,-29,44,67,22,14,-12,-59,56,-42,-81,40,46,24,53,92,-55,-52,42,92,-51,36,-53,-74,56,4,1,0,70,-73,36,7,-3,-43,-49,95,70,38,-63,3,95,-68,-56,41,32,73,11,76,-79,-47,45,-53,65,68,-28,-1,-28,49,98,-80,75,12,26,-50,68,76,-55,16,-8,-42,-81,-36,-34,-61,-94,98,-87,-7,51,-90,22,-26,-44,-12,-58,4,63,-9,-47,61,10,-94,-50,-87,-68,95,65,-24,11,-43,11,6,-2,76,45,3,74,34,95,26,43,-6,76,76,81,94,-20,44,-15,10,-17,71,-8,9,83,23,4,26,75,-85,59,-37,-2,-43,-60,-57,36,90,53,8,-7,-27,-97,-31,-51,83,-36,6,5,25,92,64,-3,-39,-27,-43,60,77,82,12,68,19,75,-34,75,-85,-15,-11,-95,-62,96,-2,11,98,66,36,59,-93,-81,-59,32,87,-95,-71,-52,-23,-38,-92,-69,-78,20,99,40,-5,-58,-8,-14,27,80,-10,41,77,64,-71,52,8,42,11,14,60,28,-77,48,32,-72,72,86,-10,80,93,11,-23,69,-72,48,-88,19,-89,15,-23,-23,-67,-46,-58,-38,82,26,-96,-29,-83,40,98,-60,-12,31,-33,-62,-6,33,94,-13,-79,-29,-43,-52,95,-55,44,-94,36,-79,-18,68,-49,0,-70,-67,-74,-90,3,-80,50,-21,-41,-85,86,2,-48,-20,-64,-54,43,-44,-7,76,-19,-35,-79,-75,-53,33,-78,6,2,-28,-94,8,-19,-91,18,61,-72,-55,-60,-37,-41,-74,64,-12,-18,76,10,-75,-67,80,-98,-10,-55,98,14,-31,32,35,74,-89,83,56,18,-36,64,-87,-75,68,-43,-59,-69,-7,-57,95,57,24,71,-33,49,80,-53,27,-30,-31,2,60,14,-89,-28,-12,-79,-45,-56,39,-4,-91,28,-3,76,85,38,84,-45,80,79,-88,5,27,-22,-69,-15,2,34,31,47,-64,-8,-39,-53,40,48,-56,95,68,82,-32,76,-12,64,30,-27,-21,14,4,-40,-30,15,41,73,92,48,-42,-29,-18,66,-82,-6,-65,-22,17,74,-97,61,46,71,20,-86,24,-92,55,-69,-43,-66,21,60,-7,67,-25,-89,41,-55,58,75,15,-83,18,10,11,52,64,-72,27,67,65,-50,15,-14,-59,-61,-7,95,-53,50,-71,67,10,-1,35,85,-14,-47,-70,-78,-95,21,-62,23,-69,25,-25,95,30,78,62,-5,-94,-46,80,-54,-8,-26,-59,15,-99,-54,-17,10,21,94,-28,-92,-53,1,-71,-49,99,-34,50,-70,68,-74,-75,-2,80,63,92,85,-83,73,-69,-14,-76,-52,-99,-76,-29,-40,33,91,-46,-94,98,-23,-17,-96,5,-18,-53,-45,-11,-85,-43,13,12,-62,-46,-19,99,-53,-46,-92,9,-46,-45,10,-23,2,46,87,-6,77,69,-31,-46,-71,-27,35,-12,19,90,76,10,-76,-34,-78,-62,19,2,-62,43,33,-55,-48,86,-24,38,-59,55,-15,-72,-74,-38,73,-6,-8,-98,43,-72,-11,-61,94,-35,48,94,31,46,-67,-73,-74,-53,46,58,-32,98,21,43,36,38,-25,97,65,0,-64,38,94,5,17,14,9,-94,53,3,-52,-22,-26,55,-75,6,58,-73,52,5,84,-80,3,-18,40,-84,-79,-85,-86,62,15,-74,-22,-14,30,94,99,-84,76,29,-5,-76,84,69,55,-91,-25,14,-88,-95,-81,72,-76,21,-46,40,36,-49,32,26,-86,-53,29,-32,9,-64,-61,-15,-48,-85,-85,46,-84,98,15,70,83,67,-16,94,71,2,66,71,-77,96,12,36,-52,-56,-61,-62,-33,44,-18,52,80,20,-63,-68,34,-72,54,49,-97,-30,20,62,-86,80,33,84,-17,-24,55,-18,-27,-56,94,-3,-36,-66,11,7,77,92,-41,34,12,-27,65,-77,-23,-3,72,-20,43,-31,-81,56,-51,52,40,8,-72,-28,90,-23,-7,84,50,33,-82,-62,-59,72,-93,-24,6,18,48,-51,18,-74,45,-10,-18,-12,35,0,-79,83,-71,37,-31,-66,-91,-41,-13,-22,-57,-62,-88,-62,-48,-71,-90,-41,4,-8,53,-70,40,-29,-68,-38,37,13,26,-28,89,46,-67,-81,-17,1,-48,-31,36,38,46,78,52,34,-84,81,62,-98,-60,-56,-29,69,-27,-89,-82,4,-50,54,93,75,-96,82,22,-64,-99,-95,13,-71,-50,-51,67,96,-96,-4,30,96,-23,-30,74,-7,13,-55,-37,85,-67,-20,-34,-18,-66,-41,-43,-63,-82,55,-51,-81,37,38,-53,86,63,90,59,67,-13,-33,63,40,36,37,-66,-51,82,-4,-89,91,52,-24,-27,85,11,6,99,28,-61,-75,23,75,40,47,38,3,37,-2,-30,-99,64,-67,41,-23,47,74,2,6,-53,12,-3,98,64,69,60,-48,-48,36,79,-10,61,-20,-58,-22,-73,80,80,63,-45,-49,41,95,-40,-18,-28,-93,-67,73,12,-21,-38,-91,-46,-97,54,-86,-46,-93,50,-67,-27,-12,-11,15,65,15,-28,22,-44,3,72,96,-2,-90,-45,46,92,-36,-4,-18,19,57,-33,72,59,-78,62,-87,-95,-11,-78,-46,76,11,68,18,-74,-83,-82,-42,19,89,-46,-83,75,-15,62,68,48,-42,-50,-33,91,16,-84,50,14,78,39,-5,-33,38,49,-79,-51,-6,15,-49,11,32,9,-70,-1,39,-53,-26,-75,85,-81,49,-79,-55,-83,88,38,-91,39,-48,63,-45,24,-69,92,-27,-72,-82,66,42,-54,-23,-48,31,7,50,-30,30,-99,-29,-8,-80,-79,-11,-36,-86,-22,78,-78,93,-69,85,-52,54,92,-82,-96,-80,-88,69,38,-43,-76,89,87,7,16,-65,-63,17,5,5,13,25,94,53,15,-28,32,37,-58,39,-1,-34,-30,-9,-17,-27,-13,-28,-81,-98,28,-58,68,-7,48,-16,27,61,-99,-91,-56,-10,34,-62,-56,-51,-14,52,62,27,-9,-39,92,60,28,-47,-90,91,24,-72,93,-71,-53,38,21,94,-78,-75,33,99,-66,76,-11,67,90,9,92,-24,-39,32,79,51,69,71,-12,-25,-99,-3,-34,24,25,-64,53,48,73,-49,19,72,-24,-48,71,9,-95,-63,-47,94,46,-78,-30,-93,53,-74,35,0,74,-77,74,74,20,-83,-24,-78,-70,-94,46,79,-44,-35,51,8,17,22,93,21,59,-77,16,-18,-55,62,-12,74,88,99,-26,62,-77,-75,13,19,-58,88,17,-29,93,-37,-50,-50,27,78,57,-56,0,28,42,-64,50,-65,17,94,73,82,46,61,81,96,0,80,98,-86,-1,-60,78,92,-13,72,-45,13,98,82,-9,32,-97,68,-40,21,-96,-89,55,-2,81,29,-43,4,-33,-85,1,44,95,-1,34,-29,15,12,-36,-98,-39,18,-9,-41,-23,82,91,-43,50,-72,77,30,-62,10,-95,-80,-84,-39,23,-41,-47,-99,-97,-75,-24,13,-5,90,-74,35,68,-37,-69,-40,22,-16,-58,-10,40,68,17,-5,-2,32,-95,-20,51,-80,40,-49,-45,69,-71,-42,93,4,47,-34,-5,49,-99,-37,-87,-92,-1,11,-8,17,-99,-68,-15,-6,26,60,-74,7,-60,76,26,56,-95,81,26,-67,-84,19,13,39,61,-92,-11,62,-52,1,69,23,-88,-39,-59,-88,-30,25,-18,95,-15,8,3,24,-39,-94,-42,-35,63,83,-26,55,-21,87,-5,-59,71,83,79,95,-39,48,19,-28,86,59,-40,-67,-16,41,-95,46,-74,-16,-53,-13,-33,4,51,-70,-13,-97,62,43,66,-66,83,37,93,39,10,-46,-36,-71,2,-50,87,38,-41,-52,-44,-36,70,-18,47,-82,68,-86,21,-4,-79,85,-2,59,28,-59,92,-12,78,62,-73,-35,-84,-10,-7,17,17,-43,-68,75,4,-13,-84,-25,68,40,-31,36,30,89,-67,50,51,7,-14,-44,48,-45,43,3,-83,46,67,-68,-86,-40,25,7,-7,56,-41,73,-79,-25,-52,88,-85,-7,25,44,-17,34,-28,-89,-82,34,-33,65,89,-90,-55,-94,33,-88,-85,46,-52,16,-47,40,-50,11,14,-30,62,38,-42,53,-68,59,-25,-9,-30,23,1,-12,-43,67,-70,-54,54,-25,-71,-13,-14,-57,-90,11,58,-61,-72,-92,49,41,-23,-11,-43,12,-58,-12,-52,16,55,18,-61,-44,-94,-27,-99,-65,18,54,-14,23,-82,49,65,-73,-40,1,-35,-13,-15,90,-94,39,-21,-38,-49,-2,26,-2,-86,-42,92,-70,13,74,2,-10,86,96,-56,-28,20,-39,-79,-38,-36,-20,62,28,44,-52,-4,49,63,74,87,-86,-51,-10,-12,-60,47,-19,-31,-63,-68,47,27,-82,43,47,-10,-60,-91,10,2,-28,67,-59,77,-12,-35,-27,-86,-72,-76,-99,-82,-27,-33,6,12,90,63,57,-73,94,4,30,-87,-76,-22,-21,-36,-37,88,42,11,32,82,-35,-80,-52,37,-67,-25,38,-90,-7,87,-47,75,-1,-57,15,-67,-53,9,36,53,-2,36,-69,76,99,-30,42,18,58,-26,1,-77,-29,48,37,-20,99,-25,-10,-8,-38,42,-56,37,62,58,69,-91,-32,-18,61,42,94,69,-4,94,-84,-62,-11,73,-12,89,73,35,14,10,-84,14,61,-18,82,99,-99,-73,36,62,84,-18,47,-71,40,9,71,34,-45,-56,5,-30,-42,94,-79,45,60,93,-42,-25,-20,-27,88,-59,54,70,-60,54,96,52,-6,58,-89,-59,86,27,26,34,-39,80,77,43,-72,-65,37,-75,57,-3,-82,-85,71,-3,-36,36,14,94,-16,30,48,-20,-18,-81,-85,-31,-40,78,95,85,12,-67,43,-33,75,47,-22,-11,48,-88,86,65,-74,34,-61,-34,-52,29,-40,31,-41,85,87,40,-96,-97,85,-60,80,80,-97,-31,-87,45,35,65,-31,90,-46,-83,-98,-83,58,-95,28,73,-30,75,2,7,-17,60,-8,-30,-23,-28,-51,-38,12,-94,-81,14,-25,-92,-64,86,72,4,53,-73,-3,55,-57,-68,59,70,-95,-94,22,-17,-11,-95,-57,80,-48,-4,-47,0,57,64,6,52,-45,57,59,-10,43,32,70,-3,35,-33,-71,77,-2,64,25,-21,46,-76,61,-64,-94,80,92,-43,-24,-55,56,-90,85,-61,61,-83,95,20,6,16,-71,-24,89,63,19,94,18,93,58,-80,-28,4,-57,-90,16,-52,89,9,4,-58,30,-62,-49,-7,-24,-88,9,-51,9,-84,41,37,-32,30,1,87,24,-81,80,-41,-62,-70,39,-43,-61,-44,-18,-94,41,85,-53,-29,99,-25,63,-47,-14,-27,1,94,-35,-58,9,32,48,-90,19,-51,-95,-23,-16,-81,-17,-77,-48,-2,-45,33,3,95,-4,27,-33,-5,-98,-93,47,-36,-44,-52,-64,20,-34,44,-70,90,30,25,-61,11,-98,-1,6,-16,22,57,82,76,-9,-38,49,63,65,92,-42,43,98,-94,-92,-45,-70,-57,51,-27,63,80,-37,-7,6,-21,80,-16,77,-14,45,-24,-80,27,-70,-13,65,78,-50,8,47,8,-49,45,-10,-42,76,19,-23,5,68,-83,-15,-91,-14,67,-13,-34,-48,-59,51,96,-6,48,0,23,-65,-58,-22,-15,49,-75,92,-99,46,-41,-65,0,77,-11,-95,23,5,-11,31,91,-66,-82,-43,-15,-65,85,-42,28,33,57,-72,44,98,-18,-71,48,-17,97,25,-70,-44,59,6,-89,-52,10,33,53,75,-36,44,-91,-42,77,-30,-8,39,27,97,-51,-16,-98,93,-40,-16,-78,84,66,-80,9,72,-48,-32,-45,-38,-7,64,94,-77,17,-42,43,25,-8,20,72,84,-63,-1,58,-15,60,59,-22,-80,-80,0,80,63,-4,-11,35,47,33,90,-90,-97,31,80,-75,-52,-84,67,50,7,-35,-1,-32,1,97,-74,85,34,62,-59,30,81,40,10,44,-87,98,-43,36,9,-76,45,11,54,3,36,79,18,-20,6,-98,44,-95,-30,-78,78,-28,84,13,-66,-75,-57,92,41,30,36,53,5,69,-11,-86,92,-88,2,24,-9,-85,-20,-91,-6,85,-90,-84,66,-44,-86,44,28,97,-66,61,98,-23,53,39,83,-33,-31,-12,-87,35,2,82,46,80,6,-63,94,62,-78,-12,24,-92,-20,-10,-36,-6,-89,68,-32,-55,29,-33,-2,-40,82,-19,3,-48,68,15,86,-53,-3,9,-73,79,22,-79,41,43,-14,-35,27,42,31,67,-64,42,35,-19,86,-58,47,-16,1,29,64,80,57,9,-5,43,56,69,-71,82,48,50,-96,-33,-30,-34,8,97,-92,-83,41,-79,58,-23,1,21,18,-75,81,95,30,22,75,-12,-69,-53,-92,86,-84,-63,46,41,86,26,84,-66,91,-31,-69,98,-15,48,95,-80,-75,-4,40,42,-3,-2,14,-72,96,-11,15,-72,36,-1,90,28,35,36,-54,-1,-61,-93,32,-70,-24,39,-94,60,-13,-99,57,-11,-26,-26,-92,70,72,22,97,68,-89,-11,72,23,88,63,-71,0,-24,-26,75,15,-42,-16,21,33,-77,26,-30,-13,4,-73,75,77,1,82,47,-50,4,22,-82,-8,-89,67,91,75,30,-80,-47,82,-29,-72,-26,28,12,95,-62,11,-2,7,97,-98,11,49,55,88,9,3,-62,89,-75,-68,-19,-88,98,-27,87,5,-31,-60,-35,39,-56,38,-56,55,10,-19,-33,85,88,-59,86,-24,90,19,-36,-24,-78,-22,-35,-77,9,23,-66,-15,72,97,66,-59,-86,-69,80,-42,46,-76,89,-67,-18,-67,-82,-53,-26,81,22,-59,0,62,16,21,-60,57,20,25,-20,30,86,-48,5,53,-7,18,60,-50,52,6,-50,19,39,31,51,33,77,-75,14,-24,-58,-86,-62,34,11,-23,-8,-69,79,71,38,65,-99,-57,18,-7,37,-21,19,-33,61,45,85,-23,-23,36,-89,-69,38,24,7,79,38,21,14,-74,75,-94,-66,54,53,71,19,53,-86,-85,-77,27,-30,18,93,-92,-36,78,-15,17,-8,-5,47,-70,95,-69,85,10,52,-24,36,27,-42,69,-42,-88,40,53,41,30,44,64,-66,-86,-18,-72,98,22,82,-17,-61,-49,54,63,-43,49,93,-57,-40,22,-5,72,-74,53,41,-40,64,-42,-86,5,64,57,-54,74,48,5,78,46,-73,38,-94,-34,88,59,-71,-54,-15,98,93,-67,36,-15,-26,35,-56,-13,81,66,60,-58,-91,-14,-34,-30,41,23,-1,-38,86,12,85,-79,-80,-36,-94,-85,91,1,-54,61,33,82,-53,-93,-6,-10,-30,-25,-43,-93,16,-58,-30,59,12,-89,-18,87,-28,-55,-24,-66,-58,-5,-2,-52,-14,-34,25,32,-73,-41,14,-27,-58,-92,40,-11,-40,96,-28,52,-62,41,11,26,52,69,-10,-99,90,65,-65,-67,-39,9,-20,23,51,81,-68,77,-60,45,-72,-41,30,44,24,89,40,95,41,54,37,-70,-42,-34,98,47,-34,89,13,-23,98,50,62,-22,-50,13,-41,-18,-32,-24,-96,-28,11,33,-84,-65,-1,32,-93,-82,-14,43,-53,43,-91,-78,-32,-48,87,57,28,85,7,-9,-60,33,-96,-24,-85,-52,51,-81,19,-61,28,11,-50,-95,-57,-44,-78,6,99,-55,-74,84,-34,-7,-64,-46,-50,41,-84,33,-68,-44,-33,-88,31,-19,-40,-41,-24,55,-3,-95,-33,23,-91,9,78,-93,91,54,-49,-82,16,-7,10,51,46,60,-8,62,-7,0,94,36,12,25,-82,48,83,-30,-20,-43,-49,46,79,-64,-67,34,-58,-99,-11,-8,-82,-95,62,28,32,-15,-35,-98,-76,34,-22,-82,-29,66,42,-35,-9,2,34,71,35,85,-6,-9,-79,3,-74,-60,4,-9,8,21,-28,-30,-51,80,55,-10,81,78,-75,-63,96,-28,-97,15,36,-6,-82,-53,-58,29,-91,35,-79,-93,-61,-54,-54,19,13,53,-60,84,-99,-34,64,55,55,23,10,56,59,6,-72,38,-78,40,-91,-84,87,-50,44,72,85,41,78,-99,86,-99,19,-24,31,35,-40,31,-99,-98,-37,33,24,72,-11,-40,-21,-6,74,-23,-66,83,-31,97,-67,89,70,94,31,25,94,-6,3,-10,70,-66,-74,-70,41,-97,-92,-96,35,8,75,-98,67,-69,-28,19,-16,-18,2,52,-20,11,42,-73,6,-27,28,-23,43,-69,67,13,-59,92,20,81,71,27,84,7,-64,37,-15,79,67,56,-2,-48,-62,76,80,-6,-12,-1,-3,70,48,-74,-53,-8,-67,90,-95,-26,59,1,-45,31,-71,-60,-85,-59,53,-1,96,20,-45,-5,48,-31,-52,6,63,12,-95,-40,-18,53,-38,6,-55,-5,-4,-74,68,-67,27,-77,63,32,-61,77,49,91,-24,45,-11,7,-83,-86,52,-35,19,15,76,24,52,-64,-46,90,41,-25,-15,-86,0,-47,-54,-96,-47,85,35,-32,62,-39,-40,-85,-93,25,-2,-77,38,-49,-36,-65,42,-82,35,-29,-47,88,-38,70,-37,46,60,39,76,83,43,-94,68,-45,-27,8,16,32,-1,22,-66,74,21,49,-98,85,83,43,79,18,91,-91,-17,-70,55,22,52,15,-39,28,-25,-96,10,-56,-64,83,28,51,-8,-96,-50,26,77,70,-25,78,32,-42,-1,-12,52,-10,-4,-88,-4,-49,33,-52,43,93,53,-82,97,-37,-62,-67,-54,65,60,38,46,-90,-59,23,56,15,2,-34,49,-99,53,-22,-33,-73,-11,62,-23,-78,86,-80,-85,39,-85,88,79,-48,97,-75,94,57,39,40,43,79,-60,-23,-29,41,42,96,18,-28,-26,61,-2,62,0,52,60,-13,48,75,-97,39,40,81,91,38,-93,62,-28,22,-21,-84,-21,18,-8,49,-63,-89,46,54,-41,96,16,34,36,-84,-14,-4,-21,-89,-52,-18,50,88,-37,18,3,-54,-43,74,68,35,89,-76,-70,-42,72,-34,-55,-5,-79,4,-8,13,-62,-95,5,0,0,61,10,48,-57,-63,13,-18,31,-84,28,87,89,-27,-1,56,-4,29,90,-55,94,-64,17,91,39,85,-19,53,89,63,-47,-11,24,39,-86,66,76,3,-75,-16,-5,29,-51,-38,-98,47,-82,-26,-47,84,-4,-52,-80,-87,-84,35,97,-26,-12,63,-63,17,-71,60,-43,-80,26,-90,22,27,-7,-82,-43,41,-21,-65,-11,-27,-14,18,-66,81,65,-46,70,58,65,44,-68,-69,7,-32,47,35,-72,-96,54,30,-87,-46,-43,-17,-29,-10,-76,26,25,-11,75,-89,-92,-91,68,49,-61,38,-16,-95,-18,15,-88,65,59,58,0,63,62,-68,-30,51,-15,4,-66,32,93,-65,-65,18,23,-90,5,7,94,-27,-66,-89,87,17,-85,-54,-90,-97,-89,68,60,-12,9,-1,-4,78,-49,80,-18,-39,-11,-47,-5,23,47,95,9,-47,2,-20,2,12,-10,-10,-70,-19,12,-84,-17,23,60,-56,87,-31,42,-17,-52,69,-60,6,-69,5,58,25,-95,6,20,-10,35,99,69,-63,11,-63,3,17,17,-84,32,77,15,-7,97,2,61,39,61,85,-14,77,-31,16,-18,-96,-82,-14,9,15,75,-79,-9,21,-42,-98,57,37,-4,-25,52,-72,-71,-33,-3,-74,45,-64,41,-17,97,-73,-40,-34,19,41,-30,37,-73,55,-71,78,53,19,0,-89,-3,-43,47,92,8,-23,97,36,43,-29,61,-34,6,3,48,4,6,85,46,-74,26,92,39,30,25,67,-15,-22,-14,84,-35,82,-81,88,75,26,-35,49,-60,85,-80,77,-49,3,-43,75,-93,63,60,29,65,-36,-1,4,70,-76,-29,-45,1,56] ) )