# Analyze five input numbers


def analyze():
    nums = []
    for i in range(5):
        num = int(input(f"Enter number {i + 1}: "))
        nums.append(num)

    count_even = 0
    for n in nums:
        if n % 2 == 0:
            count_even += 1

    print(nums)
    print(f"sum: {sum(nums)}")
    print(f"average: {sum(nums) / len(nums)}")
    print(f"biggest: {max(nums)}")
    print(f"smallest: {min(nums)}")
    print(f"even count: {count_even}")


analyze()
