def sor(x, y, z):

    nums = [x, y, z]
    nums.sort()
    print("Em ordem crescente: %f, %f, %f." % (nums[0], nums[1], nums[2])).rstrip('.').rstrip('0')

x, y, z = float(input("Digite três números: ")), float(input()), float(input())
sor(x, y, z)
