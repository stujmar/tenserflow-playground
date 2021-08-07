# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]



py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, dev_y, color='b', label='All Devs')
plt.plot(ages_x, py_dev_y, color='g', label='Python')


plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()

# You can pass all the lengend info like this.
# plt.legend(['All Devs', 'Python Devs'])

plt.show()